# add your code here
#Cesaer Cypher Using Dictionaries
# Dictionary
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# Asking user input
print ("Please Enter A Sentence")
inputString = input()

# Shift of 5
shift = 5

transAlphabet = {}

# Cypher
for i in range(0, 26):
    letter = alphabet[i]
    transAlphabet[letter]=alphabet [(i+shift) % 26]



# Coded Message Output
    print(alphabet[i] + ":" + transAlphabet[letter])
print(transAlphabet)

