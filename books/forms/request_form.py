from django import forms

class BookRequestForm(forms.Form):
    placeholders = {
        'title': 'Tytuł',
        'description': 'Opis'
    }
    title = forms.CharField(
        max_length=100,
    )
    author = forms.ChoiceField(
        choices=(),
    )
    genre = forms.ChoiceField(
        choices=(),
    )
    description = forms.CharField(
        widget=forms.Textarea()
    )

    def __init__(self, *args, authors=None, genre=None, **kwargs):
        super(BookRequestForm, self).__init__(*args, **kwargs)
        if authors:
            self.fields['author'].choices = authors

        if genre:
            self.fields['genre'].choices = genre

        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control mb-2',
            })

            if field in self.placeholders:
                self.fields[field].widget.attrs.update({
                    'placeholder': self.placeholders[field],
                })