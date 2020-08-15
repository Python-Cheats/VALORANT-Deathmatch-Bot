import pyautogui as pyg, time as t, datetime, keyboard, tkinter as tk

#Settings
wakeMethod = "moveclick"
GUIFont = ("Comic Sans", 30)
Failsafe = False
lowestSleepDelay = 0.8

#GUI Setup
GUI = tk.Tk()
GUI.title("Deathmatch XP Bot")

PADisp = tk.StringVar()
PALabel = tk.Label(GUI, textvariable = PADisp, font = GUIFont).pack()
XPDisp = tk.StringVar()
XPLabel = tk.Label(GUI, textvariable = XPDisp, font = GUIFont).pack()
GPDisp = tk.StringVar()
GPLabel = tk.Label(GUI, textvariable = GPDisp, font = GUIFont).pack()
TTDisp = tk.StringVar()
GPLabel = tk.Label(GUI, textvariable = TTDisp, font = GUIFont).pack()

PADisp.set("Press F1 to Pause")
XPDisp.set("XP Earned: No Stats Yet")
GPDisp.set("Games Played: No Stats Yet")
TTDisp.set("Average Game Time: No Stats Yet")



#Setup code
WakeUpTime = datetime.datetime.now()
XP = 0
StartDate = datetime.datetime.now()
EndDate = None
AverageTime = None
GamesPlayed = 0
t.sleep(0.3)
pause = False
pyg.FAILSAFE = Failsafe

#Main loop
while True:
	GUI.update()
	
	#Network error relaunch
	if  pyg.pixelMatchesColor(1704,236, (57,50,67), tolerance=80) and pyg.pixelMatchesColor(404,820, (53,49,64), tolerance=80) and pyg.pixelMatchesColor(1230,636, (33,37,43), tolerance=50):
		print("Network Error")
		#Close the app
		pyg.click(1000, 660)
		t.sleep(30)

		#Relaunch
		keyboard.send("WINDOWS")
		t.sleep(lowestSleepDelay)
		keyboard.write("VALORANT")
		t.sleep(lowestSleepDelay)
		keyboard.send("ENTER")

		#Wait for it to load
		t.sleep(50)

	#Ready for next game queue
	if  pyg.pixelMatchesColor(1893,25, (255,255,255)) and (pyg.pixelMatchesColor(1860,37, (53,60,76), tolerance=50) or pyg.pixelMatchesColor(1864,26, (126,118,175), tolerance=50)) and pyg.pixelMatchesColor(825,21, (42,71,65), tolerance=50) != True:
		
		pyg.click(1200, 60)
		print("Ready to queue")
		
		#Updates variables
		EndDate = datetime.datetime.now()
		XP = XP + 500
		GamesPlayed = GamesPlayed + 1
		AverageTime = (EndDate - WakeUpTime) / GamesPlayed
		GameTime = EndDate - StartDate
		log = open("Deathmatch Stats.txt", "w")
		log.write("Games Played: " + str(GamesPlayed) + "\nAverage Gametime: "+str(AverageTime)+"\nTotal XP: "+ str(XP))
		log.close()

		#Updates GUI from variables
		XPDisp.set("XP Earned: " + str(XP))
		GPDisp.set("Games Played: " + str(GamesPlayed))
		TTDisp.set("Average Game Time: " + str(AverageTime))
		GUI.update()

		#Confirm the match is ready to be started
		#XP delay
		print("XP Delay")
		t.sleep(12)

		#Clear rewards
		pyg.click(1700, 150)
		t.sleep(lowestSleepDelay)
		pyg.click(1700, 150)
		t.sleep(lowestSleepDelay)
		pyg.click(1700, 150)
		t.sleep(lowestSleepDelay)
		pyg.click(1700, 150)
		t.sleep(lowestSleepDelay)
		pyg.click(1700, 150)
		t.sleep(lowestSleepDelay)
		print("Rewards Cleared")

		#Clear match details processing error
		pyg.click(950,630)
		t.sleep(lowestSleepDelay)
		print("Match Details Processing Error Cleared")
		
		#Move to deathmatch in play tab
		t.sleep(lowestSleepDelay)
		pyg.click(950,20)
		t.sleep(lowestSleepDelay)
		pyg.click(950,20)
		t.sleep(lowestSleepDelay)
		pyg.click(1100,100)
		t.sleep(lowestSleepDelay)
		print("Moved To Deathmatch")

		#Starts the next game
		pyg.click(950,980)
		print(str(datetime.datetime.now()) + ": queing into a game\n\n\n")
		StartDate = datetime.datetime.now()

	if keyboard.is_pressed('F1'):
		pause = True
		print("Paused")
	if keyboard.is_pressed('F2'):
		pause = False
		print("Resumed")

	while pause:
		if keyboard.is_pressed('F2'):
			pause = False
		PADisp.set("PAUSED: Press F2 to Resume")
		GUI.update()
	PADisp.set("Press F1 to Pause")

	if wakeMethod.find("click") != -1:
		pyg.click(950,550)
	if wakeMethod.find("move") != -1:
		keyboard.send("w", do_release=False)
	
