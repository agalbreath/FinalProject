import checkBloodSugar
import emergency

def compareBloodSugars(currentBloodSugar, pastBloodSugar):
    global healthyTimer
    global hypoTimer
    global hyperTimer
    pastState = checkBloodSugar.checkBloodSugar(pastBloodSugar)
    currentState = checkBloodSugar.checkBloodSugar(currentBloodSugar)
    if pastState == currentState == 1:
        healthyTimer = 0
        hyperTimer += 10
        print ("Healthy Timer: " + str(healthyTimer))
        print ("Hyper Timer: " + str(hyperTimer))
        print ("Hypo Timer: " + str(hypoTimer))
    elif pastState == currentState == -1:
        healthyTimer = 0
        hypoTimer += 10
        print ("Healthy Timer: " + str(healthyTimer))
        print ("Hyper Timer: " + str(hyperTimer))
        print ("Hypo Timer: " + str(hypoTimer))
    elif


    if checkBloodSugar.checkBloodSugar(currentBloodSugar) == checkBloodSugar.checkBloodSugar(pastBloodSugar) and currentState == 1:
        healthyTimer = 0
        hyperTimer += 10
        print ("Healthy Timer: " + str(healthyTimer))
        print ("Hyper Timer: " + str(hyperTimer))
        print ("Hypo Timer: " + str(hypoTimer))
    elif checkBloodSugar.checkBloodSugar(currentBloodSugar) == checkBloodSugar.checkBloodSugar(pastBloodSugar) and currentState == -1:
        healthyTimer = 0
        hypoTimer += 10
        print ("Healthy Timer: " + str(healthyTimer))
        print ("Hyper Timer: " + str(hyperTimer))
        print ("Hypo Timer: " + str(hypoTimer))
    elif checkBloodSugar.checkBloodSugar(currentBloodSugar) == 0:
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
