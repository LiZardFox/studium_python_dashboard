from dataclasses import dataclass
from .entity import Entity

@dataclass
class Student(Entity):
    """
    Entity Class for an student.
    Holds the name of the student, the matriculation number and the password.
    """
    first_name: str
    last_name: str
    matrikel_nr: str
    password: str