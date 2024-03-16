from geopy.geocoders import Nominatim
from geopy.distance import distance

geolocator = Nominatim(user_agent="geoapiExercises")


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
            return location.raw['address']
        except:
            continue             
    return None

def get_city(lat: float, long: float) -> str:
    coord = f'{lat}, {long}'
    adress = get_address(coord)
    city = adress.get("city")
    if city is not None:
        return city
    state = adress.get("state", "")
    if state is not None:
        return state
    return None
