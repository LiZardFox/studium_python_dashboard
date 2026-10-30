from dataclasses import dataclass

from datetime import date

from study_dash.dto.grade import GradeDTO
from study_dash.dto.semester import SemesterDTO
from study_dash.dto.enrollment import EnrollmentDTO
from study_dash.entity import Student

@dataclass
class OverviewDTO:
    """
    Data transfer object for the Dashboard Overview.
    Holds Information about the logged in student, their average grade, the end of the next module, 
    their current enrollment and all other relevant information.
    """

    average_grade: GradeDTO
    student: Student
    next_modul_end: date
    enrollment: EnrollmentDTO
    enrollments: list[EnrollmentDTO]
    grades: list[GradeDTO]
    semesters: list[SemesterDTO]