from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    # return HttpResponse('testing hello world!')
    posts = [
        {
            'caption':'Sushi',
            'img_url':'https://www.justonecookbook.com/wp-content/uploads/2020/01/Sushi-Rolls-Maki-Sushi-%E2%80%93-Hosomaki-1106-II.jpg'
        },
        {
            'caption':'SoonTofu',
            'img_url':'https://www.cookerru.com/wp-content/uploads/2021/03/soon-dubu-jjigae-2-web-1170x1755.jpg.webp'
        },
        {
            'caption':'KBBQ',
            'img_url':'https://365thingsinhouston.com/wp-content/uploads/2022/02/korean-bbq-restaurants-in-greater-houston-gen-korean-barbecue-696x407.jpg'
        },
        {
            'caption':'Coca-Cola',
            'img_url':'https://us.coca-cola.com/content/dam/nagbrands/us/coke/en/home/coca-cola-original-20oz.png'
        },
        {
            'caption':'Pasta',
            'img_url':'https://www.foodiecrush.com/wp-content/uploads/2020/05/Penne-Marinara-Sauce-foodiecrush.com-004.jpg'
        },      
    ]
    
    context = {'posts': posts}
    
    return render(request, 'home_pg.html', context=context)