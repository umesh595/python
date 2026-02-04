class Engine:
    def start(self):
        print("Engine started")
class Car(Engine):
    pass
c = Car()
c.start()
class Engine:
    def start(self):
        print("Engine started")
class Car:
    def __init__(self):
        self.engine = Engine()
    def drive(self):
        self.engine.start()
        print("Car is moving")
c = Car()
c.drive()