import os
import threading
import time
import socket
from datetime import datetime
from colorama import init, Fore, Style

init(autoreset=True)

# Users and limits
users = {
    "Zjoch": {"pass": "Test", "concu": 1, "time": 60},
    "zSky": {"pass": "Zsky", "concu": 1, "time": 60},
    "lulumina": {"pass": "luluadmin", "concu": 2, "time": 300}
}

# Track if user is attacking
user_attacks = {}

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def print_red(text):
    print(Fore.RED + text + Style.RESET_ALL)

def attack_banner():
    banner = """
   ▗▄▖▗▄▄▄▖▗▄▄▄▖▗▄▖  ▗▄▄▖▗▖ ▗▖     ▗▄▄▖▗▄▄
