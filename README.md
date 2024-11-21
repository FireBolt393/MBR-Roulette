# MBR Roulette:

**MBR Roulette** is a multiplayer take on the classic game of Russian Roulette, where two players face off in a dangerous gamble. The twist? If you're playing on a **virtual machine** and lose, your Master Boot Record (MBR) will be overwritten. But if you're on a physical machine, you'll survive the outcome. Players take turns pressing the trigger, with the cylinder being spun (randomized) before every round.

## ⚠️ WARNING ⚠️

This game is designed for **virtual machines** only. If you lose while running this game in a virtual environment, your Master Boot Record (MBR) will be overwritten, rendering your virtual machine unbootable. It should never be played on a **real system**. By using this game, you accept full responsibility for any damages it may cause.

## Features

- Multiplayer gameplay using sockets.
- Players press the enter key to "pull the trigger" and wait for their opponent.
- Each round, the cylinder is spun (random chamber selected) to mimic spinning the barrel.
- If playing in a **virtual machine** and you lose, your MBR will be overwritten.
- If playing on a **physical machine**, you won't experience any system damage, but the game remains suspenseful.

## How It Works

- Two players connect over sockets.
- Before each turn, the cylinder (chamber) is spun to randomize the bullet's position.
- Players take turns pressing the enter key to pull the trigger.
- If the bullet is fired and you're playing on a virtual machine, your MBR will be overwritten.
- The only way to win the game is to survive until your opponent loses.

## Setup and Installation

### Requirements

- Python 3.x
- `socket` module (default Python library)
- Windows OS (since it uses Windows-specific system calls)
- Virtual machine for testing

### Instructions

**1. Clone the repository:**

   ```bash
   git clone https://github.com/FireBolt393/mbr-roulette.git
   cd mbr-roulette
   ```

**2. Run player1 and player2 files:**

   ```bash
   python player1.py
   ```

   ```bash
   python player2.py
   ```
   
**3. Press `Enter` to take your turn and wait.**
   
**4. Enjoy (or regret) playing.**

## Possible modifications:
Handle errors if the players disconnect. player1 file contains `tryAgain()` function that retries until both the players connect.

## Disclaimer:
This project is intended for educational and testing purposes only. The game is designed to demonstrate the risks of tampering with system files and performing dangerous operations. Do not play this game on a physical machine or any important system.

## License:
This project is open-source and distributed under the MIT License. See the LICENSE file for more details.

## Contributions:
Contributions are welcome!
