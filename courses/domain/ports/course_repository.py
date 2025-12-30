from abc import ABC, abstractmethod
from courses.domain.entities.course import Course

class CourseRepository(ABC):

    @abstractmethod
    def create(self, course: Course) -> Course:
        pass
    