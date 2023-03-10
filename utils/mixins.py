from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect

class IsAdminMixin: 
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and not request.user.es_admin:
            raise PermissionDenied
        return super(IsAdminMixin, self).dispatch(request, *args, **kwargs)

def is_admin_required():
    def permisos_requeridos(f):
        def check(request, *args, **kwargs):
            print(request.user.is_authenticated)
            
            if request.user.is_anonymous or (request.user.is_authenticated and not request.user.es_admin ):
                #raise PermissionDenied
                 return redirect('inicio')
                #return HttpResponseForbidden()
            return f(request, *args, **kwargs)
            
        return check
        
    return permisos_requeridos
