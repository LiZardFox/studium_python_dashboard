from dataclasses import dataclass;
from .entity import Entity


@dataclass
class Program(Entity):
    """
    Entity Class for an program.
    Holds the name of the program.
    """
    name: str