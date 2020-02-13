class Person:
    def __init__(self, title = "Private First Class ", firstName = "Forrest", lastName = "Gump", age = 23):
        self.title = title
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        
    def greetInformal(self):
        print("Hello, ", self.firstName, "\b!")
        
    def greetFormal(self):
        print("Hello,", self.title, self.lastName, "\b!")
    
    def howOld(self):
        print(self.firstName, "is ", self.age, " years old!")
        
    def birthday(self):
        self.age += 1
        print("Happy Birthday, ", self.firstName, "\b! You are now ", self.age, " years old!")
        
title = input("What is your title? ")
firstName = input("What is your first name? ")
lastName = input("What is your last name? ")
age = input("How old are you? ")

you = Person(title, firstName, lastName, int(age))

you.greetInformal()
you.greetFormal()
you.howOld()
you.birthday()
you.howOld()

you.age -= 1
you.howOld()
