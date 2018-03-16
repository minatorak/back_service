import uuid

import requests
from bs4 import BeautifulSoup

from common.database import Database


class Crawlerdisease(object):
    url = "https://medthai.com/%E0%B8%A3%E0%B8%B2%E0%B8%A2%E0%B8%8A%E0%B8%B7%E0%B9%88%E0%B8%AD%E0%B9%82%E0%B8%A3%E0%B8%84"

    # ชื่อ สาเหตุ อาการ การรักษา การป้องกัน
    def __init__(self, name,url,_id = None):
        self.url = url
        self.name = name
        self._id = uuid.uuid4().hex if _id is None else _id

    def json(self):
        return {
            'url':self.url,
            'name': self.name,
            '_id': self._id
        }

    def save_mongo(self):
        Database.insert(collection="disease",
                        data=self.json())

    @classmethod
    def from_mongo(cls):
        return [disease for disease in Database.find_all('disease')]

    @staticmethod
    def re_data(data):
        return {
            'url': data['url'],
            'name': data['name'],
        }

    @staticmethod
    def new_disease(name, url):
        disease = Crawlerdisease(name,url)
        disease.save_mongo()

    @staticmethod
    def get_data():
        req = requests.get(Crawlerdisease.url)
        soup = BeautifulSoup(req.content, 'html.parser')

        listname = soup.find('div', class_='letter-section',id='โรคติดต่อ')
        listnames = listname.find_all('li')
        for i in range(len(listnames)):
            try:
                name = listnames[i].a['href']
                Crawlerdisease.new_disease(name=name,
                                           url=Crawlerdisease.url+name)
            except:
                print('error')

        listname = soup.find('div', class_='letter-section',id='โรคพบบ่อย')
        listnames = listname.find_all('li')
        for i in range(len(listnames)):
            try:
                name = listnames[i].a['href']
                Crawlerdisease.new_disease(name=name,
                                           url=Crawlerdisease.url + name)
            except:
                print('error')

        listname = soup.find('div', class_='letter-section',id='อ่านมากที่สุด')
        listnames = listname.find_all('li')
        for i in range(len(listnames)):
            try:
                name = listnames[i].a['href']
                Crawlerdisease.new_disease(name=name,
                                           url=Crawlerdisease.url + name)
            except:
                print('error')


