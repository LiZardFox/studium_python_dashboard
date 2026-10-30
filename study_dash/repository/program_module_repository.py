from .repository import Repository
from study_dash.entity import ProgramModule

class ProgramModuleRepository(Repository[ProgramModule]):
    """
    Repository Class for a program-module relationship.
    Extends the Repository class.
    """
    @property
    def _table_name(self):
        return "program_module"

    def _init_entity(self, data: dict):
        """
        Initializes a ProgramModule entity from the data dictionary.
        """
        return ProgramModule(
            id=data['id'],
            program_id=data['program_id'],
            module_id=data['module_id'],
            sort=data['sort'],
        )