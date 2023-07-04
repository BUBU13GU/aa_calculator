import requests
import json

state = True
while state == True:
    option = int(input("\nWelcome to the AA Calculator\
                    \nPlease select one of the following options: \
                    \n1. Have a look at the previous entry.\
                    \n2. Make a new entry.\
                    \n3. Close the program.\
                    \n: "))

    if option == 1:
        jsonFile = open("data.json", "r")
        data = json.load(jsonFile)
        print(f"\n{data}")

        jsonFile.close
        
    elif option == 2:
        meter_distance = float(input("\nHow mmany meters have you traveled: "))
        kilometer_distance = meter_distance / 1000

        vehicles = int(input("\nHere is the list of vehicles, please select one: \
                            \n1. Hatchback\
                            \n2. SUV\
                            \n3. Sports Car\
                            \n: "))

        if vehicles > 0 and vehicles <= 3:
            AA_Calc = 'https://raw.githubusercontent.com/tyrone0501/AA-Petrol-Price/main/Cars.json'
            response = requests.get(AA_Calc)  
            response_json = response.json()

            siteresponse = response_json["Hatchback"]
            siteresponse = response_json["SUV"]
            siteresponse = response_json["SportsCar"]
            
            travel_cost = siteresponse * kilometer_distance
            description = input("\nPlease type in your description of where you traveled and why: ")
            jsonString = json.dumps(f"Cost: {travel_cost}, KM: {kilometer_distance}, Description: {description} ")
            jsonFile = open("data.json", "w")
            jsonFile.write(jsonString)
            jsonFile.close()  
        else:
            print("Invalid Input")
        
    elif option == 3:
        break 

    else:
        print("\nInvalid Output")