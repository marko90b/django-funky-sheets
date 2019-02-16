from django.forms import CheckboxSelectMultiple
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy

from funky_sheets.formsets import HotView

from .models import Movie


def index(request):
    return HttpResponseRedirect(reverse('update'))


class CreateMovieView(HotView):
    model = Movie
    template_name = 'examples/create.html'
    prefix = 'table'
    success_url = reverse_lazy('update')
    fields = ('id', 'title', 'genre', 'imdb_rating')

    factory_kwargs = {
        'widgets': {
            'genre': CheckboxSelectMultiple()
        }
    }

    hot_settings = {
        'columnSorting': 'true',
        'contextMenu': 'true',
        'autoWrapRow': 'true',
        'rowHeaders': 'true',
        'contextMenu': 'true',
        'search': 'true'
    }


class UpdateMovieView(HotView):
    model = Movie
    template_name = 'examples/update.html'
    action = 'update'
    button_text = 'Update'
    prefix = 'table'
    success_url = reverse_lazy('update')
    fields = ('id', 'title', 'genre', 'imdb_rating')

    factory_kwargs = {
        'widgets': {
            'genre': CheckboxSelectMultiple()
        }
    }

    hot_settings = {
        # 'columnSorting': 'true',
        'contextMenu': 'true',
        'autoWrapRow': 'true',
        'rowHeaders': 'true',
        'contextMenu': 'true',
        'search': 'true'
    }