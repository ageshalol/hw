import random

class GTA:
    def __init__(self, character):
        if character in ['Майкл', 'Тревор', 'Франклин']:
            self.__character = character
            self.__health = 100
            self.__money = 100
            self.__satiety = 100
            self.__walk = 0
        else:
            print("Нету такого персонажа")
    
    def get_attributes(self):
        return f"Health: {self.__health}, Money: {self.__money}, Satiety: {self.__satiety}, Walk: {self.__walk}"
    
    def walk(self):
        self.__walk += 1
    
    def attack(self, damage):
        if damage >= 1 and damage <= 20:
            print("Ваш персонаж атаковал и сделал урон", damage)
        else:
            print("Вы не нанесли урон")
    
    def take_damage(self):
        damage = random.randint(0, 30)
        self.__health -= damage
        if self.__health <= 0:
            self.__money -= 10
            self.__health += 100
    
    def earn_money(self):
        self.__money += 100
     
gta_game = GTA("Майкл")
gta_game.walk() 
gta_game.attack(10)
gta_game.take_damage()
gta_game.earn_money()
print(gta_game.get_attributes())
