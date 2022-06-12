from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Item
from django.template import loader 
from .forms import ItemForm
from django.contrib import messages

# Create your views here.

def index(request):
    item_list = Item.objects.all()
    context = {'item_list':item_list,}
    return render(request,'mainapp/index.html',context)

# def index(request):
#     item_list = Item.objects.all()
#     template = loader.get_template('mainapp/index.html')
#     context = {'item_list':item_list,}
#     return HttpResponse(template.render(context,request))

# def index(request):
#     return HttpResponse('Hello World')

def item(request):
    return HttpResponse('<h1>This is an item view</h1>')

def detail(request,item_id):
    item = Item.objects.get(pk=item_id)
    context = {"item":item}
    return render(request,'mainapp/detail.html',context)
    # return HttpResponse('This is item id: %s' %item_id)

def create_item(request):
    form = ItemForm(request.POST or None)

    if request.method == "POST":
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('mainapp:index')
    return render(request,'mainapp/create_item.html',{"form":form})

def update_item(request,item_id):
    item = Item.objects.get(id=item_id)
    form = ItemForm(request.POST or None, instance=item)

    if request.method == "POST":
        form = ItemForm(request.POST, request.FILES,instance=item)
        if form.is_valid():
            form.save()
            messages.success(request,'Food record was updated successfully.')
            return redirect ('mainapp:index')
        # return redirect('mainapp:update_item_url' '/item_id')
    return render(request,'mainapp/update_item.html',{"form":form})

def delete_item(request,item_id):
    item = Item.objects.get(id=item_id)
    # form = ItemForm(request.POST or None, instance=item)

    if request.method == 'POST':
        item.delete()
        messages.success(request,'Food record was successfully deleted.')
        return redirect('mainapp:index')
        # return redirect('mainapp:update_item_url' '/item_id')
    return render(request,'mainapp/delete_item.html',{"item":item})