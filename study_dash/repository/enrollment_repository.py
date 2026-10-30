from .repository import Repository
from study_dash.entity import Enrollment

class EnrollmentRepository(Repository[Enrollment]):
    """
    Repository Class for an enrollment.
    Extends the Repository class.
    """
    @property
    def _table_name(self):
        return "enrollment"

    def _init_entity(self, data: dict):
        """
        Initializes an Enrollment entity from the data dictionary.
        """

        return Enrollment(
            id=data['id'],
            program_id=data['program_id'],
            student_id=data['student_id'],
            semesters=data['semesters'],
            target_grade=data['target_grade'],
            start_date=data['start_date'],
            end_date=data['end_date'],
            target_end_date=data['target_end_date'],
        )

    def find_by_student_id(self, student_id: int):
        """
        Finds all enrollments for a given student id.
        """
        return self.find_many_by_sql(
            'SELECT *'
            f' FROM {self._table_name}'
            ' WHERE student_id = ?',
            (student_id,)
        )