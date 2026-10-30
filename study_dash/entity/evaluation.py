from dataclasses import dataclass
from enum import Enum
from .entity import Entity


class EvaluationType(Enum):
    """
    Enum for the different types of evaluations.
    """
    EXAM = 'exam'
    PORTFOLIO = 'portfolio'
    WORKBOOK = 'workbook'


@dataclass
class Evaluation(Entity):
    """
    Entity Class for an evaluation.
    Associated with a module.
    Holds the id of the module, the type of evaluation, the weight for the final module grade, the maximum score and number of attempts allowed.
    """
    module_id: int
    type: EvaluationType
    weight: float
    max_score: int = 100
    max_attempt: int = 3
