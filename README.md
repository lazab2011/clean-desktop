Move Desktop Files to Documents
This Python script automates the process of moving files and folders from the desktop to the Documents folder on a Windows system.

Prerequisites
Python 3.x installed on your system.
This script is specifically designed for Windows operating systems.

Installation
Clone or download the script to your local machine.
Ensure that Python is installed on your system.

Usage
1. Open the script in a text editor or Python IDE.
2. Modify the desktop_path variable to point to your desktop directory.
3. Run the script using Python.

Functionality
The script defines a function move_desktop_files_to_documents() which moves files and folders from the desktop to the Documents folder.
It first checks if the Documents folder exists. If not, it creates one.
It then lists all files and directories on the desktop and moves each item to the Documents folder.
After moving all files and folders, it prints a confirmation message.
