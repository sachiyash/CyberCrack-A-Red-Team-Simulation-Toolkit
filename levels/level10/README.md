# Level 10 - Binary Secrets

*Objective:*  
Analyze the compiled binary to uncover the correct password and retrieve the flag.

*Scenario:*  
You’ve obtained a mysterious executable file named check. When run, it asks for a password. If entered correctly, it prints the flag. Your task is to reverse-engineer the binary to find the hidden password.

*Hints:*
- The binary was compiled from C source code.
- You don’t need to brute-force — use reverse engineering techniques.
- Strings or disassemblers might help reveal the hardcoded password.

*Tools You Might Use:*
- strings check
- objdump -d check | less
- gdb, ghidra, or radare2 (for advanced users)

*Challenge Rating:*  
Medium to Hard

Binary truth is buried under layers of logic — find the key and unlock the flag.
