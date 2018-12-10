import xml.etree.ElementTree as ET
import subprocess
import time
import os
import hashlib

for file in os.listdir():
    if file.endswith(".xml"):
        flashfile = file

print("Using XML File " + file)

flashdata = ET.parse(flashfile)
flashdata = flashdata.getroot()
steps = flashdata[1]

for step in steps:
    if step.attrib['operation'] == 'reboot-bootloader':
        command = "fastboot reboot bootloader"
        wait = 7
    if step.attrib['operation'] == 'flash':
        command = "fastboot flash " + step.attrib['partition'] + " " + step.attrib['filename']
        wait = 1
    if step.attrib['operation'] == 'erase':
        command = "fastboot erase " + step.attrib['partition']
        wait = 1
    print(command)
    print(subprocess.check_output(command, shell=True).decode())
    time.sleep(wait)

print(subprocess.check_output("fastboot reboot", shell=True).decode())