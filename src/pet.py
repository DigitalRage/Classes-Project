import random

class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.age = 0
        self.level = 1
        self.health = 100
        self.hunger = 50
        self.happiness = 50
        self.energy = 50
        self.skills = []
        self.alive = True

    def clamp(self):
        for attr in ["health", "hunger", "happiness", "energy"]:
            value = getattr(self, attr)
            if not isinstance(value, (int, float)):
                setattr(self, attr, 0)
            else:
                setattr(self, attr, max(0, min(100, value)))

    def feed(self, food):
        self.hunger += food.hunger_value
        self.happiness += food.happiness_value
        self.energy -= 5
        self.clamp()
        return f"{self.name} enjoyed the {food.name}!"

    def play(self):
        if self.energy < 20:
            return f"{self.name} is too tired to play!"
        self.happiness += 15
        self.energy -= 20
        self.hunger -= 10
        self.clamp()
        return f"You played with {self.name}!"

    def sleep(self):
        if self.energy > 90:
            return f"{self.name} is not tired right now."
        self.energy += 40
        self.hunger -= 15
        self.clamp()
        return f"{self.name} took a nap."

    def update_health(self):
        if self.hunger < 20 or self.energy < 20 or self.happiness < 20:
            self.health -= 10
        else:
            self.health += 2
        self.clamp()

    def random_event(self):
        event = random.choice(["toy", "sick", "none"])
        if event == "toy":
            self.happiness += 10
            self.clamp()
            return f"🎉 {self.name} found a toy! (+10 Happiness)"
        elif event == "sick":
            self.health -= 15
            self.clamp()
            return f"⚠️ {self.name} got sick! (-15 Health)"
        return None

    def get_status(self):
        return (
            f"Name: {self.name}\n"
            f"Species: {self.species}\n"
            f"Age: {self.age} months\n"
            f"Level: {self.level}\n"
            f"Health: {self.health}%\n"
            f"Hunger: {self.hunger}%\n"
            f"Happiness: {self.happiness}%\n"
            f"Energy: {self.energy}%\n"
            f"Skills: {', '.join(self.skills) if self.skills else 'None'}"
        )
