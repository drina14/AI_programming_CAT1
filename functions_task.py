from math import pi

def area_of_circle(radius):
    if radius <= 0:
        return "Radius must be greater than 0"
    area = pi * (radius ** 2)
    return round(area, 2)
