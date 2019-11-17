from django.shortcuts import render
from django.views.generic.base import View

from .models import Category


class HomeView(View):
    """Home page"""
    def get(self, request):
        category_list = Category.objects.all()
        return render(request, "blog/home.html", {"categories": category_list})


class CategoryView(View):
    """Вывод статей категории"""
    def get(self, request, category_name):
        category = Category.objects.get(slug=category_name)
        return render(request, "blog/post_list.html", {"category": category})