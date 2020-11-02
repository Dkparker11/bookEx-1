from django.shortcuts import render


from django.http import HttpResponseRedirect

from .models import MainMenu, Book

from .forms import BookForm

from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy



# Create your views here.


def index(request):
    return render(request, 'bookMng/welcome.html',
    {
        'item_list': MainMenu.objects.all(),
    }
    )



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
        'submitted': submitted,
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



class Register(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register-success')

    def form_valid(self, form):
        form.save()
        return HttpresponseRedirect(self.success_url)

