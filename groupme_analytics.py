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
    return {"name": name, "messages_sent": 0, "likes_given": 0, "likes_per_message": 0.0, "words_sent": 0, "likes_by_member": {}, "shared_likes": {}}


def prepare_user_dictionary(members):
    return {member['user_id']: new_user(member['name']) for member in members}


def analyze_group(group_id, user_id_mapped_to_user_data, number_of_messages):
    message_id = 0
    message_number = 0
    while message_number < message_count:
        params = {
            # Get maximum number of messages at a time
            "limit": 100,
        }
        if message_id:
            params["before_id"] = message_id
        response = requests.get("https://api.groupme.com/v3/groups/%d/messages?token=%s" % (group_id, at), params=params)
        messages = response.json()["response"]["messages"]
        for message in messages:
                iterations += 1
                name = data['response']['messages'][i]['name']  # grabs name of sender
                message = data['response']['messages'][i]['text']  # grabs text of message
                #print(message)
                try:
                    #  strips out special characters
                    message_with_only_alphanumeric_characters = re.sub(r'\W+', ' ', str(message))
                except ValueError:
                    pass  # this is here to catch errors when there are special characters in the message e.g. emoticons
                sender_id = data['response']['messages'][i]['sender_id']  # grabs sender id
                list_of_favs = data['response']['messages'][i]['favorited_by']  # grabs list of who favorited message
                length_of_favs = len(list_of_favs)  # grabs number of users who liked message


                #grabs the number of words in message
                number_of_words_in_message = len(re.findall(r'\w+', str(message_with_only_alphanumeric_characters)))

                if sender_id not in user_id_mapped_to_user_data.keys():
                    user_id_mapped_to_user_data[sender_id] = [name, 0.0, 0.0, 0.0, 0.0, {}, {}, 0.0]

                #this if statement is here to fill the name in for the case where a user id liked a message but had
                #yet been added to the dictionary
                if user_id_mapped_to_user_data[sender_id][0] == '':
                    user_id_mapped_to_user_data[sender_id][0] = name

                for user_id in list_of_favs:
                    if user_id in user_id_mapped_to_user_data[sender_id][5].keys():
                        user_id_mapped_to_user_data[sender_id][5][user_id] += 1
                    else:
                        user_id_mapped_to_user_data[sender_id][5][user_id] = 1

                for user_id in list_of_favs:
                    for user_id_inner in list_of_favs:
                        if user_id not in user_id_mapped_to_user_data.keys():
                            # leave name blank because this means a user is has liked a message but has yet to be added
                            # to the dictionary. So leave the name blank until they send their first message.
                            user_id_mapped_to_user_data[user_id] = ['', 0.0, 0.0, 0.0, 0.0, {}, {}, 0.0]
                        if user_id == user_id_inner:
                            user_id_mapped_to_user_data[user_id][7] += 1
                            continue  # pass because you don't want to count yourself as sharing likes with yourself
                        try:
                            user_id_mapped_to_user_data[user_id][6][user_id_inner] += 1
                        except KeyError:
                            user_id_mapped_to_user_data[user_id][6][user_id_inner] = 1

                user_id_mapped_to_user_data[sender_id][1] += 1  # add one to sent message count
                user_id_mapped_to_user_data[sender_id][2] += length_of_favs
                user_id_mapped_to_user_data[sender_id][4] += number_of_words_in_message

        print("COMPLETE")
        print
        for key in user_id_mapped_to_user_data:
            try:
                user_id_mapped_to_user_data[key][3] = user_id_mapped_to_user_data[key][2] / user_id_mapped_to_user_data[key][1]
            except ZeroDivisionError:  # for the case where the user has sent 0 messages
                user_id_mapped_to_user_data[key][3] = 0
        return user_id_mapped_to_user_data

        if i == 19:
                message_id = data['response']['messages'][i]['id']
                remaining = iterations/number_of_messages
                remaining *= 100
                remaining = round(remaining, 2)
                print(str(remaining)+' percent done')

        payload = {'before_id': message_id}
        response = requests.get('https://api.groupme.com/v3/groups/'+group_id+'/messages?token='+TOKEN, params=payload)
        data = response.json()


