class FlyBehavior:
    def fly(self):
        print("Flying")
class NoFlyBehavior:
    def fly(self):
        print("Cannot fly")
class Bird:
    def __init__(self, fly_behavior):
        self.fly_behavior = fly_behavior
    def fly(self):
        self.fly_behavior.fly()