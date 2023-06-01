from django import forms


class ProductCreateForm(forms.Form):
    image = forms.FileField(required=False)
    title = forms.CharField(max_length=256)
    description = forms.CharField(widget=forms.Textarea)
    price = forms.FloatField()


class ReviewCreateForm(forms.Form):
    review = forms.CharField(max_length=256)
