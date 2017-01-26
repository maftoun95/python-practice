class Animal(object):
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.fart = "loud"
    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -= 5
        return self
    def displayHealth(self):
        print self.name, self.health
        return self

animal = Animal('ladsjfklfasjdk')
animal.walk().walk().walk().run().run().displayHealth()

class Dog(Animal):
    def __init__(self):
        self.health = 150
    def pet(self):
        self.health += 5
        return self
jojo = Dog()
jojo.fart

class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name)
        self.health = 170
    def fly(self):
        self.health -= 10
        return self
    def displayHealth(self):
        print 'this is a dragon!'
        super(Dragon, self).displayHealth()

fyordor = Dragon('fyordor')
fyordor.walk().walk().walk().run().run().fly().fly().displayHealth()
