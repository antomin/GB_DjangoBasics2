from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.views.generic.base import ContextMixin, View


class AddContextMixin(ContextMixin):
    title = ''

    def get_context_data(self, **kwargs):
        context = super(AddContextMixin, self).get_context_data(**kwargs)
        context['title'] = self.title
        return context


class SuperUserRequiredMixin(View):
    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(SuperUserRequiredMixin, self).dispatch(request, *args, **kwargs)
