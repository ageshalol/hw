class Washer:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
        self.powder = 0
        self.is_work = False

    def __str__(self):
        return f"Brand: {self.brand} Color: {self.color} Powder: {self.powder} Is work: {self.is_work}"

    def start(self):
        if self.powder >= 20:
            self.powder -= 20
            self.is_work = True
            print("Стирка началась")
        else:
            print("Не хватает порошка")

    def refuel(self, amount):
        if amount <= 100:
            self.powder += amount
        else:
            print("В стиралку можно положить лишь 100 грамм порошка")

    def finish(self):
        self.is_work = False
        print("Стиральная машина отключена")

washing_machine = Washer("Iphon", "Black")
print(washing_machine)
washing_machine.start()
washing_machine.refuel(50)
washing_machine.refuel(150)
washing_machine.start()
washing_machine.finish()
print(washing_machine)