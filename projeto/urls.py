"""
URL configuration for projeto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


from django.urls import path
from aplicacao.views import upload_image, home, add_carrossel, adicionar_eletivas, lista, apagar_eletivas, apagar_tutoria, adicionar_tutoria, lista_tutoria,view_eletivas,add_social_links,mais_sobre,adicionar_maissobre,apagar_maissobre, add_link_eletivas, apagar_link_eletivas,  add_news_one, view_news_one, apagar_news_one, criar_evento, listar_eventos, editar_evento, apagar_evento,adicionar_noticia, editar_noticia, apagar_noticia, nossa_historia, adicionar_historia, editar_historia, deletar_historia, adicionar_noticia3, editar_noticia3, apagar_noticia3, lista_cardapios, adicionar_cardapio, editar_cardapio, apagar_cardapio, apagar_regularlanche, editar_regularlanche, adicionar_regularlanche, adicionar_regularalmoco, editar_regularalmoco, apagar_regularalmoco, adicionar_eja, editar_eja, apagar_eja, view_news_two, matricula, calendario
urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload_image/', upload_image, name='upload_image'),
    path('add_carrossel/', add_carrossel, name='add_carrossel'),
    path('adicionar_eletivas/', adicionar_eletivas, name='adicionar_eletivas'),
    path('lista/', lista, name='lista'),
    path('<int:eletiva_id>eletiva/', apagar_eletivas, name='apagar_eletivas'),
    path('<int:tutoria_id>tutoria/', apagar_tutoria, name='apagar_tutoria'),
    path('adicionar_tutoria/', adicionar_tutoria, name='adicionar_tutoria'),
    path('lista_tutoria/', lista_tutoria, name='lista_tutoria'),
    path('', home, name='home'),
    path('<int:eletiva_id>/', view_eletivas, name='view_eletivas'),
    path('add_social_links/', add_social_links, name='add_social_links'),
    path('mais_sobre/', mais_sobre, name='mais_sobre'),
    path('adicionar_maissobre/', adicionar_maissobre, name='adicionar_maissobre'),
    path('<int:maissobre_id>maissobre/', apagar_maissobre, name='apagar_maissobre'),
    path('add_link_eletivas/', add_link_eletivas, name='add_link_eletivas'),
    path('delete/<int:link_id>/', apagar_link_eletivas, name='apagar_link_eletivas'),
    path('add_news_one/', add_news_one, name='add_news_one'),
    path('/<int:noticia_id>/', view_news_one, name='view_news_one'),
    path('<int:noticia_id>noticia/', apagar_news_one, name='apagar_news_one'),
    path('criar/', criar_evento, name='criar_evento'),
    path('lista_eventos/', listar_eventos, name='listar_eventos'),
    path('editar/<int:id>/', editar_evento, name='editar_evento'),
    path('apagar/<int:id>/', apagar_evento, name='apagar_evento'),
    path('adicionar/', adicionar_noticia, name='adicionar_noticia'),
    path('editar/<int:id>/', editar_noticia, name='editar_noticia'),
    path('apagar<int:id>/', apagar_noticia, name='apagar_noticia'),
    path('/<int:id>/', view_news_two, name='view_news_two'),
    path('nossa_historia/', nossa_historia, name='nossa_historia'),
    path('adicionar_historia/', adicionar_historia, name='adicionar_historia'),
    path('editar<int:pk>/', editar_historia, name='editar_historia'),
    path('deletar<int:pk>/', deletar_historia, name='deletar_historia'),
    path('adicionar_noticia3/', adicionar_noticia3, name='adicionar_noticia3'),
    path('editar3<int:id>/', editar_noticia3, name='editar_noticia3'),
    path('apagar3/<int:id>/', apagar_noticia3, name='apagar_noticia3'),
    path('lista_cardapios/', lista_cardapios, name='lista_cardapios'),
    path('adicionar_cardapio/', adicionar_cardapio, name='adicionar_cardapio'),
    path('editar_cardapio<int:id>/', editar_cardapio, name='editar_cardapio'),
    path('apagar_cardapio<int:id>/', apagar_cardapio, name='apagar_cardapio'),
    path('adicionar_regularlanche/', adicionar_regularlanche, name='adicionar_regularlanche'),  # Adicionar regular lanche
    path('editar_regularlanche<int:pk>/', editar_regularlanche, name='editar_regularlanche'),  # Editar regular lanche
    path('apagar_regularlanche<int:pk>/', apagar_regularlanche, name='apagar_regularlanche'),  # Apagar regular lanche
    path('adicionar_regularalmoco/', adicionar_regularalmoco, name='adicionar_regularalmoco'),  # Adicionar regular almoço
    path('editar_regularalmoco<int:pk>/', editar_regularalmoco, name='editar_regularalmoco'),  # Editar regular almoço
    path('apagar_regularalmoco<int:pk>/', apagar_regularalmoco, name='apagar_regularalmoco'),  # Apagar regular almoço
    path('adicionar_eja/', adicionar_eja, name='adicionar_eja'),  # Adicionar regular lanche
    path('editar_eja/', editar_eja, name='editar_eja'),  # Editar regular lanche
    path('apagar_eja<int:pk>/', apagar_eja, name='apagar_eja'),  # Apagar regular lanche
    path('matricula/', matricula, name='matricula'),
    path('calendario/', calendario, name='calendario')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)