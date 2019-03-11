##imports
from sense_hat import SenseHat
##for api and data
import requests
import json

sense = SenseHat()


def getProfile():
    profileData = requests.get('https://randomuser.me/api').json()

    global profileName
    global profileAge
    global profileLocation

    profileName = profileData['results'][0]['name']['first'];
