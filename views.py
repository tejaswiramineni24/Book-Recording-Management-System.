from django.shortcuts import render
from django.http import HttpResponse
from BRMSapp.models import book
from BRMSapp.forms import NewBookForm,searchform
from django.db import models
from BRMSapp import models
from django.http import HttpResponseRedirect




# Create your views here.
def test(request):
    str="Hello"
    return HttpResponse(str)


def view_books(request):
    books=book.objects.all()
    # data={'books':books}
    res=render(request,'BRMSapp/view.html', { 'books' : books })
    return res

def newBook(request):
    form = NewBookForm()
    res = render(request,'BRMSapp/new_book.html',{'form': form})
    return res

def add(request):
    if request.method == 'POST':
        form=NewBookForm(request.POST)
        book=models.book()
        book.title=form.data['title']
        book.price=form.data['price']
        book.Auther=form.data['Auther']
        book.Publisher=form.data['Publisher']
        book.save()
        s="Record Stored <br> <a href='view_books'>View All Books</a>"
        return HttpResponse(s)
    
    
def editBook(request):
        book=models.book.objects.get(id=request.GET['bookid'])
        print("book=",book)
        fields={'title':book.title,'price':book.price,'Auther':book.Auther,'Publisher':book.Publisher}
        form=NewBookForm(initial=fields)
        res=render(request,'BRMSapp/edit_book.html',{'form':form,'book':book})
        return res
    
def edit(request):
        if request.method =="POST":
            form=NewBookForm(request.POST)
            book=models.book()
            book.id=request.POST['bookid']
            book.title=request.POST['title']
            book.price=request.POST['price']
            book.Auther=request.POST['Auther']
            book.Publisher=request.POST['Publisher']
            book.save()
        return HttpResponseRedirect('view_books')


def deleteBook(request):
        bookid=models.book.objects.get(id=request.GET['bookid'])
        book=models.book.objects.filter(id=bookid.id)
        book.delete()
        return HttpResponseRedirect('view_books')

def Searchform(request): 
        form = searchform()
        res = render(request,'BRMSApp/search_book.html',{'form': form})
        return res

def search(request):
        form=searchform(request.POST)
        books=models.book.objects.filter(title=form.data['title'])
        res =render(request,'BRMSApp/search_book.html',{'form':form,'books':books})
        return res

        

    
        
        
        
               