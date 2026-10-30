from .repository import Repository
from .program_module_repository import ProgramModuleRepository

from study_dash.entity import Module
from study_dash.entity import Module

class ModuleRepository(Repository[Module]):
    """
    Repository Class for a module.
    Extends the Repository class.
    """
    def __init__(self, service_container):
        super().__init__(service_container)
        self.program_module_repository = service_container.get_service(ProgramModuleRepository)

    @property
    def _table_name(self):
        return "module"

    def _init_entity(self, data: dict):
        """
        Initializes a Module entity from the data dictionary.
        """

        return Module(
            id=data['id'],
            name=data['name'],
        )

    def find_by_program_id(self, program_id: int):
        """
        Finds all modules by program id.
        """

        return self.find_many_by_sql(
            'SELECT m.*'
            f' FROM {self._table_name} m'
            f' INNER JOIN {self.program_module_repository._table_name} pm on m.id = pm.module_id'
            ' WHERE pm.program_id = ?'
            ' ORDER BY pm.sort',
            (program_id,)
        )