class First:
    def getClassname(self):
        return "First"

    def getLetter(self):
        return "A"

class Second:
    def getClassname(self):
        return "Second"

    def getLetter(self):
        return "B"

first_object = First()
second_object = Second()

print(first_object.getClassname())  
print(second_object.getClassname())  
print(first_object.getLetter())    
print(second_object.getLetter())    