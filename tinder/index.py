from sense_hat import SenseHat
# for api and data
import requests
import json
import sys

sense = SenseHat()

# var
profileName = ""
profileAge = 0
profileLocation = ""


def loadOldData():
    with open('data.json') as json_data:
    oldData = json.load(json_data)
    return oldData


def likeProfile():
    global profileName
    global profileAge
    global profileLocation

    newProfile = {'name': profileName, 'age': profileAge,
                  'location': profileLocation, 'rate': 'like'}

    # update data.json
    with open('data.json', "a") as json_file:
        json_file.write("{}\n".format(json.dumps(newProfile)))


def dislikeProfile():
    global profileName
    global profileAge
    global profileLocation

    newProfile = {'name': profileName, 'age': profileAge,
                  'location': profileLocation, 'rate': 'dislike'}

    # update data.json
    with open('data.json', "a") as json_file:
        json_file.write("{}\n".format(json.dumps(newProfile)))


def getProfile():
    global profileName
    global profileAge
    global profileLocation

    profileData = requests.get("https://randomuser.me/api/").json()
    profileName = profileData['results'][0]['name']['first']
    profileAge = profileData['results'][0]['dob']['age']
    profileLocation = profileData['results'][0]['location']['city']

    sense.stick.direction_right = likeProfile
    sense.stick.direction_left = dislikeProfile


def printProfileInfo():
    global profileName
    global profileAge
    global profileLocation
    # start color green of per profile
    c_text = (0, 200, 25)
    sense.show_message(profileName, text_colour=c_text)
    sense.show_message(str(profileAge))
    sense.show_message(profileLocation)


try:
    while True:
    getProfile()
    printProfileInfo()
except (KeyboardInterrupt, SystemExit):
    print('Exit Program')
    sense.clear()
    sys.exit(0)
