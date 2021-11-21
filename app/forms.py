from django import forms
from .models import Crypto, Store ,Transaction_history



class CryptoForm(forms.ModelForm):
	class Meta:
		model = Crypto
		fields = ["ticker"]
		exclude = ('owner',)