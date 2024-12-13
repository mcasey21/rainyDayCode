OriginalCypher = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 
    'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 
    'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 
    't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 
    'z': 26
}

Message = input("Enter message -> ").lower()
CC_key = int(input("Enter Ceaser Cypher Key -> "))

def get_key_by_value(dictionary, value):
    for key, val in dictionary.items():
        if val == value:
            return key
    
EncryptedCypher = {} # create new empty dict to allow encrypted values
for key, value in OriginalCypher.items():
    # wrap around and encryption logic
    # % 26 to keep it within alphabet to numbers (a=1 ... z=26)
    # copy new alphabet numbers into a new dict
    EncryptedCypher[key] = (value + CC_key - 1) % 26 + 1

encrypted_message = ""

for char in Message:
    # encrypt if the character is in the alphabet
    if char in OriginalCypher:
        # get the shifted value
        # find the letter using function
        encrypted_value = EncryptedCypher[char]
        encrypted_char = get_key_by_value(OriginalCypher, encrypted_value)
        encrypted_message += encrypted_char
    else:
        # skip non-alphabet characters
        encrypted_message += char

print("Encrypted Message:", encrypted_message)
