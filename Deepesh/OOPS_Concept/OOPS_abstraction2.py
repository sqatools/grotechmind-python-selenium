# abstraction
from OOPS_abstraction import animal

# when we defined any method in one class and impliment in some other class then it is known as abtraction

class cat(animal):

    def animal_voice(self):
        print("Meow")


if __name__ == "__main__":
    obj = cat()
    obj.animal_voice()