import pyautogui, subprocess, random, time, sys

def clickrange(range):
    left = range[0]
    top = range[1]
    width = range[2]
    height = range[3]
    range1 = random.uniform(left, left+width)
    range2 = random.uniform(top, top+height)
    return (range1, range2)


def calculateRegion(pos1, pos2):
	return (pos1[0], pos1[1], pos2[0] - pos1[0], pos2[1] - pos1[1])


def findImgInRegion(imgname, reg):
	item = pyautogui.locateOnScreen(imgname, region=reg, grayscale=True)
	if item != None:
		return True
	else:
		return False

def clickInRange(range):
    (x, y) = clickrange(range)
    pyautogui.moveTo(x, y, duration=random.uniform(0.1,0.3))
    pyautogui.click(x, y,clicks=1,interval=0.0,button='left',duration=0.2)
    time.sleep(random.uniform(.5, 1))
    return

def clickInRangeFast(range):
    (x, y) = clickrange(range)
    pyautogui.moveTo(x , y, duration=random.uniform(0.1,0.3))
    pyautogui.click(x, y,clicks=1,interval=0.0,button='left',duration=0.2)
    time.sleep(random.uniform(.5, 1))
    return


def newAction(imageName, imgCoordinates, clickCoordinates):
	while(findImgInRegion(imageName, imgCoordinates) == 0):
		time.sleep(0.2)

	print imageName + ' found, now clicking...'

	clickInRange(clickCoordinates)
	return
def newActionTime(imageName, imgCoordinates, clickCoordinates, maxTime):
	temptime=0
	testtime=0
	while(findImgInRegion(imageName, imgCoordinates) == 0):
		time.sleep(0.2)
		temptime=temptime + .2
		if(temptime >= maxTime):
			print imageName + " Not Found"
			testtime=1
			break
	if(testtime == 0):
		print imageName + ' found after...' + str(temptime)
		clickInRange(clickCoordinates)
	return

def keySequence(sequence):
    for i in sequence:
        pyautogui.press(str(i))

def delay(min, max):
    num = random.random(min, max)
    time.sleep(num)
    return num
    