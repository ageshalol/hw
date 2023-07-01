#hw 1
class Cow:
    def make_sound(self):
        return "Муу"

cow = Cow()
print(cow.make_sound())

#hw2
# class Cars:
#     def __init__(self, brand, model, year, odometer=0, type_of="", volume="", is_going=False):
#         self.brand = brand
#         self.model = model
#         self.year = year
#         self.odometer = 0
#         self.type_of = type_of
#         self.volume = volume
#         self.is_going = is_going
        
#     def info_about_car(self):
#         print(f"Brand: {self.brand} Model: {self.model} Year: {self.year}")
        
#     def car_is_going(self, km):
#         self.odometer += km
#         self.is_going = True
#         return self.odometer, self.is_going
        
#     def car_not_going(self):
#         self.is_going = False
#         return self.is_going

# car = Cars("Nissan", "Silvia s14", 2000)
# car.info_about_car()
# print(car.car_is_going(50))
# print(car.car_not_going())

#hw3
# class Airplane:
#     def init(self, make, model, year, max_speed):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.max_speed = max_speed
#         self.odometer = 0
#         self.is_flying = False

#     def take_off(self):
#         self.is_flying = True

#     def fly(self, distance):
#         if self.is_flying:
#             self.odometer += distance
#         else:
#             print("Ошибка: самолет не взлетел.")

#     def land(self):
#         self.is_flying = False

#     def info_about_fly(self):
#         if self.is_flying:
#             print("Самолет в полете.")
#         else:
#             print("Самолет на земле.")

#     def info_about_plane(self):
#         print("Марка: " + self.make)
#         print("Модель: " + self.model)
#         print("Год выпуска: " + str(self.year))
#         print("Максимальная скорость: " + str(self.max_speed))
#         print("Пробег: " + str(self.odometer) + " км")
#         print("Самолет в полете: " + str(self.is_flying))

#hw 4
# class Math:
#     def addition(self, a, b):
#         result = a + b
#         print(f"Результат: {a} + {b} = {result}")

#     def multiplication(self, a, b):
#         result = a * b
#         print(f"Результат: {a} * {b} = {result}")

#     def division(self, a, b):
#         if b != 0:
#             result = a / b
#             print(f"Результат: {a} / {b} = {result}")
#         else:
#             print("Ошибка: деление на ноль!")

#     def subtraction(self, a, b):
#         result = a - b
#         print(f"Результат: {a} - {b} = {result}")

# math = Math()
# math.addition(5, 10)
# math.multiplication(5, 10)  
# math.division(10, 5)  
# math.subtraction(10, 5)  