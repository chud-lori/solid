from abc import ABC, abstractmethod

class EmployeeSalary(ABC):

    @abstractmethod
    def calculate_salary(self) -> int:
        ...

class PermanentEmployeeSalary(EmployeeSalary):
    def calculate_salary(self) -> int:
        print("Calculate salary permanent")
        return 100


class ContractEmployeeSalary(EmployeeSalary):
    def calculate_salary(self) -> int:
        print("Calculate salary contract")
        return 50


perm: PermanentEmployeeSalary = PermanentEmployeeSalary()
cont: ContractEmployeeSalary = ContractEmployeeSalary()

print(perm.calculate_salary())
print(cont.calculate_salary())