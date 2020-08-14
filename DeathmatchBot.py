import pyautogui as pyg, time as t, datetime, keyboard, tkinter as tk

#Settings
loopDelay = 5
wakeMethod = "moveclick"
GUIFont = ("Arial", 30)
CountFirstGame = False
Failsafe = False

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


#Loop to initate the first game
while True:
	GUI.update()
	if  (not CountFirstGame) or (pyg.pixelMatchesColor(1893,25, (255,255,255)) and pyg.pixelMatchesColor(825,21, (42,71,65), tolerance=60) != True):
		
		pyg.click(932,1000)

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

			if  pyg.pixelMatchesColor(1893,25, (255,255,255)) and pyg.pixelMatchesColor(1860,37, (53,60,76), tolerance=30) and pyg.pixelMatchesColor(825,21, (42,71,65), tolerance=60) != True:
				t.sleep(12)
				EndDate = datetime.datetime.now()
				pyg.click(932,1000)
				XP = XP + 500
				GamesPlayed = GamesPlayed + 1
				
				#Updates variables
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

				#Starts the next game
				print(str(datetime.datetime.now()) + ": queing into a game\n\n\n")
				StartDate = datetime.datetime.now()

			if keyboard.is_pressed('F1'):
					pause = True
			if keyboard.is_pressed('F2'):
				pause = False

			while pause:
				if keyboard.is_pressed('F2'):
					pause = False
				PADisp.set("PAUSED: Press F2 to Resume")
				GUI.update()
			PADisp.set("Press F1 to Pause")

			if wakeMethod.find("click") != -1:
				pyg.click(1816, 113)
			if wakeMethod.find("move") != -1:
				keyboard.send("w", do_release=False)
			
