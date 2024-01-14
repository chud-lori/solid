class Employee:
    def __init__(self, fullname: str = '', date_of_joining: str = '', annual_salary_package: str = '') -> None:
        self._fullname = fullname
        self._date_of_joining = date_of_joining
        self._annual_salary_package = annual_salary_package

    @property
    def fullname(self):
        return self._fullname

    @fullname.setter
    def fullname(self, value):
        self._fullname = value

    @property
    def date_of_joining(self):
        return self._date_of_joining

    @date_of_joining.setter
    def date_of_joining(self, value):
        self._date_of_joining = value

    @property
    def annual_salary_package(self):
        return self._annual_salary_package

    @annual_salary_package.setter
    def annual_salary_package(self, value):
        self._annual_salary_package = value

    def __repr__(self) -> str:
        return f"fullname: {self._fullname}, date: {self._date_of_joining}, salary: {self._annual_salary_package}"


class EmployeeService:
    def calculate_employee_salary(self, employee: Employee) -> int:
        print("Calculate salary")
        return employee._annual_salary_package / 12

    def calculate_employee_leaves(self, employee: Employee) -> int:
        print("Calculate leave")
        return employee._annual_salary_package * 20 /100

    def calculate_employee_tax(self, employee: Employee) -> int:
        print("Calculate tax")
        salary = employee._annual_salary_package
        return salary - (salary * 20 / 100)


class EmployeDAO:
    # data access object
    def save_employee(self, employee: Employee) -> Employee:
        print("Save employee")
        return employee

    def update_employee(self, employee: Employee) -> Employee:
        print("Update employee")
        return employee


emp_one: Employee = Employee("lori", "kemarin", 100)
print(f"fullname: {emp_one.fullname}")
emp_one.fullname = "lori update"
print(f"fullname: {emp_one.fullname}")

emp_ser: EmployeeService = EmployeeService()
print(emp_ser.calculate_employee_salary(emp_one))
print(emp_ser.calculate_employee_leaves(emp_one))
print(emp_ser.calculate_employee_tax(emp_one))

emp_dao: EmployeDAO = EmployeDAO()
print(emp_dao.save_employee(emp_one))
print(emp_dao.update_employee(emp_one))