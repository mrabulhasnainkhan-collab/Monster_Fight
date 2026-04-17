import random
import time  

def Monster_Fight ():
    player_health = 100
    monster_health = 100
    print("WELCOME! WELCOME!")
    time.sleep(1)
    print("TO THE")
    time.sleep(1)
    print("MONSTER FIGHT!!")
    time.sleep(1.5)

    while player_health > 0 and monster_health > 0:
        action = input("\n""What you wanna choose? Do you want to (attack) or (heal)? ").lower()
        if action == "attack":
            damage = random.randint(10,20)
            monster_health -= damage
            time.sleep(1)
            print("Don't be Scared")
            time.sleep(1)
            print(f"You dealt {damage} damage to the monster!")
            time.sleep(1)

        elif action == "heal":
            heal = random.randint(10,20)
            player_health += heal
            time.sleep(1)
            print("Good Choice")
            time.sleep(1)
            print(f"You healed for {heal} Health!")
            time.sleep(1)

        # Monster Attacks Back
        monster_damage = random.randint(15,25)
        player_health -= monster_damage
        time.sleep(1)
        print("Ohh NOO")
        time.sleep(1)
        print(f"The monster dealt {monster_damage} damage to you")
        time.sleep(1)

        print(f"\nYour Health: {player_health}, Monster Health: {monster_health}")
        time.sleep(1)
        

    if player_health <=0:
        time.sleep(1)
        print("You have been defeated!")
        time.sleep(1)
        print("Never Give Up! Try one more time")
    else:
        time.sleep(1)
        print("What a match!!")
        time.sleep(1)
        print("You defeated the monster!")

Monster_Fight()