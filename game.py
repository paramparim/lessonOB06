import random

class Game:
    def __init__(self, player, computer):
        self.player = player
        self.computer = computer

    def start(self):
        while self.player.is_alive() and self.computer.is_alive():
            if random.choice([True, False]):
                self.player.attack(self.computer)
            else:
                self.computer.attack(self.player)

            print(f"{self.player.name}: {self.player.health} здоровья")
            print(f"{self.computer.name}: {self.computer.health} здоровья")

        if self.player.is_alive():
            print(f"{self.player.name} побеждает!")
        else:
            print(f"{self.computer.name} побеждает!")