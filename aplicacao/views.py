from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from .forms import ImageCarouselForm, EletivaForm, TutoriaForm, SocialLinksForm, MaisSobreForm, LinkEletivaForm,HistoriaForm, NewsOneForm, EventoForm, Noticia2Form, Noticia3Form, IntegradoForm, RegularLancheForm, RegularAlmocoForm, EjaForm, DiretorForm
from .models import  ImgCarrossel, Eletiva, Tutoria, SocialLinks, ImageCarousel, MaisSobre, LinkEletiva,Historia, NewsOne, Evento, Noticia2, Noticia3, Integrado, RegularLanche, RegularAlmoco, Eja, Diretor

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
            return redirect('area_diretor')
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
            return redirect('area_diretor')
    else:
        form = EletivaForm()
    return render(request, 'eletivas/adicionar_eletivas.html', {'form': form})

def apagar_eletivas(request, eletiva_id):
    eletiva = get_object_or_404(Eletiva, pk=eletiva_id)
    if request.method == 'POST':
        eletiva.delete()
        return redirect('area_diretor')
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
            return redirect('area_diretor')
    else:
        form = LinkEletivaForm()

    return render(request, 'eletivas/add_link_eletivas.html', {'form': form})

def apagar_link_eletivas(request, link_id):
    link = get_object_or_404(LinkEletiva, pk=link_id)
    if request.method == 'POST':
        link.delete()
        return redirect('area_diretor')
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
            return redirect('adicionar_tutoria')
    else:
        form = TutoriaForm()
    return render(request, 'adicionar_tutoria.html', {'form': form})

def apagar_tutoria(request, tutoria_id):
    tutorias = get_object_or_404(Tutoria, pk=tutoria_id)
    if request.method == 'POST':
        tutorias.delete()
        return redirect('area_diretor')
    return render(request, 'apagar_tutoria.html', {'tutorias': tutorias})

# Link

def add_social_links(request):
    if request.method == "POST":
        form = SocialLinksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('area_diretor')  # Redirecione para onde você quiser
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
            return redirect('adicionar_maissobre')
    else:
        form = MaisSobreForm()
    return render(request, 'adicionar_maissobre.html', {'form': form})


def apagar_maissobre(request, maissobre_id):
    maissobre = get_object_or_404(MaisSobre, pk=maissobre_id)
    if request.method == 'POST':
        maissobre.delete()
        return redirect('area_diretor')
    return render(request, 'apagar_maissobre.html', {'maissobre': maissobre})


# Evento

def criar_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('area_diretor')  # redireciona para a página de eventos
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
            return redirect('area_diretor')  # Redireciona para a página de listagem de eventos após a edição
    else:
        form = EventoForm(instance=evento)
    
    return render(request, 'evento/editar_evento.html', {'form': form, 'evento': evento})

def apagar_evento(request, id):
    evento = get_object_or_404(Evento, id=id)
    
    if request.method == 'POST':
        evento.delete()
        return redirect('area_diretor')  # Redireciona para a página de listagem de eventos após a exclusão
    
    return render(request, 'evento/apagar_evento.html', {'evento': evento})



# Nossa história

def adicionar_historia(request):
    if request.method == 'POST':
        form = HistoriaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('area_diretor')
    else:
        form = HistoriaForm()
    return render(request, 'historia/adicionar_historia.html', {'form': form})

def editar_historia(request, pk):
    historia = get_object_or_404(Historia, pk=pk)
    if request.method == 'POST':
        form = HistoriaForm(request.POST, request.FILES, instance=historia)
        if form.is_valid():
            form.save()
            return redirect('area_diretor')
    else:
        form = HistoriaForm(instance=historia)
    return render(request, 'historia/editar_historia.html', {'form': form})

def deletar_historia(request, pk):
    historia = get_object_or_404(Historia, pk=pk)
    if request.method == 'POST':
        historia.delete()
        return redirect('area_diretor')
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
            return redirect('area_diretor')
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
        return redirect('area_diretor')
    return render(request, 'noticia1/apagar_news_one.html', {'noticia': newsone})


# NOTICIA 2
def adicionar_noticia(request):
    if request.method == 'POST':
        form = Noticia2Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('area_diretor')
    else:
        form = Noticia2Form()
    return render(request, 'noticia2/adicionar_noticia.html', {'form': form})

def editar_noticia(request, id):
    noticia = get_object_or_404(Noticia2, id=id)
    if request.method == 'POST':
        form = Noticia2Form(request.POST, request.FILES, instance=noticia)
        if form.is_valid():
            form.save()
            return redirect('area_diretor')
    else:
        form = Noticia2Form(instance=noticia)
    return render(request, 'noticia2/editar_noticia.html', {'form': form, 'noticia': noticia})

