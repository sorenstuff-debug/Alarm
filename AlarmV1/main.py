import sys
import time
import winsound
from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from plyer import notification

def startTimer():
    
    AlarmTime = input("how long should the timer go for? ex: 03:34:21 is 3hr, 34min, and 21s\n")
    totalT = toSeconds(AlarmTime)
    active = totalT
    while active > 0:
        active -= 1
        time.sleep(1)
        print(f"\rTimer for {AlarmTime} has {active} seconds left", end="", flush=True)
    notification.notify(title = "Alarm!", message = "Your alarm is done!", timeout = 10)
    
    for i in range(4):
        winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS)
    


def toSeconds(time):

    hourStr, minStr, secStr = time.split(":")
    return (int(hourStr) * 3600) + (int(minStr) * 60) + int(secStr)


startTimer()