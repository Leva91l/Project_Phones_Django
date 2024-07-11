import csv

# Create your views here.
from demoapp.models import Phone
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
    
    for el in Phone.objects.all():
        if el.name == phone:
            content = {
                'name': el.name,
                'price': el.price,
                'image': el.image                
            }
            return render(request, 'phone_info.html', context=content)