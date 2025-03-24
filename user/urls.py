from django.urls import path
from user import views

urlpatterns = [
    path('dashboard/',views.dashboard,name='dashboard'),
    path('users/',views.users,name='users'),
    path('books/',views.books,name='books'),
    path('books/new/',views.addbooks,name='addbook'),
    path('books/author/',views.author,name='author'),
    path('books/category/',views.category,name='category'),

    path('books/order/<str:pk>/',views.order,name='order'),
    
    path('books/update/<str:pk>/',views.updatebook,name='update'),
    path('books/delete/<str:pk>/',views.deletebook,name='delete'),
    
    path('user/update/<str:pk>/',views.updateuser,name='updateuser'),
    path('user/delete/<str:pk>/',views.deleteuser,name='deleteuser'),
    
    path('author/update/<str:pk>/',views.updateauthor,name='updateauthor'),
    path('author/delete/<str:pk>/',views.deleteauthor,name='deleteauthor'),
    
    path('category/update/<str:pk>/',views.updatecategory,name='updatecategory'),
    path('category/delete/<str:pk>/',views.deletecategory,name='deletecategory'),
    
    path('login/',views.login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('register/',views.register,name='register'),
]