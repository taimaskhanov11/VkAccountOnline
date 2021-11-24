import ipinfo
from pyowm import OWM
import logging
logger = logging.getLogger('controller')
from VkAccountOnline.celery import app

ip_token = 'd232f4da3eed53'
owm = OWM('93b59f65175591d626458dbb91a01f5a')
mgr = owm.weather_manager()


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def get_place(ip_address):
    handler = ipinfo.getHandler(ip_token)
    details = handler.getDetails(ip_address)
    # print(details.city)
    # print(details.country)
    # return f'{details.city},{details.country}'
    return str(details.city), str(details.country)


def get_weather(place):
    observation = mgr.weather_at_place(place)
    w = observation.weather
    return w

@app.task
def get_weather_bar(request):
    ip_address = get_client_ip(request)
    try:
        city, country = get_place(ip_address)
    except AttributeError as e:
        print(e)
        logger.info(e)
        city, country = 'Moscow','Russia'
    weather = get_weather(f'{city},{country}')
    return {
        'temperature': weather.temperature('celsius')['temp'],
        'city': city,
        'country': country,
    }


if __name__ == '__main__':
    pass
