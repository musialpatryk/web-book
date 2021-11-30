from django.shortcuts import render
from books.models import Review, Book
from django.http import HttpResponseRedirect
from .forms.review_form import ReviewForm
from .services import rating_service


# Create your views here.
def review_create(request):
    if request.method == 'POST':
        review_data = request.POST
        review = Review.objects.create_review(
            review_data['vote'],
            review_data['review'],
            Book.objects.get(id=review_data['book_id']),
            request.user
            # review_data['book_id']
        )
        review.save()
        return HttpResponseRedirect('/')

    book = Book.objects.get(slug='test')
    form = ReviewForm()
    return render(request, 'reviews/review_create.html', {'form': form})

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

    return HttpResponseRedirect('/')

def accept_review(request):
    return review_change_status(request, Review.STATUS_ACCEPTED)

def reject_review(request):
    return review_change_status(request, Review.STATUS_REJECTED)

def review_list(request):
    reviews = Review.objects.filter(status=Review.STATUS_PENDING)
    return render(request, 'reviews/review_list.html', {'reviews': reviews})