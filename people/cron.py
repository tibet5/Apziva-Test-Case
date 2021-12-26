import requests
from .models import Login_list, Last_url_of_users
import time



def scheduled_request():
    last_url = Last_url_of_users.objects.last()
    res = requests.get(last_url)
    link = res.headers.get('link', None)
    links = link.split(',')
    login_list = []
    for link in links:
        if 'rel="next"' in link:
            update_url = Last_url_of_users(user_url_last=link[link.find("<")+1:link.find(">")])
            update_url.save()
    login_list = []
    res = res.json()
    for x in res:
        login_list.append(x['login'])

    for user in login_list:
        print("user from cron")
        print(user)
        q = Login_list(login_id=user)
        q.save()
        time.sleep(0.5)
    print('cron ended')