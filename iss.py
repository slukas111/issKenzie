#!/usr/bin/env python
__author__ = 'Sasha Lukas'


import requests
import turtle
import time

base_url = 'http://api.open-notify.org/astros.json'
iss_icon = 'iss.gif'
world_map = 'map.gif'
cur_url = 'http://api.open-notify.org/iss-now.json'

def get_astro():
    astro = requests.get(base_url)
    astro = astro.json()
    # print("Astronauts: ")
    for person in astro["people"]:
        print("  {} is currently on the {}.".format(
            person["name"], person["craft"]))
    print("There are {} people on the ISS station.".format(
        len(astro['people'])))

def get_iss_coordinates():
    pos = requests.get(cur_url)
    pos = pos.json()
    long_ = pos[u"iss_position"][u"longitude"]
    lat_ = pos[u"iss_position"][u"latitude"]
    print(" ")
    print("The ISS is at longitude {} and latitude {} as of {}.".format(
        long_, lat_, time.ctime(pos[u"timestamp"])))
    return [float(long_), float(lat_)]


def draw_iss(coords):
    """Draws the ISS on the map where it is on program run
    and also the dot over Indy with the next time the ISS will
    be over Indy."""
    screen = turtle.Screen()
    screen.register_shape(iss_icon)
    screen.setup(width=720, height=360)
    screen.setworldcoordinates(-180, -90, 180, 90)

    iss = turtle.Turtle()
    iss.shape(iss_icon)
    iss.screen.bgpic(world_map)
    iss.screen.title("ISS locator")
    iss.penup()
    iss.goto(coords[0], coords[1])
    iss.pendown()
    iss_over_indy(screen)

    if screen is not None:
        print('Click on screen to exit ...')
        screen.exitonclick()

def iss_over_indy(screen):
    """DOT over Indy with the date and time the ISS will
    pass over Indy"""
    pass_api = "http://api.open-notify.org/iss-pass.json?"
    indy_lat = 39.768403
    indy_long= -86.1210
    coords = requests.get("{}lat={}&lon={}".format(
        pass_api, indy_lat, indy_long))
    coords = coords.json()

    passover_time = time.ctime(coords[u'response'][0]["risetime"])
    position = turtle.Turtle()
    position.color('yellow')
    position.penup()
    position.goto(indy_long, indy_lat)
    position.pendown()
    position.write(passover_time, align=("left"), font=(30))
    position.penup()
    position.dot(5)

def main():
    get_astro()
    pos = get_iss_coordinates()
    draw_iss(pos)


if __name__ == '__main__':
    main()