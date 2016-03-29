import unittest
import datetime
from six.moves.urllib.error import HTTPError
from BreezeClient import Client

test_key = 'YOUR_API_KEY'
lat_lon = (37.7,122.4)
street_address = '5th Avenue, New York'
fake_address = '123 Fake Avenue, Really Fake'

start_date = '2015-10-25T16:00:00'
startime_date = datetime.datetime.strptime(start_date, "%Y-%m-%dT%H:%M:%S" )
end_date = '2015-10-26T16:00:00'
fake_date = '2015-13-26T16:00:00'
bad_date = 2015

class TestClient(unittest.TestCase):

    def test_initialization(self):

        with self.assertRaises(ValueError):
            Client(key = None, location = lat_lon)

        for bad_location in [(1000,1000), None]:
            with self.assertRaises(ValueError):
                Client(key = test_key, location = bad_location)

        with self.assertRaises(ValueError):
            Client(key = test_key, location = lat_lon, language = 'fake_lang')

    def test_current(self):
        for location in [lat_lon, street_address]:
            client = Client(key = test_key, location = location)
            self.assertTrue(client.current()['data_valid'])

        bad_client = Client(key = test_key, location = fake_address)
        with self.assertRaises(HTTPError):
            bad_client.current()

    def test_history(self):
        for location in [lat_lon, street_address]:
            for date in [start_date, startime_date]:
                client = Client(key = test_key, location = location)
                self.assertTrue(client.history(date)['data_valid'])

                history_range = client.history(date, end_datetime = end_date)
                self.assertTrue(all(moment['data_valid'] for moment in history_range))

        client = Client(key = test_key, location = lat_lon)
        with self.assertRaises(HTTPError):
            client.history(fake_date)

        with self.assertRaises(ValueError):
            client.history(bad_date)

        for bad_interval in [100, None, '1']:
            with self.assertRaises(ValueError):
                client.history(start_date, end_datetime = end_date, interval = bad_interval)

if __name__ == '__main__':
    unittest.main()
