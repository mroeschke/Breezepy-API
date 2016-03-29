import datetime

def is_valid_lat_lon(location):
    if len(location) != 2:
        return False
    try:
        return -90 <= float(location[0]) <= 90 and -180 <= float(location[1]) <= 180
    except ValueError:
        return False

def valid_location(location):
    if isinstance(location, tuple):
        return is_valid_lat_lon(location)
    return isinstance(location, str)

def valid_interval(interval):
    if isinstance(interval, int):
        return interval in range(1,25)
    return False

def format_location(location):
    location = location.replace(',','').replace('.','')
    return '+'.join(loc.lower() for loc in location.split())

def valid_time(time):
    return isinstance(time, datetime.datetime) or isinstance(time, str)

def format_date(time):
    if isinstance(time, datetime.datetime):
        return time.isoformat()
    return time
