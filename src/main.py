from game_manager import GameManager
from utils import clear_screen

def main():
    game = GameManager()
    while True:
        clear_screen()
        game.display_header()
        print("🎮 ACTIONS:")
        print("[1] Feed Pet")
        print("[2] Play with Pet")
        print("[3] Put Pet to Sleep")
        print("[4] Check Status")
        print("[5] Pet Management")
        print("[6] Save Game")
        print("[7] Load Game")
        print("[8] Quit\n")
        choice = input("Enter your choice (1-8): ")
        if choice == "1":
            game.feeding_menu()
        elif choice == "2":
            game.play_with_pet()
        elif choice == "3":
            game.put_pet_to_sleep()
        elif choice == "4":
            game.check_status()
        elif choice == "5":
            game.pet_management_menu()
        elif choice == "6":
            game.save_game()
        elif choice == "7":
            game.load_game()
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()
