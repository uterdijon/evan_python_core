import random
import time
from rpg_objects import Hero, Opponent

def __main__():

    print("You are entering the dark, evil and scary forest of Hoia Baciu. Try to destroy every creature you meet and make it out the other side.")
    play_game()

def play_game():

    opponents = [
        Opponent("Goblin", 70),
        Opponent("Troll", 80),
        Opponent("Werewolf", 90)
    ]

    hero_name = input("Enter the hero's name: ")
    hero_level = input("Enter the hero's ability level (between 1 and 100): ")
    hero = Hero(hero_name, hero_level)

    while True:

        if len(opponents) <= 0:
            print ("Congratulations! {0} made it out of the evil forest! {0}'s final score is {1}.".format(hero.name, hero.score))
            exit()

        else:
            cmd = input("You are walking through the forest. Enter:\n <l> to look around\n or\n <q> for quit")

            if cmd not in ["l", "q"]:
                break

            if cmd == "q":
                "Too bad, the evil creatures will continue to rule the forest!"
                exit()

            if cmd == "l":

                opponent = random.choice(opponents)

                cmd = input("You look around and see a {0}. Would you like to attack? Enter <y> for yes and <n> for no.".format(opponent.name))

                if cmd == "y":
                    if hero.attack(opponent):
                        print("You won this battle! The {0} is dead. You will receive {1} points".format(opponent.name, opponent.level))
                        opponents.remove(opponent)
                        hero.score += opponent.level

                    else:
                        print("You lost. Now you must sleep and regain your power. You lose {0} points.".format(opponent.level))
                        hero.score -= opponent.level
                        time.sleep(5)
                        print("Now you are refreshed again.")


__main__()
