FUNCTION main_menu():
    LOOP forever:
        CLEAR screen
        DISPLAY current pet name and current time
        DISPLAY pet status

        DISPLAY:
            [1] Feed Pet
            [2] Play with Pet
            [3] Put Pet to Sleep
            [4] Check Status
            [5] Pet Management
            [6] Save Game
            [7] Load Game
            [8] Quit

        choice = get_valid_input()

        IF choice == 1:
            CALL feeding_menu()
        ELSE IF choice == 2:
            CALL active_pet.play()
            CALL time.advance(1)
            CALL active_pet.random_event()
        ELSE IF choice == 3:
            CALL active_pet.sleep()
            CALL time.advance(2)
        ELSE IF choice == 4:
            DISPLAY active_pet.get_status()
        ELSE IF choice == 5:
            CALL pet_management_menu()
        ELSE IF choice == 6:
            CALL save_game()
        ELSE IF choice == 7:
            CALL load_game()
        ELSE IF choice == 8:
            BREAK LOOP
        ELSE:
            DISPLAY "Invalid choice"
