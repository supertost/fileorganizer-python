<h1 align="center">File Organizer</h1>

<p align="center">
  <img src="https://github.com/supertost/fileorganizer-python/blob/main/assets/icons/FileOrganizerIcon512.png" alt="App Icon" width="100"/>
</p>

<p align="center">A Python program that automatically organizes files in a directory you choose</p>

---

## What it does

- Organize files based on categories such as **Audio**, **Video**, **Document** and **Image**
- If a file does not match a known category, it is placed into a folder named after its file extension
- Has the ability to exclude specific file extensions from being organized.

---

## Program in action
1. Organization with extension **extension exclusion**
<video src="https://github.com/user-attachments/assets/d1a9ce2a-eeb4-4336-b8fd-f4e86880caba" alt="exclusion video"></video>

2. Organization with **no extension exclusion**
<video src="https://github.com/user-attachments/assets/c5b80898-bb3f-4924-aada-413997ee2397" alt="no exclusion video"></video>


## Installation

1. Clone the repository

    <code>git clone https://github.com/supertost/fileorganizer-python.git</code>
    <br><code>cd fileorganizer-python</code>

2. Run the the program
    <br><code>python3 run.py</code>

---

### If you would like to run the unit tests:

1. After cloning the repository, install requirements with:
<br><code>pip install -r requirements.txt</code>

2. Run pytest
<br><code>pytest</code>

