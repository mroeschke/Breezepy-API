import datetime
import json
from six.moves.urllib import request, parse
from utils import *

class Client(object):
    "Client to access Breezometer API"

    def __init__(self, key = None, location = None, language = 'en'):
        """
        Input
        -----
        key: API key from Breezometer
        location: geographical location to retreive data. Use latitude & longitude for best results
            Format
            ------
            1) latitude & longitude in WGS84 standard as a tuple e.g (40.7,-74.0)
            2) street address & city  e.g. '5th Avenue New York'
        language: language of return results. 'en' - english (default), 'he' - hebrew
        """
        if not key:
            raise ValueError('Please provide API key.')

        self.key = key

        if not location:
            raise ValueError('Please provide location.')

        elif not valid_location(location):
            raise ValueError('Invalid Location.')

        if isinstance(location, tuple):
            self.lat = location[0]
            self.lon = location[1]
        else:
            self.location = format_location(location)

        if language not in ['en', 'he']:
            raise ValueError('Invalid Language. Only English ("en") and Hebrew ("he") are supported.')

        self.language = language

    def current(self):
        """
        Retreives current air quality information as JSON
        """
        query = parse.urlencode(self.__dict__)
        current = request.urlopen('https://api.breezometer.com/baqi/?' + query)
        return json.loads(current.read())

    def history(self, start_datetime, end_datetime = None, interval = 1):
        """
        Retreives historical air quality information as JSON for 'start_datetime'

        Returns air quality measurements for a time frame if 'end_datetime' is specified

        Time format follows ISO 8601: YYYY-MM-DDTHH:mm:SS
        Where
        Y = Year
        M = Month
        D = day
        H = hour
        m = minute
        S = second

        Input
        -----
        start_datetime: start of timeframe or particular day to return historical measurements as string or datetime
        end_datetime: end of timeframe as string or datetime
        interval: time interval in hours between measurements. Specify when providing end_datetime.
                  Integer value between 1-24, default 1.

        """
        params = self.__dict__
        if not valid_time(start_datetime):
            raise ValueError('start_datetime must be a string in ISO 8601 format or datetime object')

        if end_datetime:
            if not valid_time(end_datetime):
                raise ValueError('end_date must be a string in ISO 8601 format or datetime object')

            if not valid_interval(interval):
                raise ValueError('interval must be an integer between 1 and 24')

            params['start_datetime'] = format_date(start_datetime)
            params['end_datetime'] = format_date(end_datetime)
            params['interval'] = interval
        else:
            params['datetime'] = format_date(start_datetime)

        query = parse.urlencode(params)
        current = request.urlopen('https://api.breezometer.com/baqi/?' + query)
        return json.loads(current.read())
