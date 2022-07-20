import datetime
import time

DateCreation = datetime.datetime.today().strftime("%d-%m-%Y")
TimeCreation = time.strftime("%H.%M.%S")

print("Local Date: ", TimeCreation + " " + DateCreation, "\n")

print("before import Salary", "\n")

import Salary

print("Module Salary was imported", "\n")

print("before import People", "\n")

import People

print("Module People was imported", "\n")

print("Начато выполнение if __name__ == '__main__'", "\n")
if __name__ == '__main__':
    Salary.calculate_salary()
    People.get_employees()
print("Закончено выполнение if __name__ == '__main__'")
