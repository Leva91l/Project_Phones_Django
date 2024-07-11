import csv

with open(r'C:\Users\а\Desktop\Python\djangoProject\phones.csv', 'r', encoding='UTF-8') as f:
    reader = csv.DictReader(f, delimiter=';')
    for row in reader:
        # id = row['id']
        name = row['name']
        price = row['price']
        image = row['image']
        release_date = row['release_date']
        lte_exist = row['lte_exists']
        print(name, price)