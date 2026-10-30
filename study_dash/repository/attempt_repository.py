from .repository import Repository
from study_dash.entity import Attempt

class AttemptRepository(Repository[Attempt]):
    """
    Repository Class for an attempt.
    Extends the Repository class.
    """
    @property
    def _table_name(self):
        return "attempt"

    def _init_entity(self, data: dict) -> Attempt:
        """
        Initializes an Attempt entity from the data dictionary.
        """
        return Attempt(
            id=data['id'],
            enrollment_id=data['enrollment_id'],
            evaluation_id=data['evaluation_id'],
            date_of_attempt=data['date_of_attempt'],
            score=data['score'],
            grade=data['grade'],
        )

    def find_by_enrollment_id(self, enrollment_id: int) -> list[Attempt]:
        """
        Finds all attempts for a given enrollment id.
        """
        return self.find_many_by_sql(
            'SELECT *'
            f' FROM {self._table_name}'
            ' WHERE enrollment_id = ?'
            ' ORDER BY date_of_attempt DESC',
            (enrollment_id,)
        )
