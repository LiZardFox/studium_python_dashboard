from dataclasses import dataclass;
from .entity import Entity

@dataclass
class ProgramModule(Entity):
    """
    Entity Class for an program-module.
    Connects a module with a program.
    Has a sort property to sort the modules in a program.
    """
    program_id: int
    module_id: int
    sort: float