# 1
class Student:

    school_name = "Najot Ta'lim"
    country = "Uzbekistan"


    def __init__(self, fullname, age, course, grade):
        self.fullname = fullname
        self.age = age
        self.course = course
        self.grade = grade


    def show_info(self):
        print(f"""
Fullname: {self.fullname}
Age: {self.age}
Course: {self.course}
Grade: {self.grade}
School: {Student.school_name}
Country: {Student.country}
""")


    def change_grade(self, new_grade):
        self.grade = new_grade
        print(f"{self.fullname} ning yangi grade qiymati: {self.grade}")



student1 = Student("Ali Valiyev", 20, "Python", 85)
student2 = Student("Sardor Karimov", 22, "Frontend", 90)
student3 = Student("Madina Islomova", 19, "Backend", 88)


student1.show_info()
student2.show_info()
student3.show_info()


student1.change_grade(95)


student1.show_info()


Student.school_name = "PDP Academy"

print(" School nomi o'zgargandan keyin")


student1.show_info()
student2.show_info()
student3.show_info()


# 2
class Car:

    wheels = 4
    country = "Germany"


    def __init__(self, brand, color, price, speed):
        self.brand = brand
        self.color = color
        self.price = price
        self.speed = speed


    def show_car(self):
        print(f"""
Brand: {self.brand}
Color: {self.color}
Price: {self.price}$
Speed: {self.speed} km/h
Wheels: {Car.wheels}
Country: {Car.country}
""")


    def change_color(self, new_color):
        self.color = new_color
        print(f"{self.brand} ning yangi rangi: {self.color}")


    def increase_speed(self, km):
        self.speed += km
        print(f"{self.brand} ning yangi tezligi: {self.speed} km/h")



car1 = Car("BMW", "Black", 45000, 220)
car2 = Car("Mercedes", "White", 55000, 240)

print(" O'zgarishdan OLDIN")
car1.show_car()
car2.show_car()


car1.change_color("Red")
car1.increase_speed(30)

car2.change_color("Blue")
car2.increase_speed(20)

print(" O'zgarishdan KEYIN ")
car1.show_car()
car2.show_car()


# 3
class Phone:

    factory = "China"
    charger_type = "Type-C"

    # Constructor
    def __init__(self, brand, model, memory, price):
        self.brand = brand
        self.model = model
        self.memory = memory
        self.price = price


    def show_phone(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Memory: {self.memory} GB")
        print(f"Price: ${self.price}")
        print(f"Factory: {Phone.factory}")
        print(f"Charger Type: {Phone.charger_type}")
        print("-" * 30)


    def change_price(self, new_price):
        self.price = new_price


    def upgrade_memory(self, new_memory):
        self.memory = new_memory



phone1 = Phone("Samsung", "S24", 256, 1200)
phone2 = Phone("iPhone", "15 Pro", 512, 1500)
phone3 = Phone("Xiaomi", "Redmi Note 13", 128, 400)


print("Dastlabki telefonlar:")
phone1.show_phone()
phone2.show_phone()
phone3.show_phone()


phone1.change_price(1100)
phone1.upgrade_memory(512)

phone2.change_price(1400)
phone2.upgrade_memory(1024)

phone3.change_price(450)
phone3.upgrade_memory(256)


print("Yangilangan telefonlar:")
phone1.show_phone()
phone2.show_phone()
phone3.show_phone()
