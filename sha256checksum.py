#  Check the SHA256 sum for a downloaded file and compare to that which is found on the software's official website  #
#                                                                                                                    #
#                                             Don't get pwn'd, kids                                                  #

from tkinter import filedialog
import subprocess
import os

# Stack overflow said you should do this to prevent 

file = filedialog.askopenfile()
if file:
    filepath = os.path.abspath(file.name)

s = subprocess.run(['certutil', '-hashfile', f'{filepath}',  'SHA256'], stdout=subprocess.PIPE)
pipeReturn = s.stdout.decode('utf-8')

print("\n" + pipeReturn)

requestedsha = input("Now paste the hash as indicated on the official website (please): ")

# Random lesson learned: if 2 strings don't appear to be comparing correctly, use print(acsii(strName)) to see escaped chars n shit

newrequestedsha = "SHA256 hash of " + filepath + ":\r\n" + requestedsha + "\r\n" + "CertUtil: -hashfile command completed successfully.\r\n" # Too lazy to format the 3 lines returned from stdout, so just mimicking the other 2 lines here o7

if pipeReturn == newrequestedsha:
    print("\n\n************ 8======D ************\n\nMatches! Always wrap your willy :-)\n\n************ C======D ************\n")
else:
    print("\n\n********************\n\nDelete this shit, you almost just got space herpies...\n\n********************\n")