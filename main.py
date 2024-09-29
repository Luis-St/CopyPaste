import pyautogui as gui

try:
	print("Press CTRL + C to exit the programme")
	while True:
		text = input("Enter the text: ")
		gui.hotkey("alt", "tab")
		gui.write(text, 0.00001)
		gui.hotkey("alt", "tab")
		print("")
except KeyboardInterrupt:
	print("")
	input("\nPress any key to continue...")
