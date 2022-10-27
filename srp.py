"""
SRP(Single Responsibility Principle) - 단일 책임 원칙
클래스는 단 한개의 책임을 가져야 한다.
"""

# Bad Example
class StudentScoreAndCourseManager:
    def __init__(self):
        scores = {}
        courses = {}

    def get_score(self, student_name, course):
        pass

    def get_courses(self, studnet_name):
        pass

# Good Example
class ScoreManager:
    """
    각 클래스의 책임을 하나로 줄여서, 수정 시 미치는 영향이 없도록 함.
    """
    def __init__(self):
        scores = {}

    def get_scores(self, student_name, course):
        pass

class CourseManager():
    def __init__(self):
        courses = {}
    
    def get_courses(self, student_name):
        pass