def apagar_noticia(request, id):
    noticia = get_object_or_404(Noticia2, id=id)
    if request.method == 'POST':
        noticia.delete()
        return redirect('area_diretor')
    return render(request, 'noticia2/apagar_noticia.html', {'noticia': noticia})

def view_news_two(request, id):
    noticia = get_object_or_404(Noticia2, pk=id)
    return render(request, 'noticia2/view_news_two.html', {'noticia': noticia})

# NOTICIA 3
def adicionar_noticia3(request):
    if request.method == 'POST':
        form = Noticia3Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('area_diretor')
    else:
        form = Noticia3Form()
    return render(request, 'noticia3/adicionar_noticia3.html', {'form': form})

def editar_noticia3(request, id):
    noticia = get_object_or_404(Noticia3, id=id)
    if request.method == 'POST':
        form = Noticia3Form(request.POST, request.FILES, instance=noticia)
        if form.is_valid():
            form.save()
            return redirect('area_diretor')
    else:
        form = Noticia3Form(instance=noticia)
    return render(request, 'noticia3/editar_noticia3.html', {'form': form, 'noticia': noticia})

def apagar_noticia3(request, id):
    noticia = get_object_or_404(Noticia3, id=id)
    if request.method == 'POST':
        noticia.delete()
        return redirect('area_diretor')
    return render(request, 'noticia3/apagar_noticia3.html', {'noticia': noticia})

def view_news_3(request,id):
    noticia = get_object_or_404(Noticia3, pk=id)
    return render(request, 'noticia3/view_news_tres.html', {'noticia': noticia})

# INTEGRADO
# View para adicionar um cardápio DO INTEGRADO
def adicionar_cardapio(request):
    if request.method == 'POST':
        form = IntegradoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('area_diretor')  # Redireciona para a lista de cardápios
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
            return redirect('area_diretor')
    else:
        form = IntegradoForm(instance=cardapio)
    return render(request, 'cardapio/editar_cardapio.html', {'form': form, 'cardapio': cardapio})

# View para apagar um cardápio
def apagar_cardapio(request, id):
    cardapio = get_object_or_404(Integrado, id=id)
    if request.method == 'POST':
        cardapio.delete()
        return redirect('area_diretor')
    return render(request, 'cardapio/apagar_cardapio.html', {'cardapio': cardapio})

# View para listar os cardápios
def lista_cardapios(request):
    cardapios = Integrado.objects.all()
    regularlanches = RegularLanche.objects.all()
    regularalmocos = RegularAlmoco.objects.all()
    ejacardapio = Eja.objects.all()
    return render(request, 'cardapio/lista_cardapios.html', {'cardapios': cardapios, 'regularlanches': regularlanches, 'regularalmocos': regularalmocos , 'ejacardapio': ejacardapio})


# REGULAR 
# regular lanche

# View para adicionar um novo cardápio
def adicionar_regularlanche(request):
    if request.method == 'POST':
        form = RegularLancheForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('adicionar_regularlanche')
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
            return redirect('area_diretor')
    else:
        form = RegularLancheForm(instance=cardapio)
    return render(request, 'cardapio/editar_regularlanche.html', {'form': form})

# View para apagar um cardápio existente
def apagar_regularlanche(request, pk):
    cardapio = get_object_or_404(RegularLanche, pk=pk)
    if request.method == 'POST':
        cardapio.delete()
        return redirect('area_diretor')
    return render(request, 'cardapio/apagar_regularlanche.html', {'cardapio': cardapio})

# regular almoço

# Adicionar cardápio
def adicionar_regularalmoco(request):
    if request.method == 'POST':
        form = RegularAlmocoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('area_diretor')
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
            return redirect('area_diretor')
    else:
        form = RegularAlmocoForm(instance=cardapio)
    return render(request, 'cardapio/editar_regularalmoco.html', {'form': form})

# Apagar cardápio
def apagar_regularalmoco(request, pk):
    cardapio = get_object_or_404(RegularAlmoco, pk=pk)
    if request.method == 'POST':
        cardapio.delete()
        return redirect('area_diretor')
    return render(request, 'cardapio/apagar_regularalmoco.html', {'cardapio': cardapio})


# Eja 

def adicionar_eja(request):
    if request.method == 'POST':
        form = EjaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('area_diretor')
    else:
        form = EjaForm()
    return render(request, 'cardapio/adicionar_eja.html', {'form': form})

