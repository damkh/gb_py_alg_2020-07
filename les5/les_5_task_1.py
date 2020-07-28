"""
1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала
для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и
отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
"""
from collections import namedtuple
import random


companies_num = int(input("Введите количество предприятий: "))
Company = namedtuple('Company', 'name, q_1, q_2, q_3, q_4 profit_avg')
companies = []
name_template = 'Company-'
s = 0
for i in range(companies_num):
    company_name = name_template + str(i + 1)
    q_1 = random.randint(100, 400)
    q_2 = random.randint(200, 900)
    q_3 = random.randint(100, 600)
    q_4 = random.randint(500, 1500)
    profit_avg = (q_1 + q_2 + q_3 + q_4) / 4
    companies.append(Company(company_name, q_1, q_2, q_3, q_4, profit_avg))
    print(f'Средняя прибыль компании {company_name} за год равна: {profit_avg}')
    s += profit_avg

general_avg = s / companies_num
print(f'Средняя прибыль по всем компаниям равна: {general_avg}')
print(f'Прибыль выше средней: {[company.name for company in companies if company.profit_avg > general_avg]}')
print(f'Прибыль ниже средней: {[company.name for company in companies if company.profit_avg < general_avg]}')
