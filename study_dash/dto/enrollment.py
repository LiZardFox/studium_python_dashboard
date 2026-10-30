from dataclasses import dataclass

from study_dash.entity import Enrollment, Program
@dataclass
class EnrollmentDTO:
    """
    Data transfer object for an enrollment.
    Holds Information about the enrollment and its associated program.
    """
    enrollment: Enrollment
    program: Program