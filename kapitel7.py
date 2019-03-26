from random import randint
# uppgift 1
mult = int(input("Välj."))
hej = 0
check = 0
while True:
    print(mult*hej)

    hej += 1
    check += 1
    if check == 3:
        fraga = input("Vill du försätta?")
        if fraga == "ja":
            check = 0
            continue
        else:
            break


# uppgift 2

gnum = int(input("Välj ett number"))

dnum = randint(0,100)

while True:
    if gnum > dnum:
        print("LOWER")
        gnum = int(input("Välj ett nytt number"))
        
    else:
        print("HIGHER")
        gnum = int(input("Välj ett number"))
        
    if gnum == dnum:
        print(gnum, "Helt rätt")
        break
