import setHealthyRange
import emergency

def checkBloodSugar(currentBloodSugar):
    global currentState
    if currentBloodSugar - 5 > setHealthyRange.maxSafeLevel:
        currentState = 1
    elif currentBloodSugar + 5 < setHealthyRange.minSafeLevel:
        currentState = -1
    else:
        currentState = 0

def advanceTimer(currentState):
    global healthyTimer
    global hyperTimer
    global hypoTimer
    if currentState == 0:
        healthyTimer = healthyTimer + 10
        hyperTimer = 0
        hypoTimer = 0
    elif currentState == 1:
        healthyTimer = 0
        hyperTimer = hyperTimer + 10
    else:
        healthyTimer = 0
        hypoTimer = hypoTimer + 10
    if hyperTimer != 0 and hypoTimer != 0:
        emergency.emergency(3)
    if healthyTimer > 60 or hyperTimer > 60 or hypoTimer > 60:
        emergency.emergency(currentState)
