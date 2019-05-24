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

**Make this all seem official**
The MIT License (MIT)

Copyright (c) 2014 Richard Lucas

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
