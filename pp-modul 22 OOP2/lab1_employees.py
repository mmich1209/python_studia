from lab1_employee import Employee

employees = []
employees.append(Employee("Jan", "Kowalski", 25, 1000))
employees.append(Employee("Edmund", "Kaczmarczyk", 40, 2000))
employees.append(Employee("Ewa", "Nowak", 60, 3000))


def payroll(employees):
    print("Lista płac")
    print("-" * 30)
    for employee in employees:
        print(employee.get_fullname(),
              "wiek:", employee.get_age(), "lat",
              "pensja:", employee.get_salary())

payroll(employees)
employees[0].raise_salary()
employees[2].raise_salary(30)
employees[0].raise_salary()
print("Podwyzka!")

payroll(employees)