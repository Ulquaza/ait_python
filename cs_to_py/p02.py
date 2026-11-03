import sqlite3
import json
from pathlib import Path
from abc import ABC, abstractmethod

class IRoleRepository(ABC):
    @abstractmethod
    def is_assigned(self, role, user) -> bool:
        pass
    
    @abstractmethod
    def assign(self, role, user):
        pass
    
    @abstractmethod
    def unassign(self, role, user):
        pass

class InMemoryRoleRepository(IRoleRepository):
    def __init__(self):
        self._links: list[tuple[int, int]] = []
    
    def is_assigned(self, role, user) -> bool:
        return (role.id, user.id) in self._links
    
    def assign(self, role, user):
        self._links.append((role.id, user.id))
    
    def unassign(self, role, user):
        self._links.remove((role.id, user.id))

class SqlRoleRepository(IRoleRepository):
    def __init__(self, connection: sqlite3.Connection):
        self._connection = connection
    
    def is_assigned(self, role, user) -> bool:
        cursor = self._connection.execute("...", (role.id, user.id))
        return bool(cursor.fetchone()[0])
    
    def assign(self, role, user):
        self._connection.execute("insert...", (role.id, user.id))
        self._connection.commit()
    
    def unassign(self, role, user):
        self._connection.execute("delete...", (role.id, user.id))
        self._connection.commit()

class JsonRoleRepository(IRoleRepository):
    def __init__(self, path: str):
        self._path = Path(path)
        if (self._path.suffix.lower() != ".json"):
            raise ValueError("file must have .json extension")
        if (self._path.exists()):
            with self._path.open(...) as file:
                self._links = [...]
        else:
            self._links = []
    
    def _save(self):
        with self._path.open(...) as file:
            json.dump(...)
        
    def is_assigned(self, role, user) -> bool:
        return (role.id, user.id) in self._links
    
    def assign(self, role, user):
        self._links.append((role.id, user.id
        self._save()
    
    def unassign(self, role, user):
        self._links.remove((role.id, user.id))
        self._save()
    
class RoleRepositoryFactory:
    @staticmethod
    def create(kind: str, connection: sqlite3.Connection | None = None, json_path: str = "file.json") -> IRoleRepository:
        match kind:
            case "memory":
                return InMemoryRoleRepository()
            case "sql":
                return SqlRoleRepository(connection)
            case "json":
                return JsonRoleRepository(json_path)
            case _:
                raise ValueError("unknown repository type")
