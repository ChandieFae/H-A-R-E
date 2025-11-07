from geopy.distance import distance

def calculate_radius_km(mph: int, minutes_elapsed: int) -> float:
    hours = minutes_elapsed / 60
    miles = mph * hours
    km = miles * 1.60934
    return round(km, 2)
