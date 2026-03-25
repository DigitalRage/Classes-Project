from pet import Pet
from food import Food
from time_system import GameTime
from utils import clear_screen, get_int

import json
import os

VALID_SPECIES = ["Dog", "Cat", "Bird", "Fish", "Hamster"]

class GameManager:
    def __init__(self):
        self.pets = []
        self.active_pet = None
        self.time = GameTime()
        self.food_options = [
            Food("Basic Kibble", 20, 5),
            Food("Premium Food", 30, 15),
            Food("Treat", 10, 25),
            Food("Home-cooked Meal", 35, 20)
        ]

    def display_header(self):
        print("=====================================")
        print("🐾 VIRTUAL PET SIMULATOR 🐾")
        print("=====================================")
        if self.active_pet:
            print(f"Current Pet: {self.active_pet.name} ({self.active_pet.species})")
        else:
            print("No active pet selected.")
        print(f"Time: {self.time.get_time_string()}")
        print("=====================================\n")

    def require_pet(self):
        if not self.active_pet:
            print("⚠️ You need to create a pet first!")
            input("Press Enter to continue...")
            return False
        return True

    def feeding_menu(self):
        if not self.require_pet():
            return
        clear_screen()
        print("🍎 FEEDING MENU 🍎\n")
        for i, food in enumerate(self.food_options, start=1):
            print(f"[{i}] {food.name} - Hunger +{food.hunger_value}, Happiness +{food.happiness_value}")
        print("[B] Back\n")
        choice = input("Choose food: ")
        if choice.lower() == "b":
            return
        if not choice.isdigit():
            print("Invalid choice.")
            input("Press Enter to continue...")
            return
        choice = int(choice)
        if not (1 <= choice <= len(self.food_options)):
            print("Invalid choice.")
            input("Press Enter to continue...")
            return
        food = self.food_options[choice - 1]
        print(self.active_pet.feed(food))
        self.time.advance(1)
        event = self.active_pet.random_event()
        if event:
            print(event)
        input("Press Enter to continue...")

    def play_with_pet(self):
        if not self.require_pet():
            return
        result = self.active_pet.play()
        print(result)
        if "too tired" not in result:
            self.time.advance(1)
            event = self.active_pet.random_event()
            if event:
                print(event)
        input("Press Enter to continue...")

    def put_pet_to_sleep(self):
        if not self.require_pet():
            return
        result = self.active_pet.sleep()
        print(result)
        if "not tired" not in result:
            self.time.advance(2)
        input("Press Enter to continue...")

    def check_status(self):
        if not self.require_pet():
            return
        print(self.active_pet.get_status())
        input("\nPress Enter to continue...")

    def pet_management_menu(self):
        clear_screen()
        print("🐕 PET MANAGEMENT 🐕\n")
        print("[1] View Pets")
        print("[2] Create New Pet")
        print("[3] Switch Active Pet")
        print("[4] Release Pet")
        print("[B] Back\n")
        choice = input("Enter choice: ")
        if choice == "1":
            if not self.pets:
                print("No pets created yet.")
            else:
                for i, pet in enumerate(self.pets, start=1):
                    print(f"[{i}] {pet.name} ({pet.species})")
            input("\nPress Enter to continue...")
        elif choice == "2":
            name = input("Pet Name: ")
            print("Available Species:")
            for i, s in enumerate(VALID_SPECIES, start=1):
                print(f"[{i}] {s}")
            species_index = get_int("Choose species: ", 1, len(VALID_SPECIES))
            species = VALID_SPECIES[species_index - 1]
            new_pet = Pet(name, species)
            self.pets.append(new_pet)
            self.active_pet = new_pet
            print("Pet created!")
            input("Press Enter...")
        elif choice == "3":
            if not self.pets:
                print("No pets to switch to.")
                input("Press Enter...")
                return
            for i, pet in enumerate(self.pets, start=1):
                print(f"[{i}] {pet.name} ({pet.species})")
            index = get_int("Select pet: ", 1, len(self.pets))
            self.active_pet = self.pets[index - 1]
        elif choice == "4":
            if not self.pets:
                print("No pets to release.")
                input("Press Enter...")
                return
            if len(self.pets) == 1:
                print("⚠️ You cannot release your only pet!")
                input("Press Enter...")
                return
            for i, pet in enumerate(self.pets, start=1):
                print(f"[{i}] {pet.name} ({pet.species})")
            index = get_int("Select pet to release: ", 1, len(self.pets))
            released = self.pets.pop(index - 1)
            if self.active_pet == released:
                self.active_pet = self.pets[0] if self.pets else None

    def save_game(self):
        if not self.pets:
            print("No pets to save.")
            input("Press Enter...")
            return
        data = {
            "pets": [pet.__dict__ for pet in self.pets],
            "active_index": self.pets.index(self.active_pet) if self.active_pet in self.pets else None,
            "time": {"day": self.time.day, "hour": self.time.hour}
        }
        with open("/workspaces/Classes-Project/save.json", "w") as f:
            json.dump(data, f, indent=4)
        print("Game saved!")
        input("Press Enter...")

    def load_game(self):
        if not os.path.exists("save.json"):
            print("No save file found.")
            input("Press Enter...")
            return
        try:
            with open("save.json", "r") as f:
                data = json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            print("⚠️ Save file is missing or corrupted.")
            input("Press Enter...")
            return
        self.pets = []
        for pet_data in data.get("pets", []):
            pet = Pet(pet_data.get("name", "Unknown"), pet_data.get("species", "Unknown"))
            pet.__dict__.update(pet_data)
            pet.clamp()
            self.pets.append(pet)
        active_index = data.get("active_index")
        if active_index is not None and 0 <= active_index < len(self.pets):
            self.active_pet = self.pets[active_index]
        else:
            self.active_pet = self.pets[0] if self.pets else None
        time_data = data.get("time", {})
        self.time.day = time_data.get("day", 1)
        self.time.hour = time_data.get("hour", 8)
        print("Game loaded!")
        input("Press Enter...")
