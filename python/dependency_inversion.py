from abc import ABC, abstractmethod

class Repository(ABC):
    @abstractmethod
    def save(self):
        ...


class SQLRepository(Repository):
    def save(self):
        print("SAVE IN SQL")


class NoSQLRepository(Repository):
    def save(self):
        print("WRITE NOSQL")


class Service:
    def __init__(self, repository: Repository):
        self.repository = repository

    def save(self):
        self.repository.save()


repo_sql: Repository = SQLRepository()
repo_no: Repository = NoSQLRepository()

service_sql: Service = Service(repo_sql)
service_no: Service = Service(repo_no)

service_sql.save()
service_no.save()
