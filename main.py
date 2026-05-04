"""
Important imports
"""
import sys
import os
import subprocess
import random
try:
    import pyfiglet
except ImportError:
    print("pyfiglet not found. Installing...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pyfiglet", "--break-system-packages"])
    import pyfiglet

import shutil

from game_rules import NpcAndPlayerRules
from game_rules import itemRules
from game_rules import importantNpcs
from game_rules.shopRules import shop
from game_rules.combatRules import combat
from game_rules.inventoryRules import inventory_menu
import randomEccointers

godplayer = NpcAndPlayerRules.Player("god", 1000000)


def open_image(filepath):
    try:
        if sys.platform == "win32":
            os.startfile(filepath)
        elif sys.platform == "darwin":
            subprocess.run(["open", filepath])
        else:
            subprocess.run(["xdg-open", filepath], check=True)
    except (FileNotFoundError, OSError):
        print("Baller.jpeg can not open here")
        pass  # No display available (e.g. Codespaces), just skip it


def claer_termianl(player):
    os.system('cls' if os.name == 'nt' else 'clear')

    #baller is so baller more baller than baller
    if  "Ball of Baller" in player.inventory:
        print("baller")
        open_image('baller.jpeg')
# =========================
# SCREEN MANAGER
# =========================
class ScreenManager:
    def __init__(self):
        self.last_screen = None

    def save(self, screen_function):
        self.last_screen = screen_function

    def restore(self):
        if self.last_screen:
            claer_termianl()
            self.last_screen()

def randomecounter(player):
    LOOPMAX = random.randint(1, 30)
    loopyloop = 0
    while loopyloop != LOOPMAX:
        randomEccointers.randomEccounter
        claer_termianl
        loopyloop += 1

 
def print_inferno_map(player):
    map_lines = [
        r"            \ /  1. Limbo (Virtuous Pagans)",
        r"            / \ ",
        r"           /   \ 2. Lust (Stormy Winds)",
        r"          /_____\ ",
        r"         /       \ 3. Gluttony (Sludge & Rain)",
        r"        /_________\ ",
        r"       /           \ 4. Greed (Hoarding/Wasting)",
        r"      /_____________\ ",
        r"     /               \ 5. Anger (River Styx)",
        r"    /_________________\ ",
        r"   /                   \ 6. Heresy (Flaming Tombs)",
        r"  /_____________________\ ",
        r" /                       \ 7. Violence (Murder/Suicide)",
        r"/_________________________\ ",
        r"|                          \ 8. Fraud (Malebolge - Trenches)",
        r"|___________________________\ ",
        r"|                            \ 9. Treachery (Frozen Lake Cocytus)",
        r" \___________________________/ ",
        r"               || ",
        r"            LUCIFER",
    ]
 
    terminal_width = shutil.get_terminal_size().columns
    max_line_width = max(len(line) for line in map_lines)
 
    for line in map_lines:
        padding = (terminal_width - max_line_width) // 2
        print(" " * max(0, padding) + line)

    input(f"\n\nYou are one layer{player.stage}.\n\nPress enter to continune")
    claer_termianl(player)


# =========================
# The Layers Of Hell
# =========================
def layer9(player):
    player.level_up(538)
    claer_termianl(player)
    print_inferno_map(player)

def layer8(player):
    player.level_up(377)
    claer_termianl(player)
    print_inferno_map(player)
    layer9(player)

def layer7(player):
    player.level_up(302)
    claer_termianl(player)
    print_inferno_map(player)
    layer8(player)

def layer6(player):
    player.level_up(237)
    claer_termianl(player)
    print_inferno_map(player)
    layer7(player)

def layer5(player):
    player.level_up(194)
    claer_termianl(player)
    print_inferno_map(player)
    layer6(player)

def layer4(player):
    player.level_up(129)
    claer_termianl(player)
    print_inferno_map(player)
    layer5(player)

def layer3(player):
    player.level_up(86)
    claer_termianl(player)
    print_inferno_map(player)
    layer4(player)

def layer2(player):
    player.level_up(54)
    claer_termianl(player)
    print_inferno_map(player)
    layer3(player)

def layer1(player):
    claer_termianl(player)
    print_inferno_map(player)
    layer2(player)

def gamestart():
    claer_termianl(godplayer)
    name = input("Enter a Name for your character:\n")
    main_player = NpcAndPlayerRules.Player(name, 20) 
    main_player.inventory.append("Ball of Baller")
    layer1(main_player)
    



def start_screen():
    claer_termianl(godplayer)
    WIDTH = 102

    logo = pyfiglet.figlet_format("Devil's Hunger")

    print("+" + "=" * 100 + "+")

    for line in logo.splitlines():
        print("|" + line.center(100) + "|")
    
    print(f"{'|':<101}|")
    print(f"{'|':<101}|")
    print(f"{'|':<101}|")
    print(f"{'|':<101}|")
    print(f"{'|1. New Game':<101}|")
    print(f"{'|2. Load Game':<101}|")
    print(f"{'|3. Close Game':<101}|")
    print("+" + "=" * 100 + "+")
    startLoop = 0
    while startLoop == 0:
        try:
            startsceen = int(input())
        
            if startsceen == 1:
                startLoop += 1
                gamestart()
            elif startsceen == 2:
                startLoop +=1
                print("Sorry this does not work rn")
            elif startsceen == 3:
                startLoop += 1
                print("Thanks for playing!")
            else:
                print("That's not a valid choice!")

                
        except ValueError:
            print("That's not a valid choice!")

if __name__ == "__main__":
    start_screen()