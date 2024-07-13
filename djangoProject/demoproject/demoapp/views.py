import csv, json

# Create your views here.
from demoapp.models import Phone, Book
from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q


def create_phone(request):
    with open('phones.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            name = row['name']
            price = row['price']
            image = row['image']
            release_date = row['release_date']
            lte_exist = row['lte_exists']
            phone = Phone(
                name=name,
                price=int(price),
                image=image,
                release_date=release_date,
                lte_exist=lte_exist,
            )
        
            phone.save()
        return HttpResponse(f'success, {phone.name} added into db!')

def list_phone(request):
    phones = Phone.objects.all()
    return render(request, 'phones.html', {'phones': phones})

def phone_info(request, phone):
    phone = str(phone.replace('-', ' '))
    for el in Phone.objects.all():
        if el.name == phone:
            content = {
                'name': el.name,
                'price': el.price,
                'image': el.image                
            }
            return render(request, 'phone_info.html', context=content)
        
def create_book(request):
    with open(r'C:\Users\а\Desktop\Python\djangoProject\demoproject\books.json', 'r', encoding='UTF-8') as jsonfile:
        data = json.load(jsonfile)
        for el in data:
            book = Book(
                name = el['fields']['name'],
                author = el['fields']['author'],
                date = el['fields']['pub_date'],
            )
            book.save()
        return HttpResponse(f'Success! {book.name} added in db!')
    
def list_book(request):
    books = Book.objects.all()
    return render(request, 'books.html', {'books': books})

def book_pub_date(request, date):
    date = str(date)

    books = Book.objects.all()

    for book in books:
        
        if str(book.date) == date:            
            context = {
                'name': book.name,
                'author': book.author,
                'date': book.date
            }
            return render(request, 'books_pub_date.html', context=context)
