import os
import time

print("Author: NoobDeveloper500")
print("Version 1.0")
time.sleep(1)

print("1-start wireless mode")
print("2-adb install apk")
print("3-adb uninstall package")
print("4-adb kill-server")
print("5-adb devices")
print("6-installed packages")

adbsh = input("enter number: ")

if adbsh == "1":
    os.system("adb tcpip 5555")
    deviceip = input("enter device ip: ")
    toconnect = "adb connect " + deviceip
    os.system(toconnect)

    print("1-back to usb mode")
    print("2-adb install apk")
    print("3-adb uninstall package")
    print("4-adb kill-server")
    print("5-adb devices")
    print("6-installed packages")

    while True:
        wirelessadbsh = input("enter number: ")

        if wirelessadbsh == "1":
            os.system("adb usb")
            break

        if wirelessadbsh "2":
            package = input("enter apk file name: ")
            toinstall = "adb install " + package

        if wirelessadbsh == "3":
            package = input("enter package name: ")
            touninstall = "adb uninstall " + package
            os.system(touninstall)

        if wirelessadbsh == "4":
            os.system("adb kill-server")

        if wirelessadbsh == "5":
            os.system("adb devices")

        if wirelessadbsh == "6":
            os.system("adb shell pm list packages")



    

if adbsh == "2":
    package = input("enter apk file name: ")
    toinstall = "adb install " + package
    os.system(toinstall)

if adbsh == "3":
    package = input("enter package name: ")
    touninstall = "adb uninstall " + package
    os.system(touninstall)

if adbsh == "4":
    os.system("adb kill-server")

if adbsh == "5":
    os.system("adb devices")

if adbsh == "6":
    os.system("adb shell pm list packages")