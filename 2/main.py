
from inherit import Employee, Manager

def get_employee_data():
    name = input('Введите имя сотрудника: ')
    position = float(input('Введите уровень позиции: '))
    salary = float(input('Введите сумму зарплаты: '))
    year = int(input('Введите год: '))
    month = int(input('Введите месяц: '))
    return Employee(name, position, salary), year, month

def get_manager_data():
    department = input('Введите название отдела: ')
    team_size = int(input('Введите количество сотрудников: '))
    name = input('Введите имя менеджера: ')
    position = float(input('Введите уровень позиции: '))
    salary = float(input('введите сумму зарплаты: '))
    return Manager(department, team_size, name, position, salary)

def display_info(obj, year, month):
    print('Информация:', obj.info())
    print('Рассчитанная зарплата:', obj.calculation_salary(year, month))
#обычный сотрудник
employee, year, month = get_employee_data()
display_info(employee, year, month)

#менеджер
manager = get_manager_data()
display_info(manager, year, month)
