# 3 вариант


import datetime

#родительский класс
class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def info(self):
        conditions = [
            f"Имя: {self.name}",
            f"Позиция: {self.position}",
            f"Зарплата: {self.salary}"
        ]
        return "; ".join(conditions)

#считаем зарплату за конкретный месяц
    def calculation_salary(self, year, month):
        start_date = datetime.date(year, month, 1)
        next_month = month + 1 if month < 12 else 1
        next_year = year if month < 12 else year + 1
        end_date = datetime.date(next_year, next_month, 1) - datetime.timedelta(days=1) #от первого дня следующего месяца отнимаем один день

        total_days = (end_date - start_date).days + 1 #общее количество дней в месяце
        worked_days = sum(
            1 for i in range(total_days)
            if (start_date + datetime.timedelta(days=i)).weekday() < 5 #исключаем субботу и воскресенье
        )

        return self.position * self.salary * worked_days

#дочерний класс
class Manager(Employee):
    def __init__(self, department, num_employees, name, position, salary):
        super().__init__(name, position, salary)
        self.department = department
        self.num_employees = num_employees

    def info(self):
        base_info = super().info()
        extra_info = f"Отдел: {self.department};Количество сотрудников: {self.num_employees}" #добавляем данные менеджера
        return f"{base_info}; {extra_info}"

#рассчитывем зарплату
    def calculation_salary(self, year, month):
        start_date = datetime.date(year, month, 1)
        next_month = month + 1 if month < 12 else 1
        next_year = year if month < 12 else year + 1
        end_date = datetime.date(next_year, next_month, 1) - datetime.timedelta(days=1)

        total_days = (end_date - start_date).days + 1
        worked_days = sum(
            1 for i in range(total_days)
            if (start_date + datetime.timedelta(days=i)).weekday() < 5
        )

        base = self.position * self.salary * worked_days #базовая зарплата
        bonus = base * (1 / self.num_employees) #бонус (чем больше сотрудников, тем меньше бонус)
        return base + bonus
