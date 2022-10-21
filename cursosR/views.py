# Obliga a que estes logueado para poder visualizar la vista#
from django.contrib.auth.mixins import LoginRequiredMixin
# Valida los permisos
from django.core.exceptions import PermissionDenied
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Comentarios, Course, LenguajeM
# Para que te regrese a la pagina principal de una manera mas lenta
from django.urls import reverse_lazy
from django.http import HttpResponseNotFound


class cursosPageview(ListView):
    template_name = 'cursos.html'
    model = Course
    context_object_name = 'Todos_Cursos'


class cursosPageDetail(LoginRequiredMixin, DetailView):
    template_name = 'cursos_detalle.html'
    model = Course
    context_object_name = 'Todos_Cursos'
    login_url = 'login'


class cursosPageCreate(LoginRequiredMixin, CreateView):
    template_name = 'cursos_nuevo.html'
    model = Course
    fields = ('Nombre', 'Descripcion',
              'Año_Experiencia', 'Horas', 'Link_Cont', 'Lenguaje')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.Creador = self.request.user
        return super().form_valid(form)


class cursosPageUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'cursos_editar.html'
    model = Course
    fields = ['Descripcion', 'Año_Experiencia',
              'Horas', 'Link_Cont', 'Lenguaje']
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.Creador != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class cursosPageDelete(LoginRequiredMixin, DeleteView):
    template_name = 'cursos_eliminar.html'
    model = Course
    fields = "_all_"
    success_url = reverse_lazy('cursos')
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.Creador != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class lenguajePageview(ListView):
    template_name = 'lenguaje.html'
    model = LenguajeM
    context_object_name = 'Todos_Lenguajes'


class lenguajePageDetail(LoginRequiredMixin, DetailView):
    template_name = 'lenguaje_detalle.html'
    model = LenguajeM
    context_object_name = 'Todos_Lenguajes'
    login_url = 'login'


class lenguajePageCreate(LoginRequiredMixin, CreateView):
    template_name = 'lenguaje_nuevo.html'
    model = LenguajeM
    fields = ('Nom_Leng', 'Historia')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.Creador = self.request.user
        return super().form_valid(form)


class lenguajePageUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'lenguaje_editar.html'
    model = LenguajeM
    fields = ['Historia']
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        raise PermissionDenied


class lenguajePageDelete(LoginRequiredMixin, DeleteView):
    template_name = 'lenguaje_eliminar.html'
    model = LenguajeM
    fields = "_all_"
    success_url = reverse_lazy('lenguaje')
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        return HttpResponseNotFound('<h1> NO SE CUENTA CON ACCESO PARA REALIZAR ESE CAMBIO </h1>')


class comentriosPageCreate(LoginRequiredMixin, CreateView):
    template_name = 'comentarios.html'
    model = Comentarios
    fields = ('Comentario',)
    login_url = 'login'

    def form_valid(self, form):
        form.instance.NombreU = self.request.user
        form.instance.Curso_id = self.kwargs['pk']
        return super().form_valid(form)


class comentriosPageDelete(LoginRequiredMixin, DeleteView):
    template_name = 'comentarios_eliminar.html'
    model = Comentarios
    fields = "_all_"
    success_url = reverse_lazy('cursos')
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        return HttpResponseNotFound('<h1> NO SE CUENTA CON ACCESO PARA REALIZAR ESE CAMBIO </h1>')
