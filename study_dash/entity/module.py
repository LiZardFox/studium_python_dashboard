from dataclasses import dataclass;
from .entity import Entity


@dataclass
class Module(Entity):
    """
    Entity Class for a module.
    Holds the name of the module.
    """
    name: str