# uppgift 1


#uppgift 2
import requests
def get(url):
    r = requests.get(url)
    return r.json()

# man kan importa filen i andra program och sen bara skriva namn.get(www.api.se) för snabbt och smidigt göra en request. 

#uppgift 3

def line(bol=False):
    if bol == True:
        print("**********")
    else:
        print("----------")

def header(title):
    lenght = len(title)
    
    message = ""

    centerValue = 10/lenght

    for a in range(1,int(centerValue)*2+1):
       
        if a == 1:
                message += "|"

        if a == int(centerValue)*2+1:
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




    
