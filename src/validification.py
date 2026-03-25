FUNCTION get_valid_input(prompt):
    LOOP:
        TRY:
            user_input = int(input(prompt))
            RETURN user_input
        EXCEPT:
            DISPLAY "Invalid input. Please enter a number."
