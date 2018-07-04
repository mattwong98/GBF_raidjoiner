import random,pyautogui, time
from methods import clickInRange, clickInRangeFast, clickrange, supplies, delay

#offset is measured by the difference from the top left most possible coordinates to the current coordinates

menu = pyautogui.locateOnScreen("lib\_menu.png")
offsetX = menu(0) - 383
offsetY = menu(1) - 34
party = (475+offsetX,110+offsetY,20,40)
switchParty = (335+offsetX,110+offsetY,20,10)
teamSlot7 = (375+offsetX,150+offsetY,25,30)
team1 = (125+offsetX,415+offsetY,10,10)
teamChangeOk = (300+offsetX,530+offsetY,70,10)
support2 = (170+offsetX,455+offsetY,180,20)
ok = (270+offsetX,540+offsetY,130,5)
member3skill2  = (200+offsetX,528+offsetY,10,14)
raidButton = (320+offsetX,380+offsetY,100,10)
enterID = (330+offsetX,200+offsetY,80,20)
pendingBattles = (220+offsetX,820+offsetY,70,5)
pendingBattleRegion = (65+offsetX, 150+offsetY, 350, 110)

double durray = input("Number of hours: ")*3600

durray -= delay(1,3)
clickInRange(party)

durray -= delay(1,3)
clickInRange(switchParty)

durray -= delay(1,3)
clickInRange(teamSlot7)

durray -= delay(1,3)
clickInRange(team1)

durray -= delay(1,2)
clickInRange(teamChangeOk)

durray -= delay(3,8)

#declare variables
raid = "lib\_twinEle.png" 
support = support2
raidLocation = None
clickInRange(menu)
durray -= delay(0.5,1)
questButton = pyautogui.locateOnScreen("_quest.png")
clickInRange(questButton)
raidButton = pyautogui.locateOnScreen("lib\_raidButton.png")
if(raidButton == None):
    raidButton = pyautogui.locateOnScreen("lib\_specialQuestButton.png")
    raidButton = (raidButton[0]+raidButton[2]+14, raidButton[1],raidButton[2],raidButton[3])

while (durray > 0):
    clickInRange(raidButton)
    
    while (raidLocation == None):
        raidLocation = pyautogui.locateOnScreen(raid)
        durray-=delay(30,60)
    clickInRange(raidLocation)
    durray -= delay(1,2)
    test = pyautogui.locateOnScreen("lib\_cancel.png")
    if (test !=None):
        pyautogui.clickinrange(test)
    else:
        clickInRangeFast(support)
        durray -= delay(0.5,1.5)
        clickInRangeFast(ok)
        durray -= delay(12,14)
        test = pyautogui.locateOnScreen("lib\_ok.png")
        if (test!=None):
            pyautogui.clickinrange(test)
        else:
            clickInRangeFast(command)

        

            