# View para editar um cardápio existente
def editar_eja(request, pk):
    cardapio = get_object_or_404(Eja, pk=pk)
    if request.method == 'POST':
        form = EjaForm(request.POST, request.FILES, instance=cardapio)
        if form.is_valid():
            form.save()
            return redirect('area_diretor')
    else:
        form = EjaForm(instance=cardapio)
    return render(request, 'cardapio/editar_eja.html', {'form': form})

# View para apagar um cardápio existente
def apagar_eja(request, pk):
    cardapio = get_object_or_404(Eja, pk=pk)
    if request.method == 'POST':
        cardapio.delete()
        return redirect('area_diretor')
    return render(request, 'cardapio/apagar_eja.html', {'cardapio': cardapio})

def matricula(request):
    return render(request, 'matricula.html')

def calendario(request):
    return render(request, 'calendario/calendario.html')

def agenda(request):
    return render(request, 'area_diretor/agenda.html')

def registrar_diretor(request):
    if request.method == 'POST':
        form = DiretorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_diretor')
    else:
        form = DiretorForm()
    return render(request, 'area_diretor/registrar_diretor.html', {'form': form})

def login_diretor(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['senha']
        
        diretor = Diretor.objects.filter(nome=nome, email=email).first()
        if diretor and diretor.check_password(senha):
            login(request, diretor)
            return redirect('area_diretor')
        else:
            return render(request, 'area_diretor/login_diretor.html', {'erro': 'Credenciais inválidas'})
    return render(request, 'area_diretor/login_diretor.html')

def area_diretor(request):
    newsone = NewsOne.objects.all().order_by('-date_published')
    noticias = Noticia2.objects.all()
    noticia3 = Noticia3.objects.all()
    
    cardapios = Integrado.objects.all()
    regularlanches = RegularLanche.objects.all()
    regularalmocos = RegularAlmoco.objects.all()
    ejacardapio = Eja.objects.all()
    
    eventos = Evento.objects.all()
    
    tutorias = Tutoria.objects.all()
    
    maissobre = MaisSobre.objects.all()
    
    eletivas = Eletiva.objects.all()
    link = LinkEletiva.objects.all()
    return render(request, 'area_diretor/area_diretor.html', {'newsone': newsone, 'noticias': noticias, 'noticia3': noticia3, 'cardapios': cardapios, 'regularlanches': regularlanches, 'regularalmocos': regularalmocos , 'ejacardapio': ejacardapio, 'eventos': eventos, 'tutorias': tutorias, 'eletivas': eletivas , 'link': link, 'maissobre': maissobre})

def lista_eventos_diretor(request):
    eventos = Evento.objects.all()
    return render(request, 'area_diretor/lista_eventos_diretor.html', {'eventos': eventos})

def lista_noticia1(request):
    newsone = NewsOne.objects.all().order_by('-date_published')
    return render(request, 'area_diretor/lista_noticia1.html', {'newsone': newsone})

def lista_noticia2(request):
    noticias = Noticia2.objects.all()
    return render(request, 'area_diretor/lista_noticia2.html', {'noticias': noticias})

def lista_noticia3(request):
    noticia3 = Noticia3.objects.all()
    return render(request, 'area_diretor/lista_noticia3.html', {'noticia3': noticia3})

def lista_integrado(request):
    cardapios = Integrado.objects.all()
    return render(request, 'area_diretor/lista_integrado.html', {'cardapios': cardapios})

def lista_regular_lanche(request):
    regularlanches = RegularLanche.objects.all()
    return render(request, 'area_diretor/lista_regular_lanche.html', {'regularlanches':regularlanches})

def lista_regular_almoco(request):
    regularalmocos = RegularAlmoco.objects.all()
    return render(request, 'area_diretor/lista_regular_almoco.html', {'regularalmocos': regularalmocos})

def lista_eja(request):
    ejacardapio = Eja.objects.all()
    return render(request, 'area_diretor/lista_eja.html', {'ejacardapio': ejacardapio})

def lista_eletivas_diretor(request):
    eletivas = Eletiva.objects.all()
    link = LinkEletiva.objects.all()
    return render(request, 'area_diretor/lista_eletivas.html', {'eletivas': eletivas, 'link': link})

def lista_historia(request):
    historia = Historia.objects.all()
    return render(request, 'area_diretor/lista_historia.html', {'historia':historia})

def lista_mais(request):
    maissobre = MaisSobre.objects.all()
    return render(request, 'area_diretor/lista_mais.html', {'mais': maissobre})

def lista_tutorias_diretor(request):
    tutorias = Tutoria.objects.all()
    return render(request, 'area_diretor/lista_tutoria_diretor.html', {'tutorias': tutorias})