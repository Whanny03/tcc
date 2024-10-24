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

class Historia(models.Model):
    nome = models.CharField(max_length=255)
    data = models.DateField()
    imagem = models.ImageField(upload_to='imagens/')

    def __str__(self):
        return self.nome

    
class NewsOne(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    description_2 = models.TextField()
    image = models.ImageField(upload_to='news_images/', null=True)
    date_published = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

class Noticia2(models.Model):
    titulo = models.CharField(max_length=200)
    descricao1 = models.TextField()
    descricao2 = models.TextField()
    imagem = models.ImageField(upload_to='news_images/')
    data_publicacao = models.DateField()

    def __str__(self):
        return self.titulo

class Noticia3(models.Model):
    title = models.CharField(max_length=255)
    description1 = models.TextField()
    description2 = models.TextField()
    image = models.ImageField(upload_to='news_images/')
    data_publicacao = models.DateField()
    

class Evento(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    data = models.TextField(null=True)
    hora = models.TimeField()

    def __str__(self):
        return self.nome

class Integrado(models.Model):
    nome_semana = models.CharField(max_length=50)
    foto_cardapio = models.ImageField(upload_to='fotos_cardapio/')
    nome_comida = models.CharField(max_length=100)
    data_cardapio = models.DateField()

    def __str__(self):
        return f'{self.nome_semana} - {self.nome_comida}'

    class Meta:
        verbose_name = 'Cardápio Integrado'
        verbose_name_plural = 'Cardápios Integrados'

class RegularLanche(models.Model):
    nome_dia_semana = models.CharField(max_length=20)  # Nome do dia da semana (e.g. Segunda-feira)
    nome_comida = models.CharField(max_length=100)  # Nome da comida
    imagem = models.ImageField(upload_to='lanche_imagens/')  # Campo de imagem
    data_cardapio = models.DateField()  # Data do cardápio

    def __str__(self):
        return f"{self.nome_dia_semana}: {self.nome_comida} ({self.data_cardapio})"


class RegularAlmoco(models.Model):
    dia_da_semana = models.CharField(max_length=100, null=True)  # Ex: 'Segunda'
    nome_da_comida = models.CharField(max_length=100)  # Ex: 'Arroz com Feijão'
    imagem = models.ImageField(upload_to='imagens/')  # Ex: 'imagem.jpg'
    data_do_cardapio = models.DateField()  # Ex: '2024-10-22'

    def __str__(self):
        return f"{self.dia_da_semana} - {self.nome_da_comida}"
