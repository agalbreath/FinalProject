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