from django.shortcuts import render, get_object_or_404
from .models import Post, Category, Adv
from django.db.models import Q

# ----------------------
# Главная страница
# ----------------------
def home_page(request):
    hot_posts = Post.objects.order_by('-created_at')[:4]  # горячие новости
    posts = Post.objects.all()                             # все новости
    advs = Adv.objects.all()                               # реклама
    categories = Category.objects.all()                   # категории для меню

    context = {
        'hot_posts': hot_posts,
        'posts': posts,
        'advs': advs,
        'categories': categories
    }

    return render(request, "index.html", context)


# ----------------------
# Новости по категории
# ----------------------
def news_by_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    posts = Post.objects.filter(category=category).order_by('-created_at')[:4]
    advs = Adv.objects.all()  # реклама на странице категории
    categories = Category.objects.all()  # для меню

    context = {
        'category': category,
        'posts': posts,
        'advs': advs,
        'categories': categories
    }

    return render(request, "news_by_category.html", context)


# ----------------------
# Поиск — страница поиска
# ----------------------
def search_page(request):
    advs = Adv.objects.all()  # реклама на странице поиска
    categories = Category.objects.all()
    context = {
        'advs': advs,
        'categories': categories
    }
    return render(request, "search.html", context)


# ----------------------
# Результаты поиска
# ----------------------
def search_results(request):
    query = request.GET.get("q")
    results = []
    if query:
        results = Post.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )
    advs = Adv.objects.all()  # реклама
    categories = Category.objects.all()
    context = {
        'query': query,
        'results': results,
        'advs': advs,
        'categories': categories
    }
    return render(request, "search_results.html", context)


# ----------------------
# Страница конкретной новости
# ----------------------
def read_news_page(request, pk):
    post = get_object_or_404(Post, pk=pk)
    advs = Adv.objects.all()           # реклама
    categories = Category.objects.all() # для меню

    context = {
        'post': post,
        'advs': advs,
        'categories': categories
    }

    return render(request, "read_news.html", context)