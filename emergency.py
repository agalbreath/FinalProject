def emergency(state):
    global running
    if state == 0:
        print("Healthy levels have been maintained consistently. \n Simulation complete. Have a nice day!")
        running = False
    elif state == 1:
        warning("hyperglycemia")
    elif state == -1:
        warning("hypoglycemia")
    else:
        warning("labile glucose levels")

def warning(danger):
    print("User is in danger from " + danger + ". Contacting emergency contacts. . .")
    urgent = input("Contacts reached. Call 911? ")
    if urgent == "yes" or urgent == "Yes" or urgent == "YES":
        print("911 has been called. Please wait while the ambulance is dispatched to your location.")
        print("\n \n Simulation complete. Have a nice day!")
        running = False
    else:
        print("Simulation complete. Have a nice day!")
        running = False
