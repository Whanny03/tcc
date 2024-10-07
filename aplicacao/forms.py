from django import forms
from .models import ImageCarousel, Eletiva, Tutoria, SocialLinks, MaisSobre, LinkEletiva, NossaHistoria, NewsOne, Evento, Noticia2


class ImageCarouselForm(forms.ModelForm):
    class Meta:
        model = ImageCarousel
        fields = ['image', 'caption']

     
class EletivaForm(forms.ModelForm):
    class Meta:
        model = Eletiva
        fields = ['title', 'sub_title', 'description', 'image']
        
        
class TutoriaForm(forms.ModelForm):
    class Meta:
         model = Tutoria
         fields = ['title', 'description', 'image']

class SocialLinksForm(forms.ModelForm):
    class Meta:
        model = SocialLinks
        fields = ['instagram_url', 'whatsapp_number']
        widgets = {
            'instagram_url': forms.URLInput(attrs={'placeholder': 'https://instagram.com/seu_usuario'}),
            'whatsapp_number': forms.TextInput(attrs={'placeholder': 'Seu número de WhatsApp com código do país'}),
        }

class MaisSobreForm(forms.ModelForm):
    class Meta:
        model = MaisSobre
        fields = ['title', 'description', 'image', 'image_2', 'image_3']
        
class LinkEletivaForm(forms.ModelForm):
    class Meta:
        model = LinkEletiva
        fields = ['title', 'link']
        

        
class NossaHistoriaForm(forms.ModelForm):
    class Meta:
        model = NossaHistoria
        fields = ['title', 'data_publicacao', 'image']
        
        
class NewsOneForm(forms.ModelForm):
    class Meta:
        model = NewsOne
        fields = ['title', 'description', 'description_2', 'image']     
class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['nome', 'descricao', 'data', 'hora']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
            'hora': forms.TimeInput(attrs={'type': 'time'}),
        }

class Noticia2Form(forms.ModelForm):
    class Meta:
        model = Noticia2
        fields = ['titulo', 'descricao1', 'descricao2', 'imagem', 'data_publicacao']
