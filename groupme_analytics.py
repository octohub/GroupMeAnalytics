import requests
import re
import sys
from pprint import pprint


def get_groups():
    response = requests.get('https://api.groupme.com/v3/groups?token='+TOKEN)
    return response.json()['response']


def log_groups(groups):
    if len(groups) == 0:
        print("You are not part of any groups.")
        return
    for i, group in enumerate(groups):
        print('%d. %s' % (i, group['name']))


def new_user(name):
    return {"name": name, "messages_sent": 0, "likes_given": 0, "likes_received": 0.0, "words_sent": 0, "likes_by_member": {}, "shared_likes": {}, "self_likes": 0}


def prepare_user_dictionary(members):
    return {member['user_id']: new_user(member['name']) for member in members}


def analyze_group(group, users, message_count):
    message_id = 0
    message_number = 0
    while message_number < message_count:
        params = {
            # Get maximum number of messages at a time
            "limit": 100,
        }
        if message_id:
            params["before_id"] = message_id
        response = requests.get("https://api.groupme.com/v3/groups/%s/messages?token=%s" % (group['id'], TOKEN), params=params)
        messages = response.json()["response"]["messages"]
        for message in messages:
            message_number += 1

            name = message['name']
            text = message['text']
            try:
                #  strips out special characters
                message_with_only_alphanumeric_characters = re.sub(r'\W+', ' ', text)
            except ValueError:
                pass  # this is here to catch errors when there are special characters in the message e.g. emoticons
            sender_id = message['sender_id']
            likers = message['favorited_by']

            # Count words in message
            message_word_count = len(re.findall(r'\w+', str(message_with_only_alphanumeric_characters)))

            if sender_id not in users.keys():
                users[sender_id] = new_user(name)

            # Fill in name if it's not in the dictionary
            if not users[sender_id]['name']:
                users[sender_id]['name'] = name

            for user_id in likers:
                users[sender_id]['likes_by_member'][user_id] += 1

            # Count shared likes
            for user_id in likers:
                for user_id_inner in likers:
                    if user_id not in users.keys():
                        # Leave name blank for now
                        users[user_id] = new_user('')
                    if user_id == user_id_inner:
                        users[user_id]["self_likes"] += 1
                        continue  # pass because you don't want to count yourself as sharing likes with yourself
                    users[user_id]["shared_likes"][user_id_inner] += 1
            users[sender_id]["messages_sent"] += 1  # add one to sent message count
            users[sender_id]["likes_received"] += len(likers)
            users[sender_id]["words_sent"] += message_word_count

        message_id = messages[-1]["id"]  # Get last message's ID for next request
        remaining = 100 * message_number / message_count
        print("%.2f%% done\r" % remaining, end="")
    return users


def display_data(users):
    for key in users:
        try:
            likes_per_message = users[key]["likes_received"] / users[key]["messages_sent"]
        except ZeroDivisionError:
            likes_per_message = 0
        print(('{name} | Messages sent: {messages}, Likes given: {likes}, Self-likes: {self_likes}, Likes received: {likes_received}, ' +
            'Avg. Likes per message: {likes_per_message}, Words sent: {words_sent}'
                ).format(name=users[key]["name"],
                        messages=users[key]["messages_sent"],
                        likes=users[key]["likes_given"],
                        self_likes=users[key]["self_likes"],
                        likes_received=users[key]["likes_received"],
                        likes_per_message=likes_per_message,
                        words_sent=users[key]["words_sent"]))

        """
        print('Likes Received from each member and also what percent of the total likes received is from said member :')
        for key_inner in users[key][5]:
            percent = (users[key][5][key_inner] / users[key][2]) * 100
            percent = round(percent, 2)
            sys.stdout.write(users[key_inner][0])  # Name of liker
            sys.stdout.write(' : ' + str(users[key][5][key_inner]) + ', ') # number of likes to user
            sys.stdout.write(str(percent) + '%, ')
        print

        print('Percent of each member\'s total likes that went to ' + str(users[key][0]) + ': ')
        for key_inner in users[key][5]:
            sys.stdout.write(users[key_inner][0])
            convert_to_percent = (users[key][5][key_inner] /
                                  users[key_inner][7]) * 100
            convert_to_percent = round(convert_to_percent, 2)
            sys.stdout.write(': ' + str(convert_to_percent) + '%, ')
        print

        test = users[key][6]
        print('Number of times you liked the same post as another member and what percent of the posts you '
              'liked were liked by that same member: ')
        for key_inner in users[key][6]:
            percent_shared = (users[key][6][key_inner]/users[key][7])*100
            percent_shared = round(percent_shared, 2)
            sys.stdout.write(users[key_inner][0])
            sys.stdout.write(': ' + str(users[key][6][key_inner]) + ', ')
            sys.stdout.write(str(percent_shared)+'%, ')
        """


print('If you have not done so already, go to the following website to receive your API token: ' +
      'https://dev.groupme.com/. When signing up, it does not matter what you put for the callback URL. ' +
      'Alternately, click "Access Token" to use your account for authentication.')
TOKEN = input("Enter your developer access token: ")
groups = get_groups()
log_groups(groups)

try:
    group_number = int(input("Enter the number of the group you would like to analyze: "))
except ValueError:
    print("Not a number")

group = groups[group_number]

# Display basic group data before analysis
group_name = group['name']
message_count = group['messages']['count']
print("Analyzing %d messages from %s" % (message_count, group_name))

# Put all the members currently in group into a dict
members = group['members']
users = prepare_user_dictionary(members)

# Iterate through messages to collect data
users = analyze_group(group, users, message_count)

# Show data
display_data(users)
