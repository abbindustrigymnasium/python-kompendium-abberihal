# uppgift 1

omvandlings_tal = input("Vad vill du om vandla ")

def miles_to_km(miles):
    return miles*1.60934


def km_to_miles(km):
    return km*0.62137119223733



if "km" in omvandlings_tal: # kollar om km finns i inputen. 
    print(omvandlings_tal +" är " + str(km_to_miles(int(omvandlings_tal[0:len(omvandlings_tal)-2]))) + " miles") # jag slicar bort km eller miles sen gör jag numret till ett nummer för att sedan skicka in i funktionen. 

elif "miles" in omvandlings_tal:
    print(omvandlings_tal+" är "+str(miles_to_km(int(omvandlings_tal[0:len(omvandlings_tal)-5]))) + " km")
else:
    print("testa igen")




#uppgift 2
import requests
def get(url):
    r = requests.get(url)
    return r.json()

# # man kan importa filen i andra program och sen bara skriva namn.get(www.api.se) för snabbt och smidigt göra en request. 

# #uppgift 3

def line(bol=False):
    if bol == True:
        print("**********")
    else:
        print("----------")

def header(title):
    lenght = len(title)
    
    message = ""

    centerValue = 10/lenght 

    for a in range(1,int(centerValue)*2+1): # centervalue är hur mycket som blir på sidorna dräför tar vi det x2.          
       
        if a == 1: # när vi är i början sätt ut ett |
                message += "|"

        if a == int(centerValue)*2+1: # i slutet sätt ut ett |
            message += "|"

        message += " "

        if a == int(centerValue):
            message += title

    print (message)

def echo(text):
    print("|",text)

def prompt(text):
    return input(text)

def clear():
    for x in range(0,15):
        print("\n")




    
