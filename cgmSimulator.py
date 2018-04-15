# This function is used to set the acceptable variance from normal ranges. This function defaults to 5 mg/dL
# This will be the first function executed in simulator.py and will generally use the default value.
def setThreshold(thresholdValue):
    global threshold
    threshold = thresholdValue;	#Otherwise, use the given value.


# This function is used to set the maximum acceptable blood sugar level, in mg/dL
# If the patient has gone for more than 2 hours without eating, the maximum blood sugar is lower.
def setHealthyRange(eating):
    global maxSafeLevel
    global minSafeLevel
    if eating == True:
        maxSafeLevel = 180;
    else:
        maxSafeLevel = 130;
    minSafeLevel = 80;

def checkBloodSugar(currentBloodSugar):
    global currentState
    if currentBloodSugar - 5 > maxSafeLevel:
        currentState = 1
    elif currentBloodSugar + 5 < minSafeLevel:
        currentState = -1
    else:
        currentState = 0

def emergency(state):
    global running
    running = True
    if state == 1:
        danger = "hyperglycemia"
    elif state == -1:
        danger = "hypoglycemia"
    elif state == 3:
        danger = "labile glycemic levels"
    else:
        danger = None
    if danger == None:
        print("Healthy levels have been maintained consistently. \n Simulation complete. Have a nice day!")
        running = False
    else:
        print("User is in danger from " + danger + ". Contacting emergency contacts. . .")
        urgent = input("Contacts reached. Call 911? ")
        if urgent == "yes" or urgent == "Yes" or urgent == "YES":
            print("911 has been called. Please wait while the ambulance is dispatched to your location.")
            print("\n \n Simulation complete. Have a nice day!")
            running = False
        else:
            print("Simulation complete. Have a nice day!")
            running = False

def compareBloodSugars(setCurrentBloodSugar):
    global currentBloodSugar
    global pastBloodSugar
    global healthyTimer
    global hypoTimer
    global hyperTimer
    currentBloodSugar = currentBloodSugar
    if checkBloodSugar(currentBloodSugar) == checkBloodSugar(pastBloodSugar) and currentState == 1:
        healthyTimer = 0
        hyperTimer += 10
        print ("Healthy Timer: " + str(healthyTimer))
        print ("Hyper Timer: " + str(hyperTimer))
        print ("Hypo Timer: " + str(hypoTimer))
    elif checkBloodSugar(currentBloodSugar) == checkBloodSugar(pastBloodSugar) and currentState == -1:
        healthyTimer = 0
        hypoTimer += 10
        print ("Healthy Timer: " + str(healthyTimer))
        print ("Hyper Timer: " + str(hyperTimer))
        print ("Hypo Timer: " + str(hypoTimer))
    elif checkBloodSugar(currentBloodSugar) == 0:
        hyperTimer = 0
        hypoTimer = 0
        healthyTimer += 10
        print ("Healthy Timer: " + str(healthyTimer))
        print ("Hyper Timer: " + str(hyperTimer))
        print ("Hypo Timer: " + str(hypoTimer))
    if hypoTimer != 0 and hyperTimer != 0:
        emergency(3)
    elif hyperTimer >= 60 or healthyTimer >= 60 or hypoTimer >= 60:
        emergency(currentState)
    pastBloodSugar = currentBloodSugar
