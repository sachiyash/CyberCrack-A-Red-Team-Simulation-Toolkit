# Level 12 - Double Layered Cipher

*Objective:*  
Extract the flag hidden in a file using Caesar cipher and Base64 decoding.

*Challenge Description:*  
The file encoded.txt contains a secret message that has been encrypted in two stages:
1. First, the plain text flag was *Base64 encoded*.
2. Then, the resulting string was encrypted using a *Caesar cipher* with a shift of *+3*.

*Your Task:*  
Reverse the process to retrieve the flag.

---

## Steps to Solve

*Step 1: Decrypt the Caesar Cipher*

The Caesar cipher is a letter substitution method. Shift each letter in the string *backward by 3 positions*. You can use this Python snippet:

```python
text = "FbehuFufpesdqn{Sdvwhg_Gdwd}"
shift = 3
result = ""

for char in text:
    if char.isalpha():
        start = ord('A') if char.isupper() else ord('a')
        result += chr((ord(char) - start - shift) % 26 + start)
    else:
        result += char

print("Decoded Caesar:", result)
