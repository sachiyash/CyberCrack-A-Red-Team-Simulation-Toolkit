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

---

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
```

### Starting the Simulation
```bash
cd level1
cat README.md  # Follow instructions in each level
```

---

## Folder Structure

```
CyberCrack/
├── README.md
├── LICENSE
├── docs/
│   └── Full_Documentation.md
├── demo/
│   ├── screenshots/
│   └── logs/
├── level1/ to level15/
├── setup.sh
```

---

## Screenshots / Diagrams

### Sample Challenge:
![Level Screenshot](demo/screenshots/level1_example.png)

### Architecture Diagram:
![Architecture](demo/screenshots/architecture_diagram.png)

### Log Example:
```
Level 3: base64.txt decoded successfully using `base64 -d`
Flag captured: FLAG{beginner_ctf_master}
```

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Disclaimer

This project is intended strictly for **educational and ethical hacking practice purposes**. Do not use these techniques on systems you do not own or have explicit permission to test. The developer is not responsible for any misuse of this tool.

---

## YouTube Demo

Watch the full demo video here:  
[**CyberCrack Project Demo**](https://www.youtube.com/watch?v=your_video_link_here)

---

## Developed By

**Sachi Ravindra Rane**  
BSc IT – Sathaye College  
Email: sachirrane81@gmail.com  
GitHub: [sachi_yash](https://github.com/sachi_yash)