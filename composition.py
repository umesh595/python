class Engine:
    def __init__(self, horsepower):
        self._horsepower = horsepower
class Car:
    def __init__(self, horsepower):
        self.__engine = Engine(horsepower)  
    def get_power(self):
        return self.__engine._horsepower
car = Car(150)
print(car.get_power())  