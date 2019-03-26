# uppgift 1
citat = "xd xd xd xd"
print(citat.title()) # Ordens första bokstav blir stor. 

#uppgift 2
_float = input()

print("Här är talet: ",int(_float)) # skriver talet i int

# uppgift 3

print("Hej, Vad är ditt förnamn?")
name = input()
print("Vad är ditt efternamn")
lastname = input()

print ("Hej ", name + " " + lastname)

#uppgift 4

print("Hur gammal är du?")

age = input()

print("du är myndig om ", 18-age ," år")

# uppgift 5
print("hur många vill äta 2 vanliga korvar respektive 3 vanliga korvar")

dosKorvar = input()
treKorvar = input()

print("Hur många vill äta 2 veganska eller 3 veganska")

dosVeganska = input()
treVeganska = input()

veganBoxes = (int(dosVeganska) + int(treVeganska))/4 # dividerar antalet veganska på hur mångs om får plats i en förpackingn
realBoxes = (int(dosKorvar) + int(treKorvar)/8)

price = veganBoxes*34.95 + realBoxes*20.95 # antalet * med priset.  

print("2 vanliga korvar: ", dosKorvar, "Tre vanliga korvar: ", treKorvar, "2 veganska: ", dosVeganska, "3 veganska: " , treVeganska)

print("förpacknigar: KORV ", realBoxes, "vegan ", veganBoxes)

print("pris: ", price , " SEK")


