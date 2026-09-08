class Dog :
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed
    def bark(self):
        print(f"{self.name},  says wolf !")

p1 = Dog("Luke" , "Bulldog")
p1.bark()


with open("diary.txt", "r") as f:
    f.write("Today I learnead about files")
with open("diary.txt" , "r") as f:
    content =f.read()
    print(content)
    