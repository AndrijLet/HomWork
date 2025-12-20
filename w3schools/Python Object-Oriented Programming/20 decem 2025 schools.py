# class Person:
#     def __init__(self, fname, lname):
#         self.fristname = fname
#         self.lastage = fname
#
#     def printname(self):
#         print(self.firstname, self.lastname)
#
# #Use the Person class to create an object, and then execute the printname method:
#
# x = Person("John", "Doe")
# x.printname()



'''функція super() для присвоєння свого значення в класі, перезапис також'''
class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def print_name(self):
        print(self.name)


class Student(Person):
    def __init__(self, name, surname, start_year):
        super().__init__(name, surname)
        self.start_year = start_year

    def welcome_message(self):
        return (
            f"Congratulations on your admission: "
            f"{self.name} {self.surname}, start year: {self.start_year}"
        )

    def calculate_course(self, current_year):
        """Вираховує поточний курс студента"""
        course = current_year - self.start_year + 1

        if 1 <= course <= 6:
            return f"Поточний курс: {course}"
        elif course > 6:
            return "Студент вже закінчив навчання"
        else:
            return "Навчання ще не розпочалося"


# Створення об’єкта
student_on = Student('Petro', 'LLL', 2022)

# Виклики
print(student_on.welcome_message())
print(student_on.calculate_course(2024))



# middlename функція приймає та назовні та виводить його разом назовні разом із привітанням
# додати функцію яка буде вираховувати на якому курсі студент

