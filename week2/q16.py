'''Define an abstract class `IDatabaseOperations` with methods `insert()`, `update()`, and `delete()`. Implement this in `SQLDatabase` and 
`NoSQLDatabase`.'''

from abc import ABC,abstractmethod
class IDatabaseOperations(ABC):
    @abstractmethod
    def insert():
        pass
    @abstractmethod
    def update():
        pass
    @abstractmethod
    def delete():
        pass
class SQLDatabase(IDatabaseOperations):
    def insert(self):
        print("Data is inserted into SQL database")
    def update(self):
        print("Data is updated in SQL database")
    def delete(self):
        print("Data is deleted from SQL database")
class NoSQLDatabase(IDatabaseOperations):
    def insert(self):
        print("Data is inserted into NoSQL database")
    def update(self):
        print("Data is updated in NoSQL database")
    def delete(self):
        print("Data is deleted from NoSQL database")
sql=SQLDatabase()
sql.insert()
sql.update()
sql.delete()

nosql=NoSQLDatabase()
nosql.insert()
nosql.update()
nosql.delete()