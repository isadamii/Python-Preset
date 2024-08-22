import os, re, sys, time, json, base64, random, string, ctypes, threading

os.system("cls")

try:
    import requests
    import datetime
    from colorama import Fore, Style
except ModuleNotFoundError:
    print("Modules Not Found! Installing...")
    os.system("pip install requests")
    os.system("pip install datetime")
    os.system("pip install colorama")


def current_time():
    return datetime.now().strftime(f"{Fore.LIGHTBLACK_EX}%I:%M:%S %p | {Style.RESET_ALL}")

def format_time(seconds):
    minutes = int(seconds // 60)
    seconds = int(seconds % 60)
    return f"{minutes}m {round(seconds)}s"

def red(text):
    os.system(""); faded = ""
    for line in text.splitlines():
        green = 250
        for character in line:
            green -= 5
            if green < 0:
                green = 0
            faded += (f"\033[38;2;255;{green};0m{character}\033[0m")
    return faded

def purple(text):
    os.system("")
    faded = ""
    down = False

    for line in text.splitlines():
        red = 40
        for character in line:
            if down:
                red -= 3
            else:
                red += 3
            if red > 254:
                red = 255
                down = True
            elif red < 1:
                red = 30
                down = False
            faded += (f"\033[38;2;{red};0;220m{character}\033[0m")
    return faded


def water(text):
    os.system(""); faded = ""
    green = 10
    for line in text.splitlines():
        faded += (f"\033[38;2;0;{green};255m{line}\033[0m\n")
        if not green == 255:
            green += 15
            if green > 255:
                green = 255
    return faded
