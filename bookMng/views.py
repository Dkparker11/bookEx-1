from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect

from .models import MainMenu, Book

from .forms import BookForm

# Create your views here.


def index(request):
    return render(request, 'bookMng/welcome.html', 
    {
        'item_list': MainMenu.objects.all()
    }
    )



# view for posting a book
def postbook(request):
    submitted = False
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/postbook?submitted=True')
    else:
        form = BookForm()
        if 'submitted' in request.GET:
            submitted = True
    
    return render(request, 'bookMng/postbook.html', 
        {
            'form': form,
            'item_list': MainMenu.objects.all(),
            'submitted': submitted
        }
    ) 


def displaybooks(request):
    books = Book.objects.all()

    for b in books:
        pic_path = b.picture.url[14:]

    return render(request, 'bookMng/displaybooks.html',
                  {
                      'item_list': MainMenu.objects.all(),
                      'books': books
                  })






