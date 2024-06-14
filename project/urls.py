from django.urls import path
from.import views

urlpatterns=[
    path('form/',views.sample,name='upload'),
    path('',views.hmpage,name='homes'),
    path('menspage/',views.menpage,name='mens'),
    path('womenspage/',views.womenpage,name='womens'),
    path('kidpage/',views.kidspage,name='kids'),
    path('homeliv/',views.hmlvngpage,name='hlvng'),
    path('beautyspage/',views.beautypage,name='beautys'),
    path('studpage/',views.studiopage,name='studs'),
    path('hooman/',views.bohoo,name='hoomans'),
    path('prdctdetail/(?P<pk>)/',views.bohoodetails,name='prdet'),
    path('usp/',views.uspopage,name='polo'),
    path('lgin/',views.logpage,name='lginpg'),
    path('shbag/',views.shopbag,name='shpbag'),
    path('insert/<int:id>/',views.insert_shoppingbagView,name='insert_shpbag'),
    path('remove/<int:id>/',views.remove,name='remove'),
    path('register/',views.registration,name='register'),
    path('lgout/',views.logoutView,name='lgout')
]

