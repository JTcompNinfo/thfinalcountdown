# =====================================================
# COMBAT SYSTEM
# =====================================================

import random
import os


# =====================================================
# DISPLAY
# =====================================================

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def draw_combat_ui(player, enemy, last_actions=None):
    """
    Draws the full combat screen:
      - Left column: actions menu
      - Right column: player stats
      - Below: enemy health
      - Below that: last round's action log
    """
    clear_terminal()

    COL = 38                    # width of each half
    TOTAL = COL * 2 + 3        # full box width including side borders

    weapon_name = player.equipped_weapon.name if player.equipped_weapon else "None"
    armor_name  = player.equipped_armor.name  if player.equipped_armor  else "None"

    left_lines = [
        "  ACTIONS",
        "",
        "  1. Attack",
        "  2. Use Healing Item",
        "",
        "",
        "",
    ]

    right_lines = [
        f"  {player.name}",
        f"  HP:     {player.current_health}/{player.max_health}",
        f"  ATK:    {player.get_attack_power()}",
        f"  DEF:    {player.get_defense()}",
        f"  Weapon: {weapon_name}",
        f"  Armor:  {armor_name}",
        "",
    ]

    # Make both columns equal height
    height = max(len(left_lines), len(right_lines))
    while len(left_lines)  < height: left_lines.append("")
    while len(right_lines) < height: right_lines.append("")

    # ── Top border ──
    print("+" + "=" * COL + "+" + "=" * COL + "+")

    # ── Two-column rows ──
    for l, r in zip(left_lines, right_lines):
        print(f"|{l:<{COL}}|{r:<{COL}}|")

    # ── Divider ──
    print("+" + "=" * COL + "+" + "=" * COL + "+")

    # ── Enemy health (full width) ──
    enemy_str = f"  {enemy.name}   HP: {enemy.current_health}/{enemy.max_health}"
    print("|" + enemy_str.ljust(TOTAL - 2) + "|")
    print("+" + "=" * (TOTAL - 2) + "+")

    # ── Last round action log ──
    if last_actions:
        for line in last_actions:
            print("|" + f"  {line}".ljust(TOTAL - 2) + "|")
    else:
        print("|" + "  ...".ljust(TOTAL - 2) + "|")

    print("+" + "=" * (TOTAL - 2) + "+")


# =====================================================
# STAGE EFFECTS
# =====================================================

def apply_stage_effects(player, enemy):
    """
    Modify combat based on Inferno layer (stage).
    Returns an effects dict. Stage flavour text is stored
    and shown in the action log instead of printed raw.
    """
    stage = player.stage
    effects = {}

    if stage == 5:
        effects["stage_msg"] = "The air burns with wrath..."
        effects["bonus_damage"] = 2

    elif stage == 9:
        if random.random() < 0.2:
            effects["stage_msg"] = f"{enemy.name} is frozen in betrayal!"
            effects["skip_enemy_turn"] = True

    return effects


# =====================================================
# PLAYER TURN
# =====================================================

def player_turn(player, enemy, effects, last_actions, draw_fn):
    """
    Handles player input. Returns a list of action strings
    describing what happened this turn.
    """
    turn_log = []

    # Pass through any stage message
    if "stage_msg" in effects:
        turn_log.append(effects["stage_msg"])

    while True:
        draw_fn(last_actions + turn_log if turn_log else last_actions)
        try:
            choice = input("\n> ").strip()
        except ValueError:
            continue

        if choice == "1":
            # ── Attack ──
            bonus = effects.get("bonus_damage", 0)
            damage = max(1, player.get_attack_power() - enemy.defense) + bonus
            enemy.take_damage(damage)
            turn_log.append(f"{player.name} attacked {enemy.name} for {damage} damage!")
            return turn_log

        elif choice == "2":
            # ── Use Healing Item ──
            healing_items = [i for i in player.inventory if hasattr(i, "heal_amount")]

            if not healing_items:
                turn_log.append("No healing items in inventory!")
                draw_fn(last_actions + turn_log)
                input("  (press Enter)")
                turn_log.clear()
                continue

            # Show inventory sub-menu
            inv_lines = ["  Choose an item:"]
            for idx, item in enumerate(healing_items, 1):
                inv_lines.append(f"  {idx}. {item}")
            inv_lines.append("  0. Cancel")
            draw_fn(inv_lines)

            try:
                item_choice = int(input("\n> "))
                if item_choice == 0:
                    turn_log.append("Cancelled item use.")
                    continue
                if 1 <= item_choice <= len(healing_items):
                    chosen = healing_items[item_choice - 1]
                    old_hp = player.current_health
                    player.heal(chosen)
                    healed = player.current_health - old_hp
                    turn_log.append(f"{player.name} used {chosen.name} and healed {healed} HP!")
                    return turn_log
                else:
                    turn_log.append("Invalid choice.")
                    continue
            except ValueError:
                turn_log.append("Invalid choice.")
                continue

        else:
            turn_log.append("That's not a valid choice!")
            draw_fn(last_actions + turn_log)
            input("  (press Enter)")
            turn_log.clear()
            continue


# =====================================================
# ENEMY TURN
# =====================================================

def enemy_turn(player, enemy, effects):
    """
    Handles enemy action. Returns a string describing what happened.
    """
    if effects.get("skip_enemy_turn"):
        return f"{enemy.name} cannot act!"

    old_hp = player.current_health
    damage = max(1, enemy.attack_power - player.get_defense())
    player.take_damage(damage)
    taken = old_hp - player.current_health
    return f"{enemy.name} attacked {player.name} for {taken} damage!"


# =====================================================
# FULL COMBAT LOOP
# =====================================================

def combat(player, enemy):
    last_actions = ["..."]

    # Defined outside loop so closure always reads current last_actions
    def draw(log_override=None):
        draw_combat_ui(player, enemy, log_override if log_override is not None else last_actions)

    while player.is_alive() and enemy.is_alive():

        # Apply stage effects
        effects = apply_stage_effects(player, enemy)

        # Player turn — returns list of action strings
        turn_log = player_turn(player, enemy, effects, last_actions, draw)

        if not enemy.is_alive():
            turn_log.append(f"{enemy.name} has been defeated!")
            draw_combat_ui(player, enemy, turn_log)
            input("\n  (press Enter to continue)")
            last_actions = turn_log
            break

        # Enemy attacks — append to same log so both show next turn
        enemy_msg = enemy_turn(player, enemy, effects)
        turn_log.append(enemy_msg)
        last_actions = turn_log

        if not player.is_alive():
            draw_combat_ui(player, enemy, last_actions)
            input("\n  (press Enter to continue)")
            break

    return player.is_alive()