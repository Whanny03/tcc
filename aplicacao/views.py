from django.shortcuts import render, redirect, get_object_or_404
from .forms import ImageCarouselForm, EletivaForm, TutoriaForm, SocialLinksForm, MaisSobreForm, LinkEletivaForm,HistoriaForm, NewsOneForm, EventoForm, Noticia2Form, Noticia3Form, IntegradoForm, RegularLancheForm, RegularAlmocoForm
from .models import  ImgCarrossel, Eletiva, Tutoria, SocialLinks, ImageCarousel, MaisSobre, LinkEletiva,Historia, NewsOne, Evento, Noticia2, Noticia3, Integrado, RegularLanche, RegularAlmoco

#Pagina inicial
def home(request):
    images = ImgCarrossel.objects.all().values()
    print(images)
    social_link = SocialLinks.objects.all().values()
    newsone = NewsOne.objects.all().order_by('-date_published')
    noticias = Noticia2.objects.all()
    noticia3 = Noticia3.objects.all()
    return render(request, 'home.html', {'images': images,'social_link':social_link,  'newsone': newsone, 'noticias': noticias, 'noticia3': noticia3})



def upload_image(request):
    if request.method == 'POST':
        form = ImageCarouselForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ImageCarouselForm()
    return render(request, 'upload_image.html', {'form': form})



#CARROSSEL
def add_carrossel(request):
    if request.method == 'POST':
        image1 = request.FILES.get('image1')
        image2 = request.FILES.get('image2')
        image3 = request.FILES.get('image3')
        ImgCarrossel.objects.all().delete()
        carrossel=ImgCarrossel(image1=image1, image2=image2, image3=image3)
        carrossel.save()
      
        
        return redirect(home)
    else:
        return render(request,'add_carrossel.html')
    
    
    
 #ELETIVAS
def lista(request):
    eletivas = Eletiva.objects.all()
    link = LinkEletiva.objects.all()
    return render(request, 'eletivas/lista.html', {'eletivas': eletivas , 'link': link})

def adicionar_eletivas(request):
    if request.method == 'POST':
        form = EletivaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista')
    else:
        form = EletivaForm()
    return render(request, 'eletivas/adicionar_eletivas.html', {'form': form})

def apagar_eletivas(request, eletiva_id):
    eletiva = get_object_or_404(Eletiva, pk=eletiva_id)
    if request.method == 'POST':
        eletiva.delete()
        return redirect('lista')
    return render(request, 'eletivas/apagar_eletivas.html', {'eletiva': eletiva})

def view_eletivas(request, eletiva_id):
    eletiva = get_object_or_404(Eletiva, pk=eletiva_id)
    return render(request, 'eletivas/view_eletivas.html', {'eletiva': eletiva})

# Link para inscrever eletivas

def add_link_eletivas(request):
    if request.method == "POST":
        form = LinkEletivaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista')
    else:
        form = LinkEletivaForm()

    return render(request, 'eletivas/add_link_eletivas.html', {'form': form})

def apagar_link_eletivas(request, link_id):
    link = get_object_or_404(LinkEletiva, pk=link_id)
    if request.method == 'POST':
        link.delete()
        return redirect('lista')
    return render(request, 'eletivas/apagar_link_eletivas.html', {'link': link})
#tutoria

def lista_tutoria(request):
    tutorias = Tutoria.objects.all()
    return render(request, 'lista_tutoria.html', {'tutorias': tutorias})

def adicionar_tutoria(request):
    if request.method == 'POST':
        form = TutoriaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_tutoria')
    else:
        form = TutoriaForm()
    return render(request, 'adicionar_tutoria.html', {'form': form})

def apagar_tutoria(request, tutoria_id):
    tutorias = get_object_or_404(Tutoria, pk=tutoria_id)
    if request.method == 'POST':
        tutorias.delete()
        return redirect('lista_tutoria')
    return render(request, 'apagar_tutoria.html', {'tutorias': tutorias})

# Link

def add_social_links(request):
    if request.method == "POST":
        form = SocialLinksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirecione para onde você quiser
    else:
        form = SocialLinksForm()

    return render(request, 'add_social_links.html', {'form': form})

# MaisSobre

def mais_sobre(request):
    maissobre = MaisSobre.objects.all()
    return render(request, 'mais_sobre.html', {'maissobre': maissobre})

