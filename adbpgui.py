import os
import time

print("Author: NoobDeveloper500")
print("Version 1.0")
time.sleep(1)

print("1-install adb")
print("2-remove adb")
print("3-adb install apk")
print("4-adb uninstall package")
print("5-adb kill-server")
print("6-adb devices")
print("7-installed packages")

adbsh = input("enter number: ")

if adbsh == "1":
    os.system("sudo apt install adb")
    
if adbsh == "2":
    os.system("sudo apt remove adb")

if adbsh == "3":
    package = input("enter apk file name: ")
    toinstall = "adb install " + package
    os.system(toinstall)

if adbsh == "4":
    package = input("enter package name: ")
    touninstall = "adb uninstall " + package
    os.system(touninstall)

if adbsh == "5":
    os.system("adb kill-server")

if adbsh == "6":
    os.system("adb devices")

if adbsh == "7":
    os.system("adb shell pm list packages")
