# MotoRSDFlash
Replaces the Motorola RSD Lite software with a simple python script. The RSD Lite software is buggy, and this script allows you to flash software quicker and more reliably than with RSD Lite. The script reads the XML file to determine all the steps, calculates and checks the MD5 hashes for all images to be flashed, and then flashes the firmware in the same order that RSD would.

# Instructions
Place the pyFlash.py script in the folder containing the unzipped firmware. Ensure that fastboot is in your system PATH, and that you have the correct fastboot drivers for your device.

# File Structure
![File Structure Example](firmware-structure.png)
