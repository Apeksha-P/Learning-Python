class person:
    def __init__(self,a,b,c):
        self.name = a
        self.age = b
        self.gendr = c
    def talk(self):
        print("I'm ",self.name)
    def vote(self):
        if self.age<18:
            print("Not eligible to vote")
        else :
            print("Eligible to vote")

obj1 = person("Apeksha",22,"Female")
obj2 = person("Pavithri",21,"Female")
person.talk(obj1)
person.vote(obj1)
person.talk(obj2)
person.vote(obj2)
