from dataclasses import dataclass, field

from .module import ModuleDTO
@dataclass
class SemesterDTO:
    """
    Data transfer object for a semester.
    Holds Information about all the modules in that semester and its number.
    The modules are stored as a list of ModuleDTOs.
    """

    semester_nr: int
    modules: list[ModuleDTO] = field(default_factory=list)
    def add_module(self, module: ModuleDTO):
        self.modules.append(module)
        return self