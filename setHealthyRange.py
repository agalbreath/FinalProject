def setHealthyRange(eating):
    global maxSafeLevel
    global minSafeLevel
    if eating == True:
        maxSafeLevel = 180
    else:
        maxSafeLevel = 130
    minSafeLevel = 80
