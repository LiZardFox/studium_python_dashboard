from .repository import Repository
from study_dash.entity import Program

class ProgramRepository(Repository[Program]):
    """
    Repository Class for a program.
    Extends the Repository class.
    """
    @property
    def _table_name(self):
        return "program"

    def _init_entity(self, data: dict):
        """
        Initializes a Program entity from the data dictionary.
        """
        return Program(
            id=data['id'],
            name=data['name'],
        )