def adicionar_maissobre(request):
    if request.method == 'POST':
        form = MaisSobreForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('mais_sobre')
    else:
        form = MaisSobreForm()
    return render(request, 'adicionar_maissobre.html', {'form': form})


def apagar_maissobre(request, maissobre_id):
    maissobre = get_object_or_404(MaisSobre, pk=maissobre_id)
    if request.method == 'POST':
        maissobre.delete()
        return redirect('mais_sobre')
    return render(request, 'apagar_maissobre.html', {'maissobre': maissobre})


# Evento

def criar_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_eventos')  # redireciona para a página de eventos
    else:
        form = EventoForm()

    return render(request, 'evento/criar_evento.html', {'form': form})

def listar_eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'evento/listar_eventos.html', {'eventos': eventos})

def editar_evento(request, id):
    evento = get_object_or_404(Evento, id=id)
    
    if request.method == 'POST':
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            return redirect('listar_eventos')  # Redireciona para a página de listagem de eventos após a edição
    else:
        form = EventoForm(instance=evento)
    
    return render(request, 'evento/editar_evento.html', {'form': form, 'evento': evento})

def apagar_evento(request, id):
    evento = get_object_or_404(Evento, id=id)
    
    if request.method == 'POST':
        evento.delete()
        return redirect('listar_eventos')  # Redireciona para a página de listagem de eventos após a exclusão
    
    return render(request, 'evento/apagar_evento.html', {'evento': evento})



# Nossa história

def adicionar_historia(request):
    if request.method == 'POST':
        form = HistoriaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('nossa_historia')
    else:
        form = HistoriaForm()
    return render(request, 'historia/adicionar_historia.html', {'form': form})

def editar_historia(request, pk):
    historia = get_object_or_404(Historia, pk=pk)
    if request.method == 'POST':
        form = HistoriaForm(request.POST, request.FILES, instance=historia)
        if form.is_valid():
            form.save()
            return redirect('nossa_historia')
    else:
        form = HistoriaForm(instance=historia)
    return render(request, 'historia/editar_historia.html', {'form': form})

def deletar_historia(request, pk):
    historia = get_object_or_404(Historia, pk=pk)
    if request.method == 'POST':
        historia.delete()
        return redirect('nossa_historia')
    return render(request, 'historia/deletar_historia.html', {'historia': historia})

def nossa_historia(request):
    historias = Historia.objects.all()
    return render(request, 'historia/nossa_historia.html', {'historias': historias})



#NOTICIAS 1

def add_news_one(request):
    if request.method == 'POST':
        form = NewsOneForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NewsOneForm()
    return render(request, 'noticia1/add_news_one.html', {'form': form})


def view_news_one(request, noticia_id):
    newsone = get_object_or_404(NewsOne, pk=noticia_id)
    return render(request, 'noticia1/view_news_one.html', {'noticia': newsone})


#apagar
def apagar_news_one(request, noticia_id):
    newsone = get_object_or_404(NewsOne, pk=noticia_id)
    if request.method == 'POST':
        newsone.delete()
        return redirect('home')
    return render(request, 'noticia1/apagar_news_one.html', {'noticia': newsone})


# NOTICIA 2
def adicionar_noticia(request):
    if request.method == 'POST':
        form = Noticia2Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = Noticia2Form()
    return render(request, 'noticia2/adicionar_noticia.html', {'form': form})

def editar_noticia(request, id):
    noticia = get_object_or_404(Noticia2, id=id)
    if request.method == 'POST':
        form = Noticia2Form(request.POST, request.FILES, instance=noticia)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = Noticia2Form(instance=noticia)
    return render(request, 'noticia2/editar_noticia.html', {'form': form, 'noticia': noticia})

def apagar_noticia(request, id):
    noticia = get_object_or_404(Noticia2, id=id)
    if request.method == 'POST':
        noticia.delete()
        return redirect('home')
    return render(request, 'noticia2/apagar_noticia.html', {'noticia': noticia})



# NOTICIA 3
def adicionar_noticia3(request):
    if request.method == 'POST':
        form = Noticia3Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = Noticia3Form()
    return render(request, 'noticia3/adicionar_noticia3.html', {'form': form})

