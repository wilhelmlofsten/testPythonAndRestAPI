import requests
import json

from sqlalchemy import false


response = requests.get('https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow')


for data in response.json()['items']:
    if data['answer_count'] ==0  and data['is_answered'] == False:
        print("Title: " + data['title'])
        print("score: ", data['score'])
        print("view_count: ", data['view_count'])
        print("link: " + data['link'])
    else:
        print("not worthy of my time..")
    print("")