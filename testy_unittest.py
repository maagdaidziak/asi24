import unittest
import json
import requests

import pogoda
from main import powitanie, test2
from register import *

class TestPogoda(unittest.TestCase):
    def setUp(self):
        self.weather_json =  json.loads(requests.get(
    'http://samples.openweathermap.org/data/2.5/weather?q=London,uk&appid=b1b15e88fa797225412429c1c50c122a1').content.strip())
        self.temp = self.weather_json['main']['temp']

    # def sprawdz_temp(self):
    #     self.assertIs(self.weather_json['main']['temp'], 'nie istnieje')


    def test_format_temperatury(self):
        temp = self.temp
        self.assertLess(temp, 1000, "Temp wieksze od 0")

    def test_polaczeni(self):
        r = requests.get('http://samples.openweathermap.org/data/2.5/weather?q=London,uk&appid=b1b15e88fa797225412429c1c50c122a1')
        self.assertEqual(r.status_code, 200, 'brak polaczenia')


    # do bazy danych
    def test_dodania_uzytkownika(self):
        session = return_sqlalchemysession()

        username = 'user'
        password = 'password'
        user = User(username, password)
        session.add(user)
        session.commit()

        q = session.query(User).filter(User.username == username)
        self.assertTrue(session.query(q.exists()).scalar(), 'fail')
        session.close()

 # testy Magdy
    def test_sprawdź_temperaturę(self):
        result = pogoda.konwertuj_do_c(300)
        self.assertEqual(result, "26.85")

    def test_przywitaj(self):
        result = powitanie("Ola")
        self.assertEqual(result, "Witaj Ola")


    def test_test2(self):
        result = test2()
        self.assertEqual(result, "hej hej hej razy ")
