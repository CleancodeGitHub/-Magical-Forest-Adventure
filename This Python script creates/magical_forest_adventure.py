def play_game():
    print("Welcome to the Magical Forest Adventure!")
    name = input("What's your name, brave adventurer? ")
    print(f"Hello, {name}! Get ready for an enchanting journey!")

    should_we_play = input("Do you want to embark on this magical quest? (yes/no) ").lower()

    if should_we_play in ["yes", "y"]:
        print("Let the adventure begin!")

        path = input("You come across a fork in the path. Do you take the glowing path or the shadowy trail? (glow/shadow) ").lower()
        
        if path == "glow":
            print("The glowing path leads you to a fairy glade. The fairies grant you magical powers!")
            
            choice = input("Do you want to use your new powers to fly or to become invisible? (fly/invisible) ").lower()
            
            if choice == "fly":
                print("You soar above the forest and discover a hidden castle in the clouds. Congratulations, you've completed the quest!")
            elif choice == "invisible":
                print("Your invisibility allows you to sneak past a sleeping dragon and find its treasure hoard. You win!")
            else:
                print("The fairies don't understand your choice. They fly away, leaving you lost in the forest. Game over!")
        
        elif path == "shadow":
            print("The shadowy trail leads you to a mysterious cave...")
            
            cave_choice = input("Do you enter the cave or turn back? (enter/back) ").lower()
            
            if cave_choice == "enter":
                print("Inside the cave, you find an ancient wizard who teaches you powerful spells. You become the new guardian of the forest. You win!")
            elif cave_choice == "back":
                print("As you turn back, you stumble upon a group of friendly elves who guide you to safety. You've survived the adventure!")
            else:
                print("Your indecision attracts the attention of forest spirits. They turn you into a tree. Game over!")
        
        else:
            print("You wander off the path and get lost in the forest. Game over!")
    
    else:
        print("Maybe next time you'll be brave enough for this magical adventure. Farewell!")

# Start the game
play_game()