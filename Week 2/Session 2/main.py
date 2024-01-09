# Define the Character Class
class Character:
    def __init__(self, name , hp , power):
        self.name = name
        self.hp = hp
        self.power = power

    def is_alive(self):
        return self.hp > 0
    
    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
        print(f"{self.name} now has {self.hp} HP left.")

    def attack(self, other):
        if self.is_alive():
            damage = self.power
            other.take_damage(damage)
            print(f"{self.name} attacked {other.name} for {damage} Damage!")


class Mage(Character):
    def __init__(self, name , hp , power, spell):
        super().__init__(name , hp , power)
        self.spell = spell

    def cast_spell(self, other):
        if self.is_alive():
            damage = self.spell
            other.take_damage(damage)
            self.hp += damage

class Warrior(Character):
    def __init__(self, name , hp , power , defense):
        super().__init__(name , hp , power)
        self.defense = defense
        self.is_defending = False

    def defend(self):
        if self.is_alive():
            self.is_defending = True
            print(f"{self.name} is preparing to defend!")

    def take_damage(self, damage):
        if self.is_defending:
            damage -= self.defense
            if damage < 0:
                damage = 0
            self.is_defending = False
        super().take_damage(damage)
    

def play_turn(player1 , player2):
    print('-'*50)
    print(f"{player1.name}'s turn:")
    choice = input(f"For Attacking type 'a'. For using special move type 's':")
    if choice == 's' or choice == 'a':
        if isinstance(player1, Mage) and choice == 's':
            player1.cast_spell(player2)
        elif isinstance(player1 , Warrior) and choice == 's':
            player1.defend()
        else:
            player1.attack(player2)

def game_loop():
    Mike = Mage("Mage Mike", 100 , 10 , 20)
    Wendy = Warrior("Warrior Wendy", 120 , 12 , 8)

    while Mike.is_alive() and Wendy.is_alive():
        play_turn(Mike , Wendy)
        if Wendy.is_alive():
            play_turn(Wendy , Mike)
    
    print('-----Game Over-----')
    if Mike.is_alive():
        print(f"{Mike.name} Wins!")
    else:
        print(f'{Wendy.name} Wins!')


game_loop()