from dataclasses import dataclass
from .entity import Entity
from datetime import date


@dataclass
class Attempt(Entity):
    """
    Entity Class for an attempt.
    Associated with an enrollment and an evaluation.
    Holds the date of the attempt, and optionally the score and the grade.
    """
    enrollment_id: int
    evaluation_id: int
    date_of_attempt: date
    score:  int | None
    grade: float | None

    def graded(self) -> bool:
        return self.score is not None and self.grade is not None

    def passed(self) -> bool:
        return self.graded() and self.grade < 5.0                                                                 