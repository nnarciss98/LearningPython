import pyautogui
import time

# Take a screenshot
screenshot = pyautogui.screenshot()
screenshot.save("screenshot.png")

# Type text using the keyboard
pyautogui.write('Hello, this is automated typing!', interval=0.1)

# Click at a specific position on the screen
pyautogui.click(100, 200)  # Coordinates may vary

# Move the mouse and click
pyautogui.moveTo(200, 200, duration=1)
pyautogui.click()

# Perform a keyboard shortcut (Ctrl + C)
pyautogui.hotkey('ctrl', 'c')

# Wait for 2 seconds before continuing
time.sleep(2)