def editar_noticia3(request, id):
    noticia = get_object_or_404(Noticia3, id=id)
    if request.method == 'POST':
        form = Noticia3Form(request.POST, request.FILES, instance=noticia)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = Noticia3Form(instance=noticia)
    return render(request, 'noticia3/editar_noticia3.html', {'form': form, 'noticia': noticia})

def apagar_noticia3(request, id):
    noticia = get_object_or_404(Noticia3, id=id)
    if request.method == 'POST':
        noticia.delete()
        return redirect('home')
    return render(request, 'noticia3/apagar_noticia3.html', {'noticia': noticia})


# CARDAPIO
# View para adicionar um cardápio
def adicionar_cardapio(request):
    if request.method == 'POST':
        form = IntegradoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_cardapios')  # Redireciona para a lista de cardápios
    else:
        form = IntegradoForm()
    return render(request, 'cardapio/adicionar_cardapio.html', {'form': form})

# View para editar um cardápio
def editar_cardapio(request, id):
    cardapio = get_object_or_404(Integrado, id=id)
    if request.method == 'POST':
        form = IntegradoForm(request.POST, request.FILES, instance=cardapio)
        if form.is_valid():
            form.save()
            return redirect('lista_cardapios')
    else:
        form = IntegradoForm(instance=cardapio)
    return render(request, 'cardapio/editar_cardapio.html', {'form': form, 'cardapio': cardapio})

# View para apagar um cardápio
def apagar_cardapio(request, id):
    cardapio = get_object_or_404(Integrado, id=id)
    if request.method == 'POST':
        cardapio.delete()
        return redirect('lista_cardapios')
    return render(request, 'cardapio/apagar_cardapio.html', {'cardapio': cardapio})

# View para listar os cardápios
def lista_cardapios(request):
    cardapios = Integrado.objects.all()
    regularlanches = RegularLanche.objects.all()
    regularalmocos = RegularAlmoco.objects.all()
    return render(request, 'cardapio/lista_cardapios.html', {'cardapios': cardapios, 'regularlanches': regularlanches, 'regularalmocos': regularalmocos})


# REGULAR 
# regular lanche

# View para adicionar um novo cardápio
def adicionar_regularlanche(request):
    if request.method == 'POST':
        form = RegularLancheForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_cardapios')
    else:
        form = RegularLancheForm()
    return render(request, 'cardapio/adicionar_regularlanche.html', {'form': form})

# View para editar um cardápio existente
def editar_regularlanche(request, pk):
    cardapio = get_object_or_404(RegularLanche, pk=pk)
    if request.method == 'POST':
        form = RegularLancheForm(request.POST, request.FILES, instance=cardapio)
        if form.is_valid():
            form.save()
            return redirect('lista_cardapios')
    else:
        form = RegularLancheForm(instance=cardapio)
    return render(request, 'cardapio/editar_regularlanche.html', {'form': form})

# View para apagar um cardápio existente
def apagar_regularlanche(request, pk):
    cardapio = get_object_or_404(RegularLanche, pk=pk)
    if request.method == 'POST':
        cardapio.delete()
        return redirect('lista_cardapios')
    return render(request, 'cardapio/apagar_regularlanche.html', {'cardapio': cardapio})

# regular almoço

# Adicionar cardápio
def adicionar_regularalmoco(request):
    if request.method == 'POST':
        form = RegularAlmocoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_cardapios')
    else:
        form = RegularAlmocoForm()
    return render(request, 'cardapio/adicionar_regularalmoco.html', {'form': form})

# Editar cardápio
def editar_regularalmoco(request, pk):
    cardapio = get_object_or_404(RegularAlmoco, pk=pk)
    if request.method == 'POST':
        form = RegularAlmocoForm(request.POST, request.FILES, instance=cardapio)
        if form.is_valid():
            form.save()
            return redirect('lista_cardapios')
    else:
        form = RegularAlmocoForm(instance=cardapio)
    return render(request, 'cardapio/editar_regularalmoco.html', {'form': form})

# Apagar cardápio
def apagar_regularalmoco(request, pk):
    cardapio = get_object_or_404(RegularAlmoco, pk=pk)
    if request.method == 'POST':
        cardapio.delete()
        return redirect('lista_cardapios')
    return render(request, 'cardapio/apagar_regularalmoco.html', {'cardapio': cardapio})
