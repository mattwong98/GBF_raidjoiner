import random,pyautogui, time
from methods import clickInRange, clickInRangeFast, clickrange

party = (475,110,20,40)
switchParty = (335,110,20,10)
quest = clickrange(740,110,20,50)
special = clickrange(220,368,60,10)
teamChangeOk = (300,530,70,10)
angelHalo = pyautogui.locateOnScreen("Angel_Halo.png")
clickInRange(party)
time.sleep(2)
clickInRange(switchParty)
time.sleep(1)
clickInRange(quest)
time.sleep(random.uniform(3,4))
clickInRange(special)