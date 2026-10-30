from .repository import Repository
from study_dash.entity import Evaluation

class EvaluationRepository(Repository[Evaluation]):
    """
    Repository Class for an evaluation.
    Extends the Repository class.
    """
    @property
    def _table_name(self):
        return "evaluation"

    def _init_entity(self, data: dict):
        """
        Initializes an Evaluation entity from the data dictionary.
        """
        return Evaluation(
            id=data['id'],
            module_id=data['module_id'],
            type=data['type'],
            max_score=data['max_score'],
            max_attempt=data['max_attempt'],
            weight=data['weight']
        )
