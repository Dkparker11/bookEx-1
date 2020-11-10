from django.urls import path
from .import views


urlpatterns = [
    path('', views.index, name='index'),
    path('book_detail/<int:book_id>', views.book_detail, name='book_detail'),
    path('postbook', views.postbook, name='postbook'),
    path('displaybooks', views.displaybooks, name='displaybooks'),
# added search to urls    
    path('searchbar/', views.searchbar, name='searchbar'),
]

