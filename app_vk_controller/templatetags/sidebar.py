from django import template
from django.db import connection
from django.db.models import Prefetch

from clothes.models import Category, Clothes, Tag, Photo

register = template.Library()


# @register.simple_tag(takes_context=True)
# @register.simple_tag()
# def current_time():
#     timezone = context['timezone']
#     return your_get_current_time_method(timezone, format_string)


@register.simple_tag()
def get_tags():
    # tags =Tag.objects.all()

    # return cache.get_or_set('tags', Tag.objects.all(), 60)
    return Tag.objects.all()


@register.simple_tag()
def get_categories():
    # category =Category.objects.all()

    # return cache.get_or_set('category', Category.objects.all(), 60)
    return Category.objects.all()


@register.inclusion_tag('clothes/tags/tags.html')
def show_tags(tags):
    return {'tags': tags}


@register.inclusion_tag('clothes/tags/category.html')
def show_categories(categories):
    return {'categories': categories}


@register.inclusion_tag('clothes/tags/clothes_by_category.html')
def get_clothes_by_category(category, pk=0, count=5):
    if not category:
        return

    # clothes = Clothes.objects.filter(category=category).prefetch_related('photo_set')
    clothes = Clothes.objects.filter(category=category).prefetch_related('photo_set').order_by('-views').exclude(
        pk=pk).all()
    clothes = clothes[:count]
    return {'clothes': clothes, 'category': category}


@register.inclusion_tag('clothes/tags/clothes_by_tag.html')
def get_clothes_by_tags(tag, pk=0, count=5):
    if not tag:
        return

    clothes = Clothes.objects.filter(tags=tag).prefetch_related('photo_set').order_by('-views').exclude(id=pk).all()
    clothes = clothes[:count]
    return {'clothes': clothes, 'tag': tag}


@register.inclusion_tag('clothes/tags/last_clothes.html')
def show_last_clothes():
    # reset_queries()
    # clothes = Clothes.objects.only('slug', 'title').prefetch_related(
    #     Prefetch('photo_set', queryset=Photo.objects.filter(photo__isnull=False).only('photo', 'id')))[:6]

    # queryset = Contact.objects.all().prefetch_related(
    #     Prefetch('Groups', queryset=Group.objects.all().only('id')))

    clothes = Clothes.objects.filter(photo__isnull=False).only('slug', 'title').prefetch_related(
        Prefetch('photo_set', queryset=Photo.objects.all().only('id', 'clothes_id', 'photo'))).distinct()[:6]

    # clothes = Clothes.objects.prefetch_related('photo_set').filter(photo__isnull=False).distinct()[:6]
    # clothes = Clothes.objects.only('slug', 'title').filter(photo__isnull=False).distinct()[:6]
    # clothes = Clothes.objects.prefetch_related('photo_set').filter(photo__isnull=False).distinct()[:6]
    # clothes = Clothes.objects.filter(photo__isnull=False).only('slug', 'title').distinct()[:6]
    # clothes = Photo.objects.only('id', 'title', 'photo').filter(clothes_id__in=[clothe.id for clothe in clothes])[:6]

    # for i in clothes:
    #     print(i)

    # clothes.distinct()
    # clothes = Clothes.objects.prefetch_related('photo_set')[:6]
    # clothes = Clothes.objects.all()
    # print(clothes)
    # for clothe in clothes:
    #     # print(clothe.get_absolute_url)
    #     try:
    #         print(clothe.photo_set[0].photo.url)
    #     except:
    #         pass
    # pprint(connection.queries)
    # print(len(clothes))
    #
    # pprint(len(connection.queries))
    return {'clothes': clothes, 'connection': connection}
