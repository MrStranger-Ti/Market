from django.core.cache import cache
from django.shortcuts import render
from django.http import (
    HttpRequest,
)
from django.views.generic import (
    TemplateView,
)
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
)
from .models import BannerSlider, Product, ProjectSettings


def test_view_func(request: HttpRequest):
    products = Product.objects.all()
    context = {
        "products": products
    }
    return render(request, 'banner_app/test.html', context)

class IndexTemplateView(LoginRequiredMixin, TemplateView):
    template_name = "banner_app/index.html"
    #context_object_name = 'purposes'




    def get_context_data(self, **kwargs):
        context = super(IndexTemplateView, self).get_context_data(**kwargs)

        banners_sliders = BannerSlider.objects.filter(is_active=True)
        # cache.set("banners_sliders", objects, 120)
        # banners_sliders = cache.get("banners_sliders")
        # Обращаюсь к модели хранения настроек системы которые делаются в задании [MARKET-5] Сервис настроек
        my_timeout = ProjectSettings.objects.get(name="banners_sliders_cache_timeout").banners_sliders_cache_timeout

        context['banners_sliders'] = banners_sliders
        context['banners_sliders_cache_timeout'] = my_timeout

        return context