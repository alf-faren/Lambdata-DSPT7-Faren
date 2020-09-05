from pdb import set_trace as breakpoint


class Dog():
    def __init__(self, name, age, breed, housebroke=True):
        self.name = name
        self.age = age
        self.housebroke = housebroke
        self.breed = breed

    def bark(self):
        print(f'{self.name} likes to bark!')


class Beagle(Dog):
    def __init__(self, name, age, housebroke=True, barks_alot=True):
        super().__init__(name, age, housebroke)

    def bark(self):
        if self.barks_alot is True:
            print(f'{self.name} likes to bark!')
        else self.barks_alot == barks_alot
        print(f'{self.name} is a quiet one!')


if __name__ == "__main__":

    lucky = Dog("Lucky", 3, "Labrador")
    spike = Dog("Spike", 7, "Boxer")
    breakpoint()
