class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")
c1=MyClass()
print(c1.function())


class Robot:
    def introduce_self(self):
        print("my name is: " +self.name)
        print("my color is: " +self.color)
        

r1=Robot()
r1.name="Robo"
r1.color="red"


r2=Robot()
r2.name="Tom"
r2.color="Blue"


r1.introduce_self()
r2.introduce_self()