from dataclasses import dataclass
from study_dash.entity import Module

@dataclass
class ModuleDTO:
    """
    Data transfer object for a module.
    Holds Information about the module, and its grade if available.
    """

    module: Module
    grade: float|None