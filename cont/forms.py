from django import forms

class FormularioCont(forms.Form):

    nom=forms.CharField(label="Nombre", required=True)
    ema=forms.CharField(label="Email", required=True)
    cont=forms.CharField(label="Contenido", required=True, widget=forms.Textarea)