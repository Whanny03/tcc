from django.db import models



class ImageCarousel(models.Model):
    image = models.ImageField(upload_to='carousel_images/')
    caption = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.caption if self.caption else "Carousel Image"


#Carrossel de Imagens
    
class ImgCarrossel(models.Model):
    image1 = models.ImageField(upload_to='carousel_images/')
    image2 = models.ImageField(upload_to='carousel_images/')
    image3 = models.ImageField(upload_to='carousel_images/')
    
    
#Eletivas   

class Eletiva(models.Model):
    title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255, null=True)
    description = models.TextField()
    image = models.ImageField(upload_to='ele_images/')

    def __str__(self):
        return self.title

# Link inscrever nas eletivas

class LinkEletiva(models.Model):
    title = models.CharField(max_length=255)
    link = models.URLField()    
    
    def __str__(self):
        return self.title
    
# Tutoria

class Tutoria(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='tutoria_images/')
    
    def __str__(self):
        return self.title
    
# Links
class SocialLinks(models.Model):
    instagram_url = models.URLField(max_length=255, blank=True, null=True)
    whatsapp_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f"Instagram: {self.instagram_url}, WhatsApp: {self.whatsapp_number}"

# Mais Sobre
class MaisSobre(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='mais_images/', null=True)
    image_2 = models.ImageField(upload_to='mais_images/', null=True)
    image_3 = models.ImageField(upload_to='mais_images/', null=True)

    def __str__(self):
        return self.title
    
# Calendário



# Nossa História

class NossaHistoria(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='tutoria_images/', null=True)
    
    def __str__(self):
        return self.title
    
class NewsOne(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    description_2 = models.TextField()
    image = models.ImageField(upload_to='news_images/', null=True)
    date_published = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

class NewsTwo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    description_2 = models.TextField(null=True)
    image = models.ImageField(upload_to='news_images/')
    date_published = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

class Evento(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    data = models.DateField()
    hora = models.TimeField()

    def __str__(self):
        return self.nome
