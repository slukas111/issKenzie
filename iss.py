#!/usr/bin/env python
import requests

__author__ = 'Sasha Lukas'

"""global scopes for project creating variable for json file"""
url = 'http://api.open-notifty.org'
icon = 'iss.gif'
world_map ='map.gif'

def get_astronauts():
    astronauts = requests.get(url + '/astros.json')
    astronauts.raise_for_status()

    for person in astronauts["people"]:
        print("  {} is currently on the {}.".format(
            person["name"], person["craft"]))
    print("There are {} people on the ISS right now.".format(
        len(astronauts["people"])))
    return astronauts.json()['people']


def main():
    pass


if __name__ == '__main__':
    main()
