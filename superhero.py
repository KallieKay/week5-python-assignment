class Superhero:
    def __init__(self, name, secret_identity, power):
        self.name = name
        self.secret_identity = secret_identity
        self.power = power
        self.is_flying = False

    def reveal_identity(self):
        return f"The hero {self.name} is actually {self.secret_identity}!"

    def use_power(self):
        return f"{self.name} uses {self.power}!"

    def fly(self):
        if not self.is_flying:
            self.is_flying = True
            return f"{self.name} is now flying!"
        else:
            return f"{self.name} is already flying!"
    
    def stop_flying(self):
        if self.is_flying:
            self.is_flying = False
            return f"{self.name} has landed."
        else:
            return f"{self.name} wasn't flying."

class FlyingSuperhero(Superhero):
    def __init__(self, name, secret_identity, power, flight_speed):
        super().__init__(name, secret_identity, power)
        self.flight_speed = flight_speed

    def fly(self):
         return f"{self.name} flies at a speed of {self.flight_speed} mph!"

class AquaticSuperhero(Superhero):
    def __init__(self, name, secret_identity, power, water_speed):
        super().__init__(name, secret_identity, power)
        self.water_speed = water_speed

    def swim(self):
        return f"{self.name} swims at a speed of {self.water_speed} knots!"

# Instances of the classes
superman = FlyingSuperhero("Superman", "Clark Kent", "Super strength and flight", 1500)
aquaman = AquaticSuperhero("Aquaman", "Arthur Curry", "Control over the seas", 40)
flash = Superhero("Flash", "Barry Allen", "Super speed")

# Demonstrating methods
print(superman.reveal_identity())
print(superman.use_power())
print(superman.fly())
print(aquaman.swim())
print(flash.use_power())
print(flash.fly())
print(flash.stop_flying())

