import pyautogui
import time
import pyfiglet
from colorama import Fore

print(Fore.RED + pyfiglet.figlet_format("Moving_Mouse"))


def Computer_On():
    WakingTime = input("How much time would you like to stay the computer on by itself(minutes): ")
    TimeToMove = input("how often would you like the moving(minutes)? ")
    timeNow = time.strftime("%H:%M").split(":")
    endTime = int(timeNow[1]) + int(WakingTime)
    endHour = 0
    if endTime > 60:
        while endTime > 60:
            endTime = endTime - 60
            endHour += 1
        if len(str(endTime).split("")) == 1:
            endTime = "0" + str(endTime)
        finalH = int(timeNow[0]) + endHour
        finalTime = f"{finalH}:{endTime}"
        print(f"The computer stay on by himself until - {finalTime}")
        while time.strftime("%H:%M") != finalTime:
            pyautogui.moveTo(100, 100)
            pyautogui.moveTo(110, 130)
            pyautogui.moveTo(120, 150)
            pyautogui.moveTo(130, 120)
            pyautogui.moveTo(140, 250)
            pyautogui.moveTo(150, 150)
            pyautogui.moveTo(160, 130)
            pyautogui.moveTo(170, 150)
            pyautogui.moveTo(180, 120)
            pyautogui.moveTo(200, 250)
            time.sleep(60)

    else:
        finalTime = f"{timeNow[0]}:{endTime}"
        print(f"The computer stay on by himself until - {finalTime}")
        while time.strftime("%H:%M") != finalTime:
            pyautogui.moveTo(100, 100)
            pyautogui.moveTo(110, 130)
            pyautogui.moveTo(120, 150)
            pyautogui.moveTo(130, 120)
            pyautogui.moveTo(140, 250)
            pyautogui.moveTo(150, 150)
            pyautogui.moveTo(160, 130)
            pyautogui.moveTo(170, 150)
            pyautogui.moveTo(180, 120)
            pyautogui.moveTo(200, 250)
            time.sleep(60)


Computer_On()
