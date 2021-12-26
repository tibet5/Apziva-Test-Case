## Easy Reacruiter
<hr>

What this app does?

This app is live at http://tibethomeserver.cloudns.ph:8000/

Fetches the username from https://api.github.com/users and saves the usernames to Login_list model one by one.

And when a Login_list object saved it's invokes the makeRecord function wich is in the signals.py. 

When the makeRecord starts to run it gets the latest saved Login_list object and makes a call to the https://api.github.com/users/{user}. if developer or engineer keywords in the response['bio'],  it creates a people object with the fetched information.

&nbsp;
### Home
<hr>
List display of all the users, 50 by page

&nbsp;
### Search
<hr>
Listens the search box for keyup event and get data from People object's bio by using ajax method.

At first when i planned to use ajax i just had 50 people on app so it worked smoothly but now it has 950 people (i checked while i wrote this) and it's not working wery well you can tell why...


But you can copy paste the word or words that you lookin for and it works smootly that way

&nbsp;

#### How to improve
<hr>

- Get the Login_list object from signal while making record not from db
- Use an enviroment variable to store the last user list link not use db  
##### Home
- Last or newest record sorting
- A title maybe...
##### Search
- Not use ajax
- Check box sorting by location and hireable


&nbsp;
#### What i learned
<hr>

- Django Signals
- Cron Jobs

&nbsp;

I learned Django Signals one day before deadline till that day i thought this app is gonna blow because i was making the records in a child process and that was not working well

I knew the cron jobs theoretically but never used before

I deployed this app to my home server because of the cron jobs

