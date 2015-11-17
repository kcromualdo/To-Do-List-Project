from django import forms
from lists.models import Item

EMPTY_LIST_ERROR="YOu can't have an empty list"

class ItemForm(forms.models.ModelForm):
	#item_text = forms.CharField(
	#	widget=forms.fields.TextInput(attrs={
	#		'placeholder': 'Enter a to-do item',
	#		'class':'form-control input-lg',
	#	}),
	#)
	class Meta:
		model=Item
		fields=('text',)
		widgets={
			'text':forms.fields.TextInput(attrs={
				'placeholder':'Enter a to-do item',
				'class':'form-control input-lg',

			}),

		}
		error_messages={
			'text':{'required':EMPTY_LIST_ERROR}
		}