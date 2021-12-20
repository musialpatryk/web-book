from django import forms


class ReviewForm(forms.Form):

    placeholders = {
        'vote': 'Ocena',
        'review': 'Recenzja'
    }
    review = forms.CharField(max_length=255)

    vote = forms.IntegerField()
    book_id = forms.IntegerField(widget=forms.NumberInput(attrs={'hidden': True}))

    def __init__(self, *args, book=None, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        if book:
            self.book = book
            self.fields['book_id'].initial = book.id

        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control mb-2',
            })

            if field in self.placeholders:
                self.fields[field].widget.attrs.update({
                    'placeholder': self.placeholders[field],
                })