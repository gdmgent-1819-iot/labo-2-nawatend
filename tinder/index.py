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

    profileName = profileData['results'][0]['name']['first'];##imports
from sense_hat import SenseHat
##for api and data
import requests
import json
import sys

sense = SenseHat()

#var 
profileName = ""
profileAge = 0
profileLocation = "" 
  
def getProfile():
    global profileName
    global profileAge
    global profileLocation
    profileData = requests.get("https://randomuser.me/api/").json()
    profileName = profileData.results[0].name.first + profileData.results[0].name.last
    profileAge = profileData['results'][0]['gender']
    profileLocation = profileData['results'][0]['location']['city']
    print("globally:", profileName)

def printProfileInfo():
    global profileName
    global profileAge
    global profileLocation
  
    sense.show_message(profileName)
    sense.show_message(profileAge)
    sense.show_message(profileLocation)

getProfile()
# sense.stick.direction_left = like
# sense.stick.direction_right = dislike