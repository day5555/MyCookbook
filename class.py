#!/usr/bin/python

class Parent:        # define parent class
   parentAttr = 100
   def __init__(self):
      print("Calling parent constructor")

   def parentMethod(self):
      print('Calling parent method')

   def setAttr(self, attr):
      Parent.parentAttr = attr

   def getAttr(self):
      print("Parent attribute :", Parent.parentAttr)

   def myOverride(selfs):
       print("OVerrride von Parent")

class Child(Parent): # define child class
   __secret = 0
   def __init__(self):
       # Parent.__init__(self)
       print("Calling child constructor")

   def childMethod(self):
      print('Calling child method')

   def myOverride(selfs):
       print("OVerrride von CHILDREN")

   # Overloading Operators
   def __str__(self):
       return  ('parentAttr String: ' + str(self.parentAttr))

   def __add__(self, other):
       return (self.parentAttr + other.parentAttr)


c = Child()          # instance of child
c.childMethod()      # child calls its method
c.parentMethod()     # calls parent's method
c.setAttr(200)       # again call parent's method
c.getAttr()          # again call parent's method
c.myOverride()       # override the parent method and use the children methode
print(c)
print("Addition: ", c + c)  # ADD Operator
// print(c.__secret) # nicht direkt von aussen sichtbar
