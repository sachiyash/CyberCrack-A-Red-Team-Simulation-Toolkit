text = "Fdhvdu#Fubsfbdn{Sbwfsb_Ebwb}"
shift = 3

result = ""
for char in text:
    if char.isalpha():
        start = ord('A') if char.isupper() else ord('a')
        result += chr((ord(char) - start - shift) % 26 + start)
    else:
        result += char

print("Decoded:", result)
