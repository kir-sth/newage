from config_reader import config
from geopy.geocoders import Yandex
from geopy.distance import distance


geolocator = Yandex(api_key=config.geo_token.get_secret_value())


def get_years_old(age: int) -> str:
    if 10 <= age <= 20:
        return "лет"
    last_digit = str(age)[-1]
    if int(last_digit) == 1:
        years_old = "год"
    elif 2 <= int(last_digit) <= 4:
        years_old = "года"
    else:
        years_old = "лет"
    return years_old

def get_address(coord, retries=5):
    for i in range(retries):
        try:
            location = geolocator.reverse(coord, exactly_one=True)
            components = location.raw["metaDataProperty"]["GeocoderMetaData"]["Address"]["Components"]
            return {component["kind"]: component["name"] for component in components}
        except:
            continue             
    return None

def get_city(lat: float, long: float) -> str:
    coord = f'{lat}, {long}'
    adress = get_address(coord)
    city = adress.get("locality")
    if city is not None:
        return city
    state = adress.get("province")
    if state is not None:
        return state
    return None
