from django.urls import path
from Firstapp import views

urlpatterns=[
    #Welcome admin Page
    path('admin_welcome/',views.welcome_admin),

    #IT JOBS
    path('dashboard/',views.dashboard),
    path('it_show/',views.it_show),
    path('it_add/',views.it_add),
    path('it_update/<int:id>/',views.it_update),
    path('it_delete/<int:id>/',views.it_delete),

    #MECHANICAL JOBS
    path('mech_show/',views.mech_show),
    path('mech_add/',views.mech_add),
    path('mech_update/<int:id>/',views.mech_update),
    path('mech_delete/<int:id>/',views.mech_delete),

    #CIVIL JOBS
    path('civil_show/',views.civil_show),
    path('civil_add/',views.civil_add),
    path('civil_update/<int:id>/',views.civil_update),
    path('civil_delete/<int:id>/',views.civil_delete),

    #show resume
    path('show_resume/<int:id>/',views.showresume),
    path('mech_show_resume/<int:id>/',views.mech_showresume),
    path('civil_show_resume/<int:id>/',views.civil_showresume)



]