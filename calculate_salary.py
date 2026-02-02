from abc import ABC,abstractmethod
class Employee(ABC):
    def __init__(self,name,base_salary):
        self._name=name
        self._base_salary=base_salary
    @abstractmethod
    def calculate_salary(self):
        pass
class FullTimeEmployee(Employee):
    def __init__(self,name,base_salary,bonus):
        self._bonus=bonus
        super().__init__(name,base_salary)
    def calculate_salary(self):
        return self._base_salary+self._bonus
class ContractEmployee(Employee):
    def __init__(self,name,base_salary,hours_worked):
        super().__init__(name,base_salary)
        self._hours_worked=hours_worked
    def calculate_salary(self):
        return self._base_salary*self._hours_worked
class Intern(Employee):
    def __init__(self,name,stiphend):
        super().__init__(name,0)
        self._stiphend=stiphend
    def calculate_salary(self):
        return self._stiphend
employees=[FullTimeEmployee("A",50000,10000),ContractEmployee("B",10000,5000),Intern("C",25000)]
result=[emp.calculate_salary() for emp in employees]
print(result)