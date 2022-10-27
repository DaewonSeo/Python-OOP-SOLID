"""
ISP(Interface Segregation Principle) - 인터페이스 분리 원칙
클래스에서 사용하지 않는(상관없는) 메서드는 분리해야 한다.
"""



# # Bad Example
# class Elf(Character):
#     def attack(self):
#         print('Practice the black art')

#     def move(self):
#         print('fly')

#     def eat(self): # Elf class에는 불필요한 메소드로 추상메소드로 구현하면 안된다.
#         print('no eat')


# class Human(Charactor):
#     def attack(self):
#         print('Plunge a knife')

#     def move(self):
#         print('run')

#     def eat(self):
#         print('eat food')


# class Character(metaclass=ABCMeta):
#     @abstractmethod
#     def attack(self):
#         pass

#     @abstractmethod
#     def move(self):
#         pass

# class Elf(Character):
#     def attack(self):
#         print('~~~')

#     def move(self):
#         print('~~~')

# class Human(Character):
#     def attack(self):
#         print('~~~')

#     def move(self):
#         print('~~~')

#     def eat(self): # 특정 method가 필요할 경우 다음과 같이 만들어주면 된다.
#         print('~~~')

from abc import *

class AttackingWay(metaclass=ABCMeta):
    @abstractmethod
    def attack(self):
        pass

class MovingWay(metaclass=ABCMeta):
    @abstractmethod
    def move(self):
        pass

class EatingWay(metaclass=ABCMeta):
    @abstractmethod
    def eat(self):
        pass

class UsingKnife(metaclass=ABCMeta):
    @abstractmethod
    def use_knife(self):
        pass

class UsingWizard(metaclass=ABCMeta):
    @abstractmethod
    def use_wizard(self):
        pass

class Elf(AttackingWay, MovingWay, UsingWizard):
    def attack(self):
        print('Practice the black art')

    def move(self):
        print('fly')

    def use_wizard(self):
        print('마법을 사용하다.')

class Human(AttackingWay, MovingWay, EatingWay, UsingKnife):
    def attack(self):
        print('plunge a knife')

    def move(self):
        print('run')

    def eat(self):
        print('eat foods')

    def use_knife(self):
        print('칼로 찌른다.')




e = Elf()
h = Human()

e.move()
e.use_wizard()

h.move()
h.eat()
h.use_knife()
