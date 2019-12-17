from django.http import Http404
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Event


class PermissionMixin(LoginRequiredMixin):
    def get_object(self, queryset=None):
        """
            Hook to ensure object is owned by request.user.
            check user auth before delete.
        """
        obj = super(PermissionMixin, self).get_object()
        user = self.request.user
        if obj.creator != user:
            raise Http404()
        return obj