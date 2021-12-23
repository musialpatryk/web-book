from django.core.paginator import Paginator
from django.shortcuts import render
from books.models import Book
from reviews.models import Review
from django.http import HttpResponseRedirect
from .forms.review_form import ReviewForm
from .services import rating_service
from django.contrib import messages
from accounts.decorators import allowed_users, admin_only
from django.contrib.auth.decorators import login_required


@login_required(login_url='accounts:login')
@allowed_users(allowed_roles=['viewer', 'admin'])
def review_create(request):
    if request.method == 'POST':
        review_data = request.POST
        vote = int(review_data['vote'])

        if vote > 5 or vote < 0:
            messages.success(request, 'Oddany głos powinien mieścić się w przedziale od 1 do 5')
            return HttpResponseRedirect('/')

        review = Review.objects.create_review(
            vote,
            review_data['review'],
            Book.objects.get(id=review_data['book_id']),
            request.user
        )
        review.save()
        messages.success(request, 'Recenzja została dodana i oczekuje na akceptację')
        return HttpResponseRedirect('/')

    form = ReviewForm()
    return render(request, 'reviews/review_create.html', {'form': form})

@login_required(login_url='accounts:login')
@admin_only
def review_change_status(request, status):
    if request.method != 'POST':
        return HttpResponseRedirect('/')

    if status != Review.STATUS_PENDING and status != Review.STATUS_REJECTED and status != Review.STATUS_ACCEPTED:
        return HttpResponseRedirect('/')

    review = Review.objects.get(pk=request.POST['review_id'])

    review.status = status
    review.save()
    if review.status == Review.STATUS_ACCEPTED:
        rating_service.recalculate_book_rating(review.book)
        rating_service.recalculate_author_rating(review.book.authors.all())

    messages.success(request, 'Pomyslnie zmieniono status recenzji')
    return HttpResponseRedirect('/')


def accept_review(request):
    return review_change_status(request, Review.STATUS_ACCEPTED)


def reject_review(request):
    return review_change_status(request, Review.STATUS_REJECTED)

@login_required(login_url='accounts:login')
@admin_only
def review_list(request):
    p = Paginator(Review.objects.filter(status=Review.STATUS_PENDING), 10)
    page = request.GET.get('page')
    reviews = p.get_page(page)
    return render(request, 'reviews/review_list.html', {'reviews': reviews})