class Dog:
    def __init__(self, name, breed, sex, age):
        self.name  = name
        self.breed = breed
        self.sex   = sex
        self.age   = age


    def bark():
        return 'Woof!'


dog1 = Dog('Bob', "wer", "man", 4)

print(dog1.bark())

#????????????????????????????????????????????


class Dog:
    def __init__(self, nametest, breed, sex, age):
        self.name  = nametest
        self.breed = breed
        self.sex   = sex
        self.age   = age

    def bark(self, say):
        return say

apollo = Dog('Apollo', 'Dobermann', 'male', 4)

print(apollo.bark('Meow!'))
