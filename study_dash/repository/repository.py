from abc import abstractmethod
from typing import TypeVar
import sqlite3

from study_dash.entity import Entity
from study_dash.service import DBConnection
from study_dash.service import Service, ServiceContainer

T = TypeVar('T', bound=Entity)

class Repository[T](Service):
    """
    Abstract Repository class.
    Extends the Service class.
    Provides basic read and delete operations for entities.
    Has a entity map to store and retrieve entities by their ID.
    """

    
    def __init__(self, service_container: ServiceContainer):
        self.__entity_map: dict[int, T] = {}
        self.db_connection = service_container.get_service(DBConnection)

    @property
    @abstractmethod
    def _table_name(self) -> str:
        """Holds the name of the table associated with this repository."""
        pass

    def _get_db(self) -> sqlite3.Connection:
        """Shorthand for getting the database connection."""
        return self.db_connection.get_db()

    def _delete_from_map(self, id: int) -> None:
        """Removes an entity from the map by its ID."""
        self.__entity_map.pop(id, None)

    def _clear_map(self) -> None:
        """Clears all entities from the map."""

        self.__entity_map.clear()

    def _map_or_init(self, data: dict) -> T:
        """Maps an entity to the map or initializes a new one."""

        id = data['id']
        if id in self.__entity_map:
            return self.__entity_map[id]
        entity = self._init_entity(data)
        self.__entity_map[entity.id] = entity
        return entity

    def find_all(self):
        """Finds all entities in the database."""

        return self.find_many_by_sql(
            'SELECT *'
            f' FROM {self._table_name}'
        )
    
    def find_by_id(self, id: int):
        """Finds an entity by its ID."""

        if id in self.__entity_map:
            return self.__entity_map[id]
        return self.find_one_by_sql(
            'SELECT *'
            f' FROM {self._table_name}'
            ' WHERE id = ?',
              (id,)
        )
    
    def find_many_by_sql(self, sql: str, parameters: sqlite3._Parameters = ()):
        """Finds many entities by executing a SQL query."""

        db = self._get_db()
        data = db.execute(sql,parameters).fetchall()
        return [self._map_or_init(d) for d in data]

    def find_one_by_sql(self, sql: str, parameters: sqlite3._Parameters = ()):
        """Finds one entity by executing a SQL query."""

        db = self._get_db()
        data = db.execute(sql, parameters).fetchone()
        if data == None:
            return None
        return self._map_or_init(data)


    def delete(self, entity: T):
        """Deletes an entity from the database."""

        db = self._get_db()
        db.execute(f'DELETE FROM {self._table_name} WHERE id = ?', (entity.id,))
        db.commit()
        self._delete_from_map(entity.id)
        

    @abstractmethod
    def _init_entity(data: dict) -> T:
        """Initializes an entity from a data dictionary."""

        pass
