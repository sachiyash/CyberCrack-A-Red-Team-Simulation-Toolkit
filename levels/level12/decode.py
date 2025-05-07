text = "FbehuFufpesdqn{Sdvwhg_Gdwd}"
shift = 3

result = ""

for char in text:
    if char.isalpha():
        # Determine if it's uppercase or lowercase
        start = ord('A') if char.isupper() else ord('a')
        # Shift backward by 3 with wrap-around using modulo
        result += chr((ord(char) - start - shift) % 26 + start)
    else:
        # Keep non-alphabet characters unchanged
        result += char

print("Decoded:", result)


