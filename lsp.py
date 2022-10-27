"""
LSP(Liskov Substitution Principle) 리스코프 치환 법칙
자식클래스는 항상 부모클래스와 교체할 수 있다는 원칙
"""
from abc import *

class Character(metaclass=ABCMeta):
    def __init__(self, name='yourname', health_point=100, striking_power=3, defensive_power=3):
        self.name = name
        self.health_point = health_point
        self.striking_power = striking_power
        self.defensive_power = defensive_power

    def get_info(self):
        print(self.name, self.health_point, self.striking_power, self.defensive_power)

    @abstractmethod
    """
    추상메소드는 상속한 클래스에서 반드시 해당 추상메소드를 구현하도록 강제한다.
    상속받은 클래스에서 추상메소드를 구현하지 않더라도 import 시까지 에러는 발생하지 않는다. 하지만, 객체 생성 시 에러가 발생한다.
    또한, 추상클래스에서 추상메소드가 없으면 기본적인 클래스의 기능을 한다.
    """
    def attack(self):
        pass

    @abstractmethod
    def move(self):
        pass

    def eat(self):
        pass
