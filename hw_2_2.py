# class SlotMachine:
#     def __init__(self, name):
#         self.name = name
#         self.user_balance = 100
#         self.game_balance = 0
        
#     def info(self):
#         return f"Name: {self.name} User balance: {self.user_balance} Game balance: {self.game_balance}"
    
#     def top_up_balance(self, amount):
#         if amount > 100:
#             print("Вы можете пополнить до 100$")
#             return False
#         else:
#             self.user_balance -= amount
#             self.game_balance += amount
    
#     def balance_up(self, amount):
#         if amount > 100:
#             print("Вы можете пополнить до 100$")
#             return False
#         else:
#             self.user_balance += amount
            
    
#     def game(self):
#         import random
#         number = random.randint(1, 10)
#         for i in range(5):
#             guess = int(input("Угадай число от 1 до 10:"))
#             if guess == number:
#                 print("Ты выиграл!")
#             self.game_balance += 50
#             return
#         else:
#              self.game_balance -= 10
#              print("ты приграл!")
#              print("Вы потеряли все попытки!")
        
#     def conclusion_money(self, amount):
#         if amount < 50:
#             print("Вывести можно от 50$")
#             return False
#         else:
#             self.game_balance -= amount
#             self.balance_up(amount)
 
#     def main(self):
#         while True:
#             print("Команды игрового автомата:")
#             print("1 - Информация об игроке")
#             print("2 - Пополнение игрового баланса")
#             print("3 - Игра")
#             print("4 - Вывод игровых денег")

#             choice = input("Выберите команду (1-4): ")

#             if choice == "1":
#                 self.info()
#             elif choice == "2":
#                 self.top_up_balance()
#             elif choice == "3":
#                 self.game()
#             elif choice == "4":
#                 self.conclusion_money()
#             else:
#                 print("Неверный выбор команды. Попробуйте еще раз.")

# name = input("Введите имя игрока: ")
# slot_machine = SlotMachine(name)
# slot_machine.main()