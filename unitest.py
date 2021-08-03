import unittest
import urllib.request
import json

class TestApiSomEnergia(unittest.TestCase):

    def test_http(self):
        """ Verifiquem connexió
        Controlem que la crida HTTP a la API funciona correctament
        """
        url = 'https://opendata.somenergia.coop/v0.2/members/by/city/monthly/from/2019-01-01/to/2021-08-01?city=17010'
        httpcode = urllib.request.urlopen(url).getcode()
        if httpcode == 200:
            print('API 200 OK')
        else:
            exit()

    def test_estructura(self):
        """ Verifiquem l'estructura
        Controlem que la crida HTTP retorna l'estructura esperada
        """
        with urllib.request.urlopen("https://opendata.somenergia.coop/v0.2/members/by/city/monthly/from/2019-01-01/to/2021-08-01?city=17010&format=json") as url:
            data = json.loads(url.read().decode())
        data['city']

if __name__ == '__main__':
    unittest.main()