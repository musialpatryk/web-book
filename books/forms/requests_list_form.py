from django import forms


class RequestListForm(forms.Form):
    book_id = forms.IntegerField(widget=forms.NumberInput(attrs={'hidden': True}))
    accept = forms.NullBooleanField()

    def __init__(self, *args, book=None, **kwargs):
        super(RequestListForm, self).__init__(*args, **kwargs)
        if book:
            self.book = book
            self.fields['book_id'].initial = book.id