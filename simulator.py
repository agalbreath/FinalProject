import cgmSimulator

cgmSimulator.setThreshold(5)
cgmSimulator.running = True
print ("Welcome to CGM Simulator!")
print ("This simulator is used to demonstrate the functionality of Bluetooth-enabled Constant Glucose Monitors to automatically alert emergency contacts in case of emergency.")
print ("During this simulator, you will be asked to input your blood sugar periodically.")
print ("This will be counted as your blood sugar for the next ten minutes.")
print ("If you can go for 2 hours with a healthy blood sugar range, the simulation will end.")
print ("If it remains above or below healthy ranges for 1 hour, your emergency contacts will be notified.")
print ("You may also be asked to answer yes or no questions. Please type your answers as 'yes' or 'no'.")
eating = input ("First thing's first: Has it been less than two hours since your last meal? ")
if eating == "yes" or eating == "Yes" or eating == "YES":
    cgmSimulator.setHealthyRange(True)
    cgmSimulator.currentBloodSugar = 150
    cgmSimulator.pastBloodSugar = 150
    print ("Maximum healthy blood sugar is 180 mg/dL. Current blood sugar is 150 mg/dL.")
elif eating == 'no' or eating == 'No' or eating == 'NO':
    cgmSimulator.setHealthyRange(False)
    cgmSimulator.currentBloodSugar = 105
    cgmSimulator.pastBloodSugar = 150
    print ("Maximum healthy blood sugar is 130 mg/dL. Current blood sugar is 105 mg/dL.")
else:
    print ("Well how is that possible? Is something wrong?")
    print ("Error. Simulation ending.")
    cgmSimulator.running = False
while cgmSimulator.running == True:
    cgmSimulator.currentBloodSugar = int(input("Please enter your current blood sugar: "))
    cgmSimulator.checkBloodSugar(cgmSimulator.currentBloodSugar)
    cgmSimulator.compareBloodSugars(cgmSimulator.currentBloodSugar, cgmSimulator.pastBloodSugar)
