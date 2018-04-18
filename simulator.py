import checkBloodSugar
import emergency
import setHealthyRange

checkBloodSugar.healthyTimer = 0
checkBloodSugar.hyperTimer = 0
checkBloodSugar.hypoTimer = 0
print ("Welcome to CGM Simulator!")
print ("This simulator is used to demonstrate the functionality of Bluetooth-enabled Constant Glucose Monitors to automatically alert emergency contacts in case of emergency.")
print ("During this simulator, you will be asked to input your blood sugar periodically.")
print ("This will be counted as your blood sugar for the next ten minutes.")
print ("If you can go for 2 hours with a healthy blood sugar range, the simulation will end.")
print ("If it remains above or below healthy ranges for 1 hour, your emergency contacts will be notified.")
print ("You may also be asked to answer yes or no questions. Please type your answers as 'yes' or 'no'.")
eating = input ("First thing's first: Has it been less than two hours since your last meal? ")
if eating == "yes" or "Yes" or "YES" or "y":
    setHealthyRange.setHealthyRange(True)
    print ("Maximum healthy blood sugar is 180 mg/dL.")
    print ("Minimum healthy blood sugar is 80 mg/dL.")
    emergency.running = True
elif eating == "no" or "No" or "NO" or "n":
    setHealthyRange.setHealthyRange(False)
    print ("Maximum healthy blood sugar is 130 mg/dL")
    print ("Minimum healthy blood sugar is 80 mg/dL.")
    emergency.running = True
else:
    print ("How is that possible? Is something wrong?")
    print ("Error, simulation ending.")
    emergency.running = False

while emergency.running == True:
    currentBloodSugar = int(input ("Please enter your current blood sugar: "))
    state = checkBloodSugar.checkBloodSugar(currentBloodSugar)
    checkBloodSugar.advanceTimer(state)
