from dataclasses import dataclass
from study_dash.entity import Module

@dataclass
class GradeDTO:
    """
    Data transfer object for a grade.
    Holds Information about the grade, its color and the associated module.
    """

    color: str
    grade: float
    module: Module|None = None