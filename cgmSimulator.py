def setThreshold(thresholdValue):
	if thresholdValue = None:
		threshold = 5;
	else: 
		threshold = thresholdValue;

def setHealthyRange(eating):
	if eating:
		maxSafeLevel = 180;
	else:
		maxSafeLevel = 130;
	minSafeLevel = 80;
	
def checkBloodSugar(currentBloodSugar):
	if currentBloodSugar - 5 > maxSafeLevel:
		currentState = 1
	elif currentBloodSugar + 5 < minSafeLevel:
		currentState = -1
	else:
		currentState = 0

def emergency(state):
	if state == 1:
		danger = "hyperglycemia"
	elif state == 2:
		danger = "hypoglycemia"
	elif state == 3:
		danger = "labile glycemic levels"
	else:
		danger = None
	if danger = None: #If the user has gone for 2 straight hours with a healthy blood sugar range.
		print("Healthy levels have been maintained consistently. \n Simulation complete. Have a nice day!")
	else:
		print(User is in danger from ")
		print danger
		urgent = input(". Contacting emergency contacts . . . \n Contacts reached. Call 911?)
		if urgent == 1:
			print("911 has been called. Please wait while the ambulance is dispatched to your location.")
			print("\n \n Simulation complete. Have a nice day!")
		else:
			print("Simulation complete. Have a nice day!")