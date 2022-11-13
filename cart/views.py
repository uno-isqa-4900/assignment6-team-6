from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from bookstore.models import Book
from .cart import Cart
from .forms import CartAddBookForm


@require_POST
def cart_add(request, book_id):
    print("I am in cart")
    cart = Cart(request)
    book = get_object_or_404(Book, id=book_id)
    form = CartAddBookForm(request.POST)
    if form.is_valid():
        print("form is valid")
        cd = form.cleaned_data
        print(cd)
        cart.add(book=book,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')


def cart_remove(request, book_id):
    cart = Cart(request)
    book = get_object_or_404(Book, id=book_id)
    cart.remove(book)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
            item['update_quantity_form'] = CartAddBookForm(
                              initial={'quantity': item['quantity'],
                              'update': True})
    return render(request, 'cart/detail.html', {'cart': cart})