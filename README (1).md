# CyberCrack: A Red Team Simulation Toolkit for Beginner-Level CTF and Ethical Hacking Practice

## Problem Statement

Cybersecurity education often lacks hands-on platforms that simulate real-world attack scenarios in a beginner-friendly environment. Many existing platforms require internet access or are too advanced for new learners. **CyberCrack** addresses this gap by providing a local, Linux-based simulation toolkit that mimics Red Team attack tactics in a safe and controlled environment.

## Key Features

- 15 progressive Red Team CTF levels
- AI-based challenge design
- Terminal-based interactive experience
- Inspired by OverTheWire (Krypton, Leviathan, Natas)
- Localhost deployment – no internet needed
- Beginner-friendly Linux and hacking fundamentals



## Setup Instructions

### Prerequisites
- Ubuntu/Kali Linux environment
- Basic knowledge of terminal commands

### Installation
```bash
git clone https://github.com/sachi_yash/CyberCrack.git
cd CyberCrack
chmod +x setup.sh
./setup.sh


### Starting the Simulation
```bash
cd level1
cat README.md  # Follow instructions in each level




## Folder Structure

CyberCrack/
├── levels/
│   ├── level1/
│   │   ├── README.md              # Instructions or challenge intro
│   │   ├── manual.txt             # Optional guide or story
│   │   ├── hidden_flag.txt        # Real flag file (can be hidden)
│   │   ├── flah.txt               # Decoy
│   │   ├── decoy1.txt             # Another decoy
│   │   ├── some_script.sh         # Decoy script
│   │   ├── .hidden_file           # Optional hidden file
│   │   ├── check.sh               # Script to verify correct flag
│   │   └── ...                    # Other misdirecting files



## Screenshots / Diagrams

### Sample Challenge:
![Level Screenshot](C:\Users\DELL1\Pictures\Screenshots)
![Screenshot (632)](https://github.com/user-attachments/assets/8920e905-a112-4ff1-a555-9aac9e7c0867)

### Architecture Diagram:
Flow:

User → Navigates to Level Folder → Reads Clue → Uses Linux commands → Finds Flag → Runs Check Script
You Can Draw Boxes Like:

[ User Terminal ]
       |
       v
[ CyberCrack Toolkit ]
       |
       v
[ Level 1 Folder ] -- [ Level 2 Folder ] -- ... -- [ Level 15 Folder ]
       |
       v
[ challenge.txt ] [ check_script.sh ] [ hidden_flag ]

### Log Example:

Level 3: base64.txt decoded successfully using `base64 -d`
Flag captured: FLAG{beginner_ctf_master}




## License

This project is licensed under the [MIT License](LICENSE).



## Disclaimer

This project is intended strictly for **educational and ethical hacking practice purposes**. Do not use these techniques on systems you do not own or have explicit permission to test. The developer is not responsible for any misuse of this tool.



## YouTube Demo

Watch the full video here:  
[**CyberCrack Project**](https://youtu.be/3YkBES0rRzs?si=dpfRLMyaMEPDW93I)
https://youtu.be/aSn-Oa1tVnk?si=yFmlKw9cabo4-fiM



## Developed By

**Sachi Ravindra Rane & Yash Dhumali**  
BSc IT – Sathaye College  
Email: sachirrane81@gmail.com  
GitHub: [sachiyash](https://github.com/sachiyash)
