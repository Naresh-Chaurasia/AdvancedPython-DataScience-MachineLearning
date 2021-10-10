class Parrot:

    def fly(self):
        print("Parrot can fly")
    
    def swim(self):
        print("Parrot can't swim")


class Penguin(Parrot):

    def fly(self):
        print("Penguin can't fly")
    
# common interface
def flying_test(bird):
    bird.fly()


# instantiate objects
blu = Parrot()
peggy = Penguin()
peggy.swim()

# passing the object
#flying_test(blu)
# flying_test(peggy)
