from datetime import date
from dataclasses import dataclass;
from .entity import Entity

@dataclass
class Enrollment(Entity):
    """
    Entity Class for an enrollment.
    Associated with an a student, and a program.
    Holds the id of the program, the id of the student, the number of semesters, the start and end date of the enrollment.
    Optionally target grade and target end date can be specified.
    """
    program_id: int
    student_id: int
    semesters: int
    start_date: date
    end_date: date
    target_grade: float | None = None
    target_end_date: date  | None = None