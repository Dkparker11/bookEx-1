from django.shortcuts import render
from django.http import HttpResponse
from .models import MainMenu

from .forms import BookForm
from django.http import  HttpResponseRedirect
from .models import Book

from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required




def index(request):
    #return HttpResponse("Hello World")
    #return render(request, 'bookMng/displaybooks.html')
    return render(request, 'bookMng/home.html',
                  {
                      'item_list': MainMenu.objects.all()
                  }
                  )


@login_required(login_url=reverse_lazy('login'))
def postbook(request):
    submitted = False
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            #form.save()
            book = form.save(commit=False)
            try:
                book.username = request.user
            except Exception:
                pass
            book.save()
            return HttpResponseRedirect('/postbook?submitted=True')
    else:
        form = BookForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request,
                 'bookMng/postbook.html',
                 {
                     'form': form,
                     'item_list': MainMenu.objects.all(),
                     'submitted': submitted
                 }

   )


@login_required(login_url=reverse_lazy('login'))
def displaybooks(request):
    books = Book.objects.all()
    for b in books:
        b.pic_path = b.picture.url[14:]
    return render(request,
                  'bookMng/displaybooks.html',
                  {
                      'item_list': MainMenu.objects.all(),
                      'books': books
                  }
    )



@login_required(login_url=reverse_lazy('login'))
def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request,
                  'bookMng/book_detail.html',
                  {
                      'item_list': MainMenu.objects.all(),
                      'book': book
                  })




class Register(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register-success')

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.success_url)
# Create your views here.



# Added search function
def searchbar(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        book = Book.objects.get(name=search)
        return render(request,
                      'bookMng/book_detail.html',
                      {
                          'item_list': MainMenu.objects.all(),
                          'book': book
                      })
    