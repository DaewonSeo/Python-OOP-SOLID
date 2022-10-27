"""
OCP(Open Closed Principle) - 개방-폐쇄 원칙
확장에는 열려있으나, 수정에는 닫혀있어야 함
예. 캐릭터 클래스를 만들 때 캐릭터 마다 다른 스탯과 특성을 가져아하는데 이는
부모 클래스를 수정할 필요 없이(수정-X) 상속받아서 자식클래스에서 수정하면(확장-O) 된다는 원칙.
"""

# Bad Example
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

# class AreaCalculator:
#     def __init__(self, shapes):
#         self.shapes = shapes

#     def total_area(self):
#         total = 0
#         for shape in self.shapes:
#             total += shape.width * shape.height
#         return total

# shapes = [Rectangle(2, 3), Rectangle(1, 6)]
# calculator = AreaCalculator(shapes)
# print(f"The total area is: {calculator.total_area()}")


# Good Example
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class AreaCalculator:
    """
    다른 도형을 확장하기 위해서, AreaCalculator를 수정할 필요 없이 다른 class를 정의해서 수정하면 됨.
    """
    def __init__(self, shapes):
        self.shapes = shapes

    def total_area(self):
        total = 0
        for shape in self.shapes:
            total += shape.area()
        return total

shapes = [Rectangle(1, 6), Rectangle(2, 3), Circle(5)]
calculator = AreaCalculator(shapes)

print(f"The total area is: {calculator.total_area()}")