def display_data(user_id_mapped_to_user_data):

    for key in user_id_mapped_to_user_data:
        print(user_id_mapped_to_user_data[key][0] + ' Data:')
        print('Messages Sent: ' + str(user_id_mapped_to_user_data[key][1]))
        print('Total Likes Given: ' + str(user_id_mapped_to_user_data[key][7]))
        try:
            print('Self Likes: ' + str(user_id_mapped_to_user_data[key][5][key]))
            self_likes = user_id_mapped_to_user_data[key][5][key]
        except KeyError:
            self_likes = 0
            print('Self Likes: ' + str(0))
        print('Total Likes Received: ' + str(user_id_mapped_to_user_data[key][2]))
        print('Average Likes Received Per Message: ' + str(user_id_mapped_to_user_data[key][3]))

        print('Total Likes Received with Self Likes Subtracted: ' +
              str(user_id_mapped_to_user_data[key][2] - self_likes))

        total_likes_minus_self_likes = user_id_mapped_to_user_data[key][2] - self_likes
        try:
            new_avg = total_likes_minus_self_likes / user_id_mapped_to_user_data[key][1]
        except ZeroDivisionError:  # for the case where the user has sent 0 messages
            new_avg = 0
        print('Average Likes Received Per Message with Self Likes Subtracted: '
              + str(new_avg))

        print('Total Words Sent: ' + str(user_id_mapped_to_user_data[key][4]))

        print('Likes Received from each member and also what percent of the total likes received is from said member :')
        for key_inner in user_id_mapped_to_user_data[key][5]:
            percent = (user_id_mapped_to_user_data[key][5][key_inner] / user_id_mapped_to_user_data[key][2]) * 100
            percent = round(percent, 2)
            sys.stdout.write(user_id_mapped_to_user_data[key_inner][0])  # Name of liker
            sys.stdout.write(' : ' + str(user_id_mapped_to_user_data[key][5][key_inner]) + ', ') # number of likes to user
            sys.stdout.write(str(percent) + '%, ')
        print

        print('Percent of each member\'s total likes that went to ' + str(user_id_mapped_to_user_data[key][0]) + ': ')
        for key_inner in user_id_mapped_to_user_data[key][5]:
            sys.stdout.write(user_id_mapped_to_user_data[key_inner][0])
            convert_to_percent = (user_id_mapped_to_user_data[key][5][key_inner] /
                                  user_id_mapped_to_user_data[key_inner][7]) * 100
            convert_to_percent = round(convert_to_percent, 2)
            sys.stdout.write(': ' + str(convert_to_percent) + '%, ')
        print

        test = user_id_mapped_to_user_data[key][6]
        print('Number of times you liked the same post as another member and what percent of the posts you '
              'liked were liked by that same member: ')
        for key_inner in user_id_mapped_to_user_data[key][6]:
            percent_shared = (user_id_mapped_to_user_data[key][6][key_inner]/user_id_mapped_to_user_data[key][7])*100
            percent_shared = round(percent_shared, 2)
            sys.stdout.write(user_id_mapped_to_user_data[key_inner][0])
            sys.stdout.write(': ' + str(user_id_mapped_to_user_data[key][6][key_inner]) + ', ')
            sys.stdout.write(str(percent_shared)+'%, ')
        print
        print
    #uncomment this line below to view the raw dictionary
    #pprint(user_id_mapped_to_user_data)


print('If you have not done so already, go to the following website to receive your API token: ' +
      'https://dev.groupme.com/. When signing up, it does not matter what you put for the callback URL. ' +
      'Alternately, click "Access Token" to use your account for authentication.')
TOKEN = input("Enter your developer access token:")
groups = get_groups()
log_groups(groups)

try:
    group_number = int(input("Enter the number of the group you would like to analyze: "))
except ValueError:
    print("Not a number")

group = groups[group_number]

# Display basic group data before analysis
group_name = group['name']
number_of_messages = group['messages']['count']
print("Analyzing %d messages from %s" % (number_of_messages, group_name))

# Put all the members currently in group into a dict
members = group['members']
user_dictionary = prepare_user_dictionary(members)

# Iterate through messages to collect data
user_id_mapped_to_user_data = analyze_group(group_id, user_dictionary, number_of_messages)

# Show data
display_data(user_id_mapped_to_user_data)
