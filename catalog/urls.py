# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 09:11:56 2023

@author: Nguyen Minh Triec
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    # added on 2023-10-14 by N.M.T ====
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
    # ====
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    path('borrowed/', views.AllBooksBorrowedListView.as_view(), name='all-borrowed'),
    path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
    # ====
    path('author/create/', views.AuthorCreate.as_view(), name='author-create'),
    path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author-update'),
    path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author-delete'),
    # ====
    path('book/create', views.BookCreate.as_view(), name='book-create'),
    path('book/<int:pk>/update', views.BookUpdate.as_view(), name='book-update'),
    
    path('circles/', views.random_circles, name='random-circles'),
]

