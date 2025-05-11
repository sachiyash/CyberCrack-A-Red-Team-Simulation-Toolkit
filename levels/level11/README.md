# Level 11 - Encoded Mystery

*Objective:*  
Decode the hidden flag from a multi-layered encoded message.

*Scenario:*  
A file named encoded.txt contains an encrypted flag. It has been obfuscated using multiple encoding layers — your job is to decode and extract the original flag.

*Encoding Process Used:*
1. The flag was written in plain text.
2. It was Base64 encoded and stored in encoded.txt.
3. Then the Base64 output was Caesar Cipher shifted by +3.

*Sample Decoding Steps:*
- Step 1: Decode the Base64-encoded file:
  ```bash
  base64 -d encoded.txt
