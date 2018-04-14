# This function is used to set the acceptable variance from normal ranges. This function defaults to 5 mg/dL
# This will be the first function executed in simulator.py and will generally use the default value.
def setThreshold(thresholdValue):
	if thresholdValue == None:	#If no value is put into the function, go to default.
		threshold = 5;
	else:
		threshold = thresholdValue;	#Otherwise, use the given value.

# This function is used to set the maximum acceptable blood sugar level, in mg/dL

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
	if danger == None: #If the user has gone for 2 straight hours with a healthy blood sugar range.
		print("Healthy levels have been maintained consistently. \n Simulation complete. Have a nice day!")
		running = False
	else:
		print("User is in danger from ")
		print (danger)
		urgent = input(". Contacting emergency contacts . . . \n Contacts reached. Call 911?")
		if urgent == "yes" or urgent == "Yes" or urgent == "YES":
			print("911 has been called. Please wait while the ambulance is dispatched to your location.")
			print("\n \n Simulation complete. Have a nice day!")
			running = False
		else:
			print("Simulation complete. Have a nice day!")
			running = False

#def compareBloodSugars(currentBloodSugar, pastBloodSugar):
