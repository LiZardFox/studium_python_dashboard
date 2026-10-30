from abc import ABC
from dataclasses import dataclass

@dataclass
class Entity(ABC):
    """
    Abstract Base Class for all entities.
    Holds the id of the entity.
    """
    id: int