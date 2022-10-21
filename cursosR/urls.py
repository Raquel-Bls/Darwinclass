from django.urls import path
from .views import cursosPageview, cursosPageDetail, cursosPageCreate, cursosPageUpdate, cursosPageDelete
from .views import lenguajePageview, lenguajePageDetail, lenguajePageCreate, lenguajePageUpdate, lenguajePageDelete, comentriosPageCreate, comentriosPageDelete

urlpatterns = [
    # ---------------------CURSOS-------------
    path('cursos/', cursosPageview.as_view(), name='cursos'),
    path('cursos/<int:pk>', cursosPageDetail.as_view(), name='cursos_detalle'),
    path('cursos/nuevo', cursosPageCreate.as_view(), name='cursos_nuevo'),
    path('cursos/<int:pk>/editar/',
         cursosPageUpdate.as_view(), name='cursos_editar'),
    path('cursos/<int:pk>/eliminar/',
         cursosPageDelete.as_view(), name='cursos_eliminar'),
    # -----------------------LENGUAJES------------
    path('lenguaje/', lenguajePageview.as_view(), name='lenguaje'),
    path('lenguaje/<int:pk>', lenguajePageDetail.as_view(), name='lenguaje_detalle'),
    path('lenguaje/nuevo', lenguajePageCreate.as_view(), name='lenguaje_nuevo'),
    path('lenguaje/<int:pk>/editar/',
         lenguajePageUpdate.as_view(), name='lenguaje_editar'),
    path('lenguaje/<int:pk>/eliminar/',
         lenguajePageDelete.as_view(), name='lenguaje_eliminar'),
    # --------------------COMENTARIOS------------
    path('<int:pk>/comentarios/',
         comentriosPageCreate.as_view(), name='comentarios'),
    path('comentarios/<int:pk>/eliminar/',
         comentriosPageDelete.as_view(), name='comentarios_eliminar'),
]
