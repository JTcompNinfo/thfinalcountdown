import random
from game_rules.itemRules import ITEM_DICT, ALL_POOLS
import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def generate_shop(stage):
    names = ALL_POOLS.get(stage, ALL_POOLS[1])
    items = [ITEM_DICT[name] for name in names]
    return random.sample(items, len(items))


def shop(player):
    shop_items = generate_shop(player.stage)

    while True:
        clear_terminal()
        try:
            if player.stage == 1:
                print("\n=== Gary's Deprsion Surpesion ===")
            elif player.stage == 2:
                print("\n=== Spencer's===")
            elif player.stage == 3:
                print("\n=== City Chinese Pop Up shop and Buffet ===")
            elif player.stage == 4:
                print("\n=== Gary's Deprsion Surpesion ===")
            elif player.stage == 5:
                print("\n=== Gary's Deprsion Surpesion ===")
            elif player.stage == 6:
                print("\n=== Gary's Deprsion Surpesion ===")
            elif player.stage == 7:
                print("\n=== Gary's Deprsion Surpesion ===")
            elif player.stage == 8:
                print("\n=== Gary's Deprsion Surpesion ===")
            elif player.stage == 9:
                print("\n=== Gary's Deprsion Surpesion ===")
            print(f"Gold: {player.gold}")

            # BUY
            print("\nBuy:")
            for i, item in enumerate(shop_items, 1):
                print(f"{i}. {item}")

            # SELL
            print("\nSell:")
            for i, item in enumerate(player.inventory, len(shop_items) + 1):
                print(f"{i}. {item.name} - {item.price // 2} gold")

            exit_option = len(shop_items) + len(player.inventory) + 1
            print(f"{exit_option}. Leave")

            choice = input("Choose: ")

            if choice == str(exit_option):
                break

            # BUY
            elif choice.isdigit() and 1 <= int(choice) <= len(shop_items):
                item = shop_items[int(choice) - 1]

                if player.gold >= item.price:
                    player.gold -= item.price
                    player.add_to_inventory(item)
                    print(f"Bought {item.name}")
                else:
                    print("Not enough gold")

            # SELL
            elif choice.isdigit() and len(shop_items) < int(choice) <= len(shop_items) + len(player.inventory):
                index = int(choice) - len(shop_items) - 1
                item = player.inventory[index]

                player.gold += item.price // 2
                player.inventory.remove(item)

                print(f"Sold {item.name}")

        except ValueError:
            print("Invalid choice")       