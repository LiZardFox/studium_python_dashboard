from .repository import Repository
from study_dash.entity import Student

class StudentRepository(Repository[Student]):
    """
    Repository Class for a student.
    Extends the Repository class.
    """
    @property
    def _table_name(self):
        return "student"

    def _init_entity(self, data: dict):
        """
        Initializes a Student entity from the data dictionary.
        """
        return Student(
            id=data['id'],
            first_name=data['first_name'],
            last_name=data['last_name'],
            matrikel_nr=data['matrikel_nr'],
            password=data['password'],
        )

    def find_by_matrikel_nr(self, matrikel_nr: str) -> Student:
        """
        Finds a student by their matrikel number.
        """

        return self.find_one_by_sql(
            'SELECT *'
            f' FROM {self._table_name}'
            ' WHERE matrikel_nr = ?',
            (matrikel_nr,)
        )

    def insert_student(self, matrikel_nr: str, password_hash: str, first_name: str, last_name: str):
        """
        Inserts a new student into the database.
        """

        db = self._get_db()
        db.execute(
            f'INSERT INTO {self._table_name}'
            ' (matrikel_nr, password, first_name, last_name)'
            ' VALUES (?, ?, ?, ?)',
            (matrikel_nr, password_hash, first_name, last_name),
        )
        db.commit()
        return self.find_by_matrikel_nr(matrikel_nr=matrikel_nr)