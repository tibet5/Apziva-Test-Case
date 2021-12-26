from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Login_list, People
import requests, re


@receiver(post_save, sender=Login_list)
def makeRecord(sender, **kwargs):
    user = Login_list.objects.last()
    print("last recorded human")
    print(user)
    q = f'https://api.github.com/users/{user}' 
    res = requests.get(q, auth=('xxxx','xxxxxxxxxxxxx'))
    res = res.json()
    if not People.objects.filter(login = res['login']):
        try:
            if re.search("[Dd]+eveloper|[Ee]+ngineer", res['bio']):
                print('yes added to db')
                obj = People(
                    login = res['login'],
                    name = res['name'],
                    e_mail = res['email'],
                    bio = res['bio'],
                    location = res['location'],
                    user_url = res['html_url'],
                    avatar_url = res['avatar_url'],
                    hireable = res['hireable']
                )
                print(obj)
                obj.save()
                print()
            else:
                print('no doesnt have re')
        except:TypeError()
    else: print('user exists')
