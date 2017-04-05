#! /usr/bin/env python3

import os
from map import Map
from time import sleep
from character import Player, Monster


def MainMenuPrompt():
    os.system("clear")

    print("\tWelcome to Place Holder!\n\n")

    print("[N]ew Game\n[L]oad Game\n[E]xit\n")

    choice = input("Choose an option: ").lower()[:1]

    return choice

def NewGame():
    # Create a new game
    # Create a new board
    # Prompting player for name
    # Creating a character
    print("You selected New Game")

def LoadGame():
    # Prompt the user for save file
    # Load game state
    print("You selected Load Game")

def Exit():
    # Display parting message
    # exit()
    print("You selected Exit")

def main():

    choice = MainMenuPrompt()

    if choice == 'n':
        NewGame()
    elif choice == 'l':
        LoadGame()
    elif choice == 'e':
        Exit()
    else:
        print("Invalid Option!")

    hero = Player("John")

    newMap = Map(10, 10)
    for _ in range(3):
        newMap.addCharacter(Monster())
    newMap.addCharacter(hero)
    while True:
        os.system("clear")
        print(newMap)
        newMap.update()


if __name__ == '__main__':
    main()
