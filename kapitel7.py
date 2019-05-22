from random import randint
# uppgift 1
mult = int(input("Välj."))
hej = 0
check = 0
while True:
    print(mult*hej) 

    hej += 1
    check += 1
    if check == 3: # när den har loopat 3 gånger fråga om du vill forsättta
        fraga = input("Vill du försätta?") # om de vill forsätta -> forsätt annars breaka loopen.
        if fraga == "ja":
            check = 0
            continue
        else:
            break


# uppgift 2

gnum = int(input("Välj ett number"))

dnum = randint(0,100) # random nummer 

while True:
    if gnum > dnum: # det ena är större än det andra väl ett nytt
        print("LOWER")
        gnum = int(input("Välj ett nytt number"))
        
    else:
        print("HIGHER")
        gnum = int(input("Välj ett number"))
        
    if gnum == dnum: # om man gissar rätt. 
        print(gnum, "Helt rätt")
        break
