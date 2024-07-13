import json

def create_book():
    with open(r'C:\Users\а\Desktop\Python\djangoProject\demoproject\books.json', 'r', encoding='UTF-8') as jsonfile:
        data = json.load(jsonfile)
        # print(data)
        for el in data:
            x = el['fields']['name']
            print(x)
create_book()