import csv

data = [
    ('iPhone 15 128 GB', 79990),
    ('iPhone 15 256 GB', 89990),
    ('iPhone 15 Pro 128 GB', 119990)
]

with open('prices.csv', 'w', newline='', encoding='cp1251') as f:
    writer = csv.writer(f, delimiter=',')   # явно ставим запятую
    writer.writerow(['Название', 'Цена'])
    writer.writerows(data)

print('prices.csv готов!')