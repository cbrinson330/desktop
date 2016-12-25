from nanpy import (Servo, Arduino)
from pprint import pprint
import requests, json

#Holders
oldTemp = 0

def getAPIData():
	url = 'http://api.wunderground.com/api/a1bc55c4ddd1b3f0/conditions/q/DE/Mainz.json'
	response = requests.get(url)
	data = json.loads(response.text)
	
	curTemperature = data['current_observation']['temp_c']
	conditions = data['current_observation']['icon']

	return curTemperature, conditions

def setWeatherServo(cond):
	#weatherServo
	servoObj = Servo(4)
	degToTurn = 0;

	if cond == 'chanceflurries' or cond == 'chancesnow' or cond == 'flurries' or cond == 'snow':
		#is snow icon 
		degToTurn = 30

	if cond == 'chancesleet' or cond == 'sleet':
		#is sleet icon 
		degToTurn = 90 

	if cond == 'chancestorms' or cond == 'tstorms':
		#is storm icon 
		degToTurn = 150

	if cond == 'clear' or cond == 'sunny':
		#is sun icon 
		degToTurn = 210
	
	if cond == 'fog' or cond == 'hazy' or cond == 'cloudy':
		#is cloudy icon 
		degToTurn = 270
	
	if cond == 'mostlycloudy' or cond == 'mostlysunny' or cond == 'partlycloudy' or cond == 'patlysunny':
		#is partSunPartCloud icon 
		degToTurn = 330
	
	#servoObj.write(degToTurn)
	print(degToTurn)
	
def curTemp(newTemp):
	#TODO set gears tos show current temp
	#store temp in var
	oldTemp = newTemp

if __name__ == "__main__":
	curTemp, conditionsOutput = getAPIData()
	setWeatherServo(conditionsOutput)
	setTempGear(curTemp)
