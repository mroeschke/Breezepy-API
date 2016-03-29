# Breezometer-API
Python Wrapper around Breezometer API.

Here's a basic example of how to use the API:

    from BreezeClient import Client

    client = Client(key = 'YOUR_API_KEY', location = '5th Avenue, New York')

    #Get Current Conditions
    current_conditions = client.current()

    #Get Historical Conditions
    historical_conditions = client.history('2015-10-25T16:00:00')

    #Get Historial Contitions over a time period
    historical_period = client.history('2015-10-25T16:00:00', end_datetime = '2015-10-26T16:00:00')

This project is not affiliated with Breezometer and is still a work in progress. Please refer to [the API documentation](https://breezometer.com/api/) for more information.
