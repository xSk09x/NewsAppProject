from random import randint
class car:
    pass

class fire_car:
    pass

car1 = car()
car2 = fire_car()

# result = isinstance(car1,car)
# print(result)
class buterbrod:
    xleb = 2
    colbasa = 1
    
    def __init__(self, cucumbers, salat, cheese, salami):
        self.cucumbers = cucumbers
        self.salat = salat
        self.cheese = cheese
        self.salami = salami

    def fall(self,):
        result = randint(1,4)
        if result == 1:
            print("Упал огурцом вниз")
        elif result == 2:
            print("Упал салатом вниз")
        elif result == 3:
            print("Упал сыром вниз")
        else:
            print("Упал салями вниз")
sandwich = buterbrod(2,1,1,2)
sandwich.fall()

print(123)