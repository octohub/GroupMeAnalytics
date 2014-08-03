GroupMeAnalytics
================

Groupme (https://groupme.com/) provides an awesome API (https://dev.groupme.com/docs/v3) that allows users to parse conversations in groups they are a part of.

**What information does it give me about the members in my groups?**  
-Number of messages sent.  
-Total Likes Given.  
-Self Likes. (special rung in hell for people that like their own messages)
-Total Likes Received.  
-Average Likes Received Per Message.  
-Total Likes Received with Self Likes Subtracted.  (because inflating your numbers isn't cool)  
-Average Likes Received Per Message with Self Likes Subtracted.  
-Total Words Sent.  
-Likes Received from each member and also what percent of the total likes received is from said member.  
-Percent of each member's total likes that went to a particular member.  
-Number of times you liked the same post as another member and what percent of the posts you liked were liked by that same member.  



**How to use it?**  
-Get your groupme API key using your regular account credentials by logging in here: https://dev.groupme.com/session/new  
-Click the shiny orange button "Create Application" and fill out the form. Doesn't matter what you put in these fields, for the callback URL you can simply put in "https://example.com/oauth_callback"  
-After that, go to your application page and you will see your access token  
-Grab python 2.7.x (not compatible with python 3.4.x) from here: https://www.python.org/downloads/  
-Clone the code from this repo and copy in your API token when the python app prompts you  

**Help!**
Feel free to reach out to me on github or twitter(https://twitter.com/dickclucas).
  
**Here is data from one of my groups (with names changed of course):**
Bob Data:  
Messages Sent: 522.0  
Total Likes Given: 870.0  
Self Likes: 0  
Total Likes Received: 1182.0  
Average Likes Received Per Message: 2.26436781609  
Total Likes Received with Self Likes Subtracted: 1182.0  
Average Likes Received Per Message with Self Likes Subtracted: 2.26436781609  
Total Words Sent: 5954.0  
Likes Received from each member and also what percent of the total likes received is from said member :  
John : 147, 12.44%, Tim : 98, 8.29%, Philip : 29, 2.45%, Jane : 18, 1.52%, Mary : 384, 32.49%, Patrick : 355, 30.03%, Anthony : 82, 6.94%, Morgan : 35, 2.96%, Paul : 34, 2.88%,   
Percent of each member's total likes that went to Bob:   
John: 39.84%, Tim: 29.08%, Philip: 19.86%, Jane: 28.57%, Mary: 32.08%, Patrick: 32.66%, Anthony: 28.57%, Morgan: 26.52%, Paul: 27.64%,  
Number of times you liked the same post as another member and what percent of the posts you liked were liked by that same member:  
John: 150, 17.24%, Tim: 130, 14.94%, Philip: 76, 8.74%, Jane: 38, 4.37%, Mary: 452, 51.95%, Patrick: 408, 46.9%, Anthony: 121, 13.91%, Morgan: 63, 7.24%, Paul: 48, 5.52%,   

John Data:  
Messages Sent: 173.0  
Total Likes Given: 369.0  
Self Likes: 3  
Total Likes Received: 362.0  
Average Likes Received Per Message: 2.09248554913  
Total Likes Received with Self Likes Subtracted: 359.0  
Average Likes Received Per Message with Self Likes Subtracted: 2.07514450867  
Total Words Sent: 2018.0  
Likes Received from each member and also what percent of the total likes received is from said member :  
Bob : 96, 26.52%, John : 3, 0.83%, Tim : 24, 6.63%, Philip : 11, 3.04%, Jane : 3, 0.83%, Mary : 107, 29.56%, Patrick : 76, 20.99%, Anthony : 24, 6.63%, Morgan : 8, 2.21%, Paul : 10, 2.76%,   
Percent of each member's total likes that went to John:   
Bob: 11.03%, John: 0.81%, Tim: 7.12%, Philip: 7.53%, Jane: 4.76%, Mary: 8.94%, Patrick: 6.99%, Anthony: 8.36%, Morgan: 6.06%, Paul: 8.13%,  
Number of times you liked the same post as another member and what percent of the posts you liked were liked by that same member:   
Bob: 150, 40.65%, Tim: 83, 22.49%, Philip: 42, 11.38%, Jane: 10, 2.71%, Mary: 250, 67.75%, Patrick: 214, 57.99%, Anthony: 78, 21.14%, Morgan: 52, 14.09%, Paul: 40, 10.84%,   

Tim Data:  
Messages Sent: 208.0  
Total Likes Given: 337.0  
Self Likes: 15  
Total Likes Received: 345.0  
Average Likes Received Per Message: 1.65865384615  
Total Likes Received with Self Likes Subtracted: 330.0  
Average Likes Received Per Message with Self Likes Subtracted: 1.58653846154  
Total Words Sent: 2151.0  
Likes Received from each member and also what percent of the total likes received is from said member :  
Bob : 67, 19.42%, John : 15, 4.35%, Tim : 15, 4.35%, Philip : 9, 2.61%, Jane : 3, 0.87%, Mary : 102, 29.57%, Anthony : 17, 4.93%, Patrick : 83, 24.06%, Morgan : 13, 3.77%, Paul : 21, 6.09%,   
Percent of each member's total likes that went to Tim:   
Bob: 7.7%, John: 4.07%, Tim: 4.45%, Philip: 6.16%, Jane: 4.76%, Mary: 8.52%, Anthony: 5.92%, Patrick: 7.64%, Morgan: 9.85%, Paul: 17.07%,   
Number of times you liked the same post as another member and what percent of the posts you liked were liked by that same member:   
Bob: 130, 38.58%, John: 83, 24.63%, Philip: 50, 14.84%, Jane: 3, 0.89%, Mary: 231, 68.55%, Patrick: 199, 59.05%, Anthony: 59, 17.51%, Morgan: 32, 9.5%, Paul: 40, 11.87%,   

Philip Data:  
Messages Sent: 204.0  
Total Likes Given: 146.0  
Self Likes: 1  
Total Likes Received: 402.0  
Average Likes Received Per Message: 1.97058823529  
Total Likes Received with Self Likes Subtracted: 401.0  
Average Likes Received Per Message with Self Likes Subtracted: 1.96568627451  
Total Words Sent: 2178.0  
Likes Received from each member and also what percent of the total likes received is from said member :  
Bob : 82, 20.4%, John : 20, 4.98%, Tim : 41, 10.2%, Philip : 1, 0.25%, Jane : 6, 1.49%, Mary : 121, 30.1%, Patrick : 85, 21.14%, Anthony : 29, 7.21%, Morgan : 8, 1.99%, Paul : 9, 2.24%,   
Percent of each member's total likes that went to Philip:   
Bob: 9.43%, John: 5.42%, Tim: 12.17%, Philip: 0.68%, Jane: 9.52%, Mary: 10.11%, Patrick: 7.82%, Anthony: 10.1%, Morgan: 6.06%, Paul: 7.32%,  
Number of times you liked the same post as another member and what percent of the posts you liked were liked by that same member:   
Bob: 76, 52.05%, John: 42, 28.77%, Tim: 50, 34.25%, Jane: 4, 2.74%, Mary: 96, 65.75%, Patrick: 96, 65.75%, Anthony: 41, 28.08%, Morgan: 21, 14.38%, Paul: 31, 21.23%,   

GroupMe Data:  
Messages Sent: 10.0  
Total Likes Given: 0.0  
Self Likes: 0  
Total Likes Received: 21.0  
Average Likes Received Per Message: 2.1  
Total Likes Received with Self Likes Subtracted: 21.0  
Average Likes Received Per Message with Self Likes Subtracted: 2.1  
Total Words Sent: 84.0  
Likes Received from each member and also what percent of the total likes received is from said member :  
Bob : 3, 14.29%, John : 2, 9.52%, Tim : 3, 14.29%, Philip : 1, 4.76%, Jane : 1, 4.76%, Mary : 1, 4.76%, Patrick : 5, 23.81%, Anthony : 2, 9.52%, Paul : 3, 14.29%,   
Percent of each member's total likes that went to GroupMe:   
Bob: 0.34%, John: 0.54%, Tim: 0.89%, Philip: 0.68%, Jane: 1.59%, Mary: 0.08%, Patrick: 0.46%, Anthony: 0.7%, Paul: 2.44%, 
Number of times you liked the same post as another member and what percent of the posts you liked were liked by that same member:   


Jane Data:  
Messages Sent: 35.0  
Total Likes Given: 63.0  
Self Likes: 0  
Total Likes Received: 87.0  
Average Likes Received Per Message: 2.48571428571  
Total Likes Received with Self Likes Subtracted: 87.0  
Average Likes Received Per Message with Self Likes Subtracted: 2.48571428571  
Total Words Sent: 326.0  
Likes Received from each member and also what percent of the total likes received is from said member :  
Bob : 28, 32.18%, John : 2, 2.3%, Philip : 1, 1.15%, Mary : 16, 18.39%, Anthony : 5, 5.75%, Patrick : 30, 34.48%, Morgan : 5, 5.75%,   
Percent of each member's total likes that went to Jane:   
Bob: 3.22%, John: 0.54%, Philip: 0.68%, Mary: 1.34%, Anthony: 1.74%, Patrick: 2.76%, Morgan: 3.79%,   
Number of times you liked the same post as another member and what percent of the posts you liked were liked by that same member:   
Bob: 38, 60.32%, John: 10, 15.87%, Tim: 3, 4.76%, Philip: 4, 6.35%, Mary: 34, 53.97%, Patrick: 46, 73.02%, Anthony: 8, 12.7%, Morgan: 3, 4.76%, Paul: 2, 3.17%,   

Mary Data:  
Messages Sent: 243.0  
Total Likes Given: 1197.0  
Self Likes: 4  
Total Likes Received: 442.0  
Average Likes Received Per Message: 1.81893004115  
Total Likes Received with Self Likes Subtracted: 438.0  
Average Likes Received Per Message with Self Likes Subtracted: 1.8024691358  
Total Words Sent: 1968.0  
Likes Received from each member and also what percent of the total likes received is from said member :  
Bob : 131, 29.64%, John : 40, 9.05%, Tim : 43, 9.73%, Philip : 25, 5.66%, Jane : 8, 1.81%, Mary : 4, 0.9%, Patrick : 129, 29.19%, Anthony : 41, 9.28%, Morgan : 17, 3.85%, Paul : 4, 0.9%,  
Percent of each member's total likes that went to Mary:  
Bob: 15.06%, John: 10.84%, Tim: 12.76%, Philip: 17.12%, Jane: 12.7%, Mary: 0.33%, Patrick: 11.87%, Anthony: 14.29%, Morgan: 12.88%, Paul: 3.25%,   
Number of times you liked the same post as another member and what percent of the posts you liked were liked by that same member:   
Bob: 452, 37.76%, John: 250, 20.89%, Tim: 231, 19.3%, Philip: 96, 8.02%, Jane: 34, 2.84%, Patrick: 652, 54.47%, Anthony: 188, 15.71%, Morgan: 90, 7.52%, Paul: 86, 7.18%,   

Anthony Data:  
Messages Sent: 239.0  
Total Likes Given: 287.0  
Self Likes: 4  
Total Likes Received: 454.0  
Average Likes Received Per Message: 1.89958158996  
Total Likes Received with Self Likes Subtracted: 450.0  
Average Likes Received Per Message with Self Likes Subtracted: 1.88284518828  
Total Words Sent: 1578.0  
Likes Received from each member and also what percent of the total likes received is from said member :  
Bob : 109, 24.01%, John : 62, 13.66%, Tim : 26, 5.73%, Philip : 22, 4.85%, Jane : 10, 2.2%, Mary : 100, 22.03%, Patrick : 104, 22.91%, Anthony : 4, 0.88%, Morgan : 9, 1.98%, Paul : 8, 1.76%,   
Percent of each member's total likes that went to Anthony:   
Bob: 12.53%, John: 16.8%, Tim: 7.72%, Philip: 15.07%, Jane: 15.87%, Mary: 8.35%, Patrick: 9.57%, Anthony: 1.39%, Morgan: 6.82%, Paul: 6.5%,   
Number of times you liked the same post as another member and what percent of the posts you liked were liked by that same member:   
Bob: 121, 42.16%, John: 78, 27.18%, Tim: 59, 20.56%, Philip: 41, 14.29%, Jane: 8, 2.79%, Mary: 188, 65.51%, Patrick: 150, 52.26%, Morgan: 29, 10.1%, Paul: 29, 10.1%,   

Patrick Data:  
Messages Sent: 383.0  
Total Likes Given: 1087.0  
Self Likes: 2  
Total Likes Received: 579.0  
Average Likes Received Per Message: 1.51174934726  
Total Likes Received with Self Likes Subtracted: 577.0  
Average Likes Received Per Message with Self Likes Subtracted: 1.50652741514  
Total Words Sent: 4068.0  
Likes Received from each member and also what percent of the total likes received is from said member :  
Bob : 184, 31.78%, John : 42, 7.25%, Tim : 47, 8.12%, Philip : 19, 3.28%, Jane : 8, 1.38%, Mary : 200, 34.54%, Anthony : 51, 8.81%, Patrick : 2, 0.35%, Morgan : 16, 2.76%, Paul : 10, 1.73%,   
Percent of each member's total likes that went to Patrick:   
Bob: 21.15%, John: 11.38%, Tim: 13.95%, Philip: 13.01%, Jane: 12.7%, Mary: 16.71%, Anthony: 17.77%, Patrick: 0.18%, Morgan: 12.12%, Paul: 8.13%,   
Number of times you liked the same post as another member and what percent of the posts you liked were liked by that same member:   
Bob: 408, 37.53%, John: 214, 19.69%, Tim: 199, 18.31%, Philip: 96, 8.83%, Jane: 46, 4.23%, Mary: 652, 59.98%, Anthony: 150, 13.8%, Morgan: 86, 7.91%, Paul: 84, 7.73%,   

Morgan Data:  
Messages Sent: 251.0  
Total Likes Given: 132.0  
Self Likes: 6  
Total Likes Received: 435.0  
Average Likes Received Per Message: 1.73306772908  
Total Likes Received with Self Likes Subtracted: 429.0  
Average Likes Received Per Message with Self Likes Subtracted: 1.70916334661  
Total Words Sent: 2149.0  
Likes Received from each member and also what percent of the total likes received is from said member :  
Bob : 119, 27.36%, John : 18, 4.14%, Tim : 20, 4.6%, Philip : 5, 1.15%, Jane : 4, 0.92%, Mary : 95, 21.84%, Patrick : 135, 31.03%, Anthony : 20, 4.6%, Morgan : 6, 1.38%, Paul : 13, 2.99%,   
Percent of each member's total likes that went to Morgan:   
Bob: 13.68%, John: 4.88%, Tim: 5.93%, Philip: 3.42%, Jane: 6.35%, Mary: 7.94%, Patrick: 12.42%, Anthony: 6.97%, Morgan: 4.55%, Paul: 10.57%,   
Number of times you liked the same post as another member and what percent of the posts you liked were liked by that same member:   
Bob: 63, 47.73%, John: 52, 39.39%, Tim: 32, 24.24%, Philip: 21, 15.91%, Jane: 3, 2.27%, Mary: 90, 68.18%, Patrick: 86, 65.15%, Anthony: 29, 21.97%, Paul: 19, 14.39%,   

Paul Data:  
Messages Sent: 119.0  
Total Likes Given: 123.0  
Self Likes: 11  
Total Likes Received: 302.0  
Average Likes Received Per Message: 2.53781512605  
Total Likes Received with Self Likes Subtracted: 291.0  
Average Likes Received Per Message with Self Likes Subtracted: 2.44537815126  
Total Words Sent: 940.0  
Likes Received from each member and also what percent of the total likes received is from said member :  
Bob : 51, 16.89%, John : 18, 5.96%, Tim : 20, 6.62%, Philip : 23, 7.62%, Jane : 2, 0.66%, Mary : 67, 22.19%, Patrick : 83, 27.48%, Anthony : 12, 3.97%, Morgan : 15, 4.97%, Paul : 11, 3.64%,   
Percent of each member's total likes that went to Paul:   
Bob: 5.86%, John: 4.88%, Tim: 5.93%, Philip: 15.75%, Jane: 3.17%, Mary: 5.6%, Patrick: 7.64%, Anthony: 4.18%, Morgan: 11.36%, Paul: 8.94%,   
Number of times you liked the same post as another member and what percent of the posts you liked were liked by that same member:   
Bob: 48, 39.02%, John: 40, 32.52%, Tim: 40, 32.52%, Philip: 31, 25.2%, Jane: 2, 1.63%, Mary: 86, 69.92%, Patrick: 84, 68.29%, Anthony: 29, 23.58%, Morgan: 19, 15.45%,   
