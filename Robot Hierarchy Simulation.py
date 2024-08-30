from abc import abstractmethod

class Robot:
    def __init__(self,name,battery_level):
        self.__name=name
        self.__battery_level=battery_level
    def status(self):
        print(f"Robot's name : {self.__name:<10} , Robot's Battery level : {self.__battery_level}%")
    def get_battery_level(self):
        return self.__battery_level
    def get_name(self):
        return self.__name
    def set_battery_level(self,battery_level):
        if(battery_level>0):
            self.__battery_level=battery_level
        else:
            print("Battery level must be positive")
    @abstractmethod
    def move(self):
        pass
class GroundRobot(Robot):
    def __init__(self,name,battery_level,wheels):
        super().__init__(name,battery_level)
        self.wheels=wheels
    def move(self):
        print(f"{self.get_name():<5} Robot is moving on {self.wheels} wheels")
class AerialRobot(Robot):
    def __init__(self,name,battery_level,rotors):
        super().__init__(name,battery_level)
        self.rotors=rotors
    def move(self):
        print(f"{self.get_name():<5} Robot is flying with {self.rotors} rotors")
class fleet_managment:
    def __init__(self):
        self.__fleet=set()
    def add_bot(self,bot):
        if(isinstance(bot,Robot)):
            self.__fleet.add(bot)
        else:
            print("Not of type Robot")    
    def move_bots(self):
        for robot in self.__fleet:
            robot.move()
        print()
    def status_bots(self):
        for robot in self.__fleet:
            robot.status()
        print()
r=GroundRobot("Elephanto",90,8)
a=AerialRobot("Falconer",56,5)
fleet=fleet_managment()
fleet.add_bot(r)
fleet.add_bot(r)
r.set_battery_level(95)
fleet.add_bot(a)
fleet.status_bots()
fleet.move_bots()