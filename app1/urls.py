
from django.contrib import admin
from django.urls import path
from . import views
from .views import serve_image

urlpatterns = [
    path("admin/", admin.site.urls ),
    path("",views.home,name='home'),
    path("coment/",views.coment, name='coment'),
    path("help/",views.help, name='help'),
    path('images/<str:image_name>/', views.serve_image, name='serve_image'),
    path("year/",views.year, name='year'),
    path("firstyear/",views.first_year_electrical, name='electrical'),
    path("coarses1/",views.coarses1,name='coarses'),
    path("el_sem/",views.elec_sem,name='elec_sem'),
    path("civ_sem/",views.civil,name='civil'),
    path("civ/",views.civil_sem,name='civil_sem'),
    path("mech_sem/",views.mechanical,name='mechanical'),
    path("mech/",views.mech_sem,name='mech_sem'),
    path("met_sem/",views.metallugy,name='metallugy'),
    path("met/",views.met_sem,name='met_sem'),
    path("quant_sem/",views.quantity,name='quantity'),
    path("quantity/",views.quantity_sem,name='quantity_sem'),
    path("industrial_sem/",views.industrial,name='industrial'),
    path("industrial/",views.industrial_sem,name='industrial_sem'),
    path("textile_sem/",views.textile,name='textile'),
    path("textile/",views.textile_sem,name='textile_sem'),
    path("chem_sem/",views.chemical,name='chemical'),
    path("chemical/",views.chemical_sem,name='chemical_sem'),

]
