gender = input("Kön")

eye = input("Ögonfärg")

hair = input("Hårfärg")


if gender == "man" and eye == "brun" and hair == "brun":
    print("du är Daniel Radcliffe")
elif gender == "man" and eye == "brun" and hair == "röd":
    print("du är Rupert")
elif gender == "kvinna" and eye == "brun" and hair == "brun":
    print("du är Selena gomez och Emma watson")
elif gender == "man" and eye == "brun" and hair == "grön":
    print("du är Shreck")
elif gender == "man" and eye == "grön" and hair == "orange":
    print("du är Donald Trump")
elif gender == "kvinna" and eye == "brun" and hair == "svart":
    print("du är någon")
else: 
    print("du finns inte med i systemet")

age = int(input("skriv din ålder: "))

timmar = [14, 13, 12, 11.5, 11, 10.5, 10, 9.5, 9, 8.5, 8]

if age == 1:
    print("du ska sova", timmar[0])

if age == 2:
    print("du ska sova", timmar[1])

if age == 3:
    print("du ska sova", timmar[2])

if age == 4:
    print("du ska sova", timmar[3])

if age == 5 or age == 6:
    print("du ska sova", timmar[4])

if age == 7:
    print("du ska sova", timmar[5])

if age == 8 or age == 9 or age == 10:
    print("du ska sova", timmar[6])

if age == 11:
    print("du ska sova", timmar[7])

if age == 12 or age == 13 or age == 14 or age == 15:
    print("du ska sova", timmar[8])

if age == 16:
    print("du ska sova", timmar[9])

if age >= 17:
    print("du ska sova", timmar[10])


state = input("Skriv landet ")

norden = ["svergie", "finland", "norge", "danmark", "island"]

stor = ["england", "nordirland", "skottland", "wales"]

if state.lower() in norden:
    print("du kommer från norden")
elif state.lower() in stor:
    print("du kommer från storb ri<nrar")
else: 
    print("landet ligger inte här")