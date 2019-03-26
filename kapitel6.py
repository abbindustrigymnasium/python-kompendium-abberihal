import requests



# uppgift 6.1
# 
# uppgift 6.2

city = input("Skriv en stad du vill ha väderprognos för ->")

url2 = 'https://54qhf521ze.execute-api.eu-north-1.amazonaws.com/weather/'+city

r2 = requests.get(url2) 

weather_dictonary = r2.json()

if "error" in weather_dictonary:
    print(weather_dictonary['error'])
else:
    print('Väderprognos för', weather_dictonary['city'])

    hej= ''

    for i in weather_dictonary["forecasts"]:
        hej += i["date"] + ": " + i["forecast"] + "\n"
    
    print(hej)

# upgift 6.3

url3  = "https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/"

r3 = requests.get(url3)

artist_dictonary = r3.json()


artistlist = ''

for s in artist_dictonary["artists"]:
    artistlist += s["name"] + "\n"

print(artistlist)

learnmore = input("Vilken artist vill du lära dig mer om: ")

for a in artist_dictonary["artists"]:
    if a["name"] == learnmore:
        url4 = 'https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/'+ a["id"]
        r4 = requests.get(url4)
        moreinfo = r4.json()
        print("Genres: ")
        for d in moreinfo["artist"]["genres"]:
            print(d)
        print("År aktiva ", moreinfo["artist"]["years_active"][0])
        print("Medlemmar: ")
        for x in moreinfo["artist"]["members"]:
            print(x)