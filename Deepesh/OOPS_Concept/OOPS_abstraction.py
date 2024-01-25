# abstraction

# when we defined any method in one class and impliment in some other class then it is known as abtraction

class animal:
    def animal_voice(self):
        pass

class dog(animal):
    def animal_voice(self):
        print("Barking")

class Lion(animal):

    def animal_voice(self):
        print("Roar")