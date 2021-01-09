class Person(object):
    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job

    def celebrate_birthday(self):
        self.age += 1

        if self.age >= 65:
            self.job = "Retired"

        return "Happy Birthday {}".format(str(self.name)


class Person(object):
    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job

    def celebrate_birthday(self):
        self.age = self.age + 1
        if self.age >= 65:
            self.job = "Retired"

        # DON"T PRINT YOU IDIOT
        return "Happy birthday {}!".format(self.name)