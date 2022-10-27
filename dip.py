"""
DIP(Dependency Inversion Principle) - 의존성 역전 법칙
 - 부모 클래스는 자식 클래스의 구현에 의존해서는 안됨
 - 자식 클래스 코드 변경 또는 자식 클래스 변경 시, 부모 클래스 코드를 변경해야 하는 상황을 만들면 안됨
 - 자식 클래스에서 부모 클래스 수준에서 정의한 추상 타입에 의존할 필요가 있음
"""

#Bad Example
class BubbleSort:
    def bubble_sort(self):
        pass

class SortManager:
    def __init__(self):
        self.sort_method = BubbleSort()

    def begin_sort(self):
        self.sort_method.bubble_sort()

# 이때 bubblesort 클래스의 메서드 이름이 변경되면 치명적인 에러가 발생한다.

#Good Example

class SortManager:
    def __init__(self, sort_method):
        self.set_sort_method(sort_method)

    def set_sort_method(self, sort_method):
        self.sort_method = sort_method

    def begin_sort(self):
        self.sort_method.sort()

class BubbleSort:
    def sort(self):
        print('bubble sort')
        pass

class QuickSort:
    def sort(self):
        print('quick sort')
        pass

class SelectionSort:
    def sort(self):
        print('selection sort')
        pass

bubble_sort = BubbleSort()
quick_sort = QuickSort()
selection_sort = SelectionSort()

s1 = SortManager(bubble_sort)
s1.begin_sort()

s2 = SortManager(quick_sort)
s2.begin_sort()

s3 = SortManager(selection_sort)
s3.begin_sort()