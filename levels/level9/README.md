# Level 9 - Pixels Can Talk

*Objective:*  
Extract the hidden flag concealed within an innocent-looking image.

*Scenario:*  
You’ve received an image named hidden_flag.jpg. But remember — in the world of cybersecurity, images can carry more than meets the eye. Somewhere in the pixels, a secret message lies buried.

*Hints:*
- Tools like steghide allow data to be embedded within images.
- A password was used during embedding: cyber456.
- Use proper extraction commands and pay attention to file outputs.

*Tools You Might Use:*
- steghide extract -sf hidden_flag.jpg -p cyber456
- file hidden_flag.jpg
- exiftool, binwalk, or strings (if exploring deeper)

*Challenge Rating:*  
Medium

Sometimes secrets aren’t stored in plain sight — they’re painted into the background.
