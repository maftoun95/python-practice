import random
class Human(object):
  def __init__(self, clan):
    print 'New Human!!!'
    self.health = 100
    self.clan = clan
    self.strength = 3
    self.intelligence = 3
    self.stealth = 3
  def taunt(self):
    print "You want a piece of me?"
  def attack(self):
    self.taunt()
                                 # use the random module to generate a number when we attack
    luck = round(random.random() * 100)
    if(luck > 50):
      if(luck * self.stealth > 150):
        print 'attacking!'
        return True
      else:
        print 'attack failed'
        return False
    else:
      self.health -= self.strength 
      print "attack failed"
      return False

jimbo = Human('jimdawg')
jimbo.attack()
print '-'*25
class Wizard(Human):
    def __init__(self, clan):
        super(Wizard, self).__init__()   # use super to call the Human __init__ method
        self.intelligence = 10           # every wizard starts off with 10 intelligence
    def heal(self):
        self.health += 10
        print self.health

marko = Wizard()
marko.attack()
marko.taunt()
marko.heal()
