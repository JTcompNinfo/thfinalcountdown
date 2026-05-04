def inventory_menu(player, clear_func, screen_manager):
    while True:
        clear_func()

        print("=== INVENTORY ===")
        print(f"{player.name} | HP: {player.current_health}/{player.max_health}")
        print(f"Gold: {player.gold}")

        print("\nEquipped:")
        print(f"Weapon: {player.equipped_weapon.name if player.equipped_weapon else 'None'}")
        print(f"Armor: {player.equipped_armor.name if player.equipped_armor else 'None'}")

        print("\nItems:")
        if not player.inventory:
            print("  (Empty)")
        else:
            for i, item in enumerate(player.inventory):
                print(f"{i + 1}. {item}")

        print("\nOptions:")
        print("1. Use / Equip Item")
        print("2. Exit")

        choice = input("\nChoose: ")

        # =========================
        # USE / EQUIP
        # =========================
        if choice == "1":
            if not player.inventory:
                input("No items. Press Enter...")
                continue

            try:
                index = int(input("Select item #: ")) - 1
                item = player.inventory[index]

                if hasattr(item, "heal_amount"):
                    player.heal(item)

                elif hasattr(item, "attack_bonus"):
                    player.equip_weapon(item)

                elif hasattr(item, "defense_bonus"):
                    player.equip_armor(item)

                input("Press Enter...")

            except:
                input("Invalid choice. Press Enter...")

        # =========================
        # EXIT
        # =========================
        elif choice == "2":
            screen_manager.restore()
            break

        else:
            input("Invalid choice. Press Enter...")