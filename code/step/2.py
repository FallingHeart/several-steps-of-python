class Man:
    
    def __init__(self, name, chinese_name, age, height, weight):
        self.name = name
        self.chinese_name = chinese_name
        self.age = age
        self.height = height
        self.weight = weight

    def eat(self):
        self.weight = self.weight + 5
        print('After %s eats something, his weight comes to %d.' % (self.name,self.weight))

    def grown_up(self,year):
        self.age = self.age + year
        print('%d year later, the age of %s comes to %d.' % (year,self.name,self.age))

xiaoming = Man('Bob','小明',12,120,40)

print(xiaoming.weight)

this_year_age = xiaoming.age
print(this_year_age)

xiaoming.eat()

xiaoming.grown_up(5)