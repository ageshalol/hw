class Student:
    def __init__(self, name, direction):
        self.name = name
        self.direction = direction
        self.books = []
        self.knowledge = 0
        self.is_ready_to_work = False
        self.languages = {}

    def read_book(self, book_name):
        self.books.append(book_name)
        self.__add_points(100)

    def do_homework(self):
        self.__add_points(10)

    def do_project(self):
        self.__add_points(50)

    def __add_points(self, points):
        self.knowledge += points
        if self.knowledge >= 1000:
            print("Этот студент готов к работе")
            self.is_ready_to_work = True
            
    def learn_new_language(self, language, amount_learned):
        if amount_learned < 1 or amount_learned > 100:
            raise ValueError("Неверное количество изученного языка")
        self.languages[language] = amount_learned
        
lol = Student("Lol", "Computer Science")
lol.read_book("Введение Python")
lol.do_homework()
lol.learn_new_language("Java", 50)
lol.learn_new_language("JavaScript", 80)
lol.do_project()
print(lol.books)
print(lol.languages)
print(lol.knowledge)
print(lol.is_ready_to_work)  