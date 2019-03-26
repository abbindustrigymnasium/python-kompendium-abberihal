
# uppgift 1

tot = 0

for number in range(1000000):
    tot += number # adderar på varje tal. 
    
print(tot)

# uppgift 2

summan = 0

for number in range(500): 
    if number%2 == 1: # använder modus och kollar om talet är jämnt eller udda
        summan += number 
print(summan)

# uppgift 3

reg = ["anna", "Eva", "Erik ", "Lars ", "Karl"]
avreg = ["anna", "Erik", "Karl"]

for names in avreg:
    if names in reg: # kollar om namnet finns i reg listan. 
        reg.remove(names)
    

print(reg)

# uppgift 4

name = ["Maria", "Erik", "Karl"]
lastname = ["Svensson", "Karlsson", "Andersson"]

for _name in name:
    for _lastname in lastname:
        print(_name + " " + _lastname )



