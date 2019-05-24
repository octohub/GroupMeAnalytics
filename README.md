# GroupMeAnalytics
GroupMe (https://groupme.com/) provides an API (https://dev.groupme.com/docs/v3) that allows users to parse messages in groups they are a part of.

This program compiles data on all users in one group. Information provided for each user includes the number of messages sent, number of likes iven, number of likes given to one's own messages, likes received, average number of likes received per message, total likes not including self likes, average likes per message without self likes, total number of words sent, rates of receiving and giving likes from and to each other member in the group, and rates of sharing likes with other members.

## Prerequisites
This program requires Python 3, which can be obtained [here](https://www.python.org/downloads).

## Use
- Obtain your GroupMe API Access Key using your regular account credentials by logging in [here](https://dev.groupme.com/session/new).
- Click the button reading "Access Token" in the top right of the page. Take note of the token that is shown, but do not share it with anyone.
- Run the app with your API key as a parameter:
```py
python3 analyze.py xxxxxxxxxxxxxxxxxxxxxxxxxxx
```
