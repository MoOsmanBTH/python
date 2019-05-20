#Inte klar

def swap(element1, element2):
    temp = element1
    element1 = element2
    element2 = temp

alphabet = ["%s"%(chr(a))for a in range(ord("A"),ord("Z")+ 1, 1)]
word = "PLAYFAIR"

for a in range(0, len(word), 1):
    swap(alphabet[a], aword[])


alphabet.pop(9)    


table = ""
for a in range(0, 5, 1):
    for b in range(0,5,1):
        table += alphabet[a*5+b]
    table += "\n"

print(table)