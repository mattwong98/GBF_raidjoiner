import pyperclip
import time
import pyautogui
import sys

pos1 = pyautogui.position()
time.sleep(4)
pos2 = pyautogui.position()

if(sys.argv[1]=='click'):
	print pos1[0], pos1[1], pos2[0], pos2[1], "-->Click Range"
	copything= str(pos1[0]) + ',' + str(pos1[1])+ ',' + str(pos2[0]) + ',' + str(pos2[1])
	pyperclip.copy(copything)
if(sys.argv[1]=='picture'):
	print pos1[0], pos1[1], pos2[0]-pos1[0], pos2[1]-pos1[1], "-->Picture Range"
	copything= str(pos1[0]) + ',' + str(pos1[1])+ ',' + str(pos2[0]-pos1[0]) + ',' + str(pos2[1]-pos1[1])
	pyperclip.copy(copything)

