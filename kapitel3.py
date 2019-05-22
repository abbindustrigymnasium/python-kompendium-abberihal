# uppgift 1
male = ["Erik","Lars","Karl","Anders","Johan"]
female = ["Maria","Anna","Margareta","Elisabeth","Eva"]

#uppgift 5
print("Vem ska bort")
namn = input()
male.remove(namn) # tar bort
female.remove(namn)
# ---

print(male[0])
print(female[2])
print(female[4])
print(male[1])

# uppgift 2
del male[1] # tar bort
del male[2]
del female[0]
# ---

#uppgift 3
male.sort() # sorterar
female.sort()
# ---

print ("Män:", male )
print ("Kvinnor :", female )

