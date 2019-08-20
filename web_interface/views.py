import json
import re

from django.core import serializers
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q

# Create your views here.
from django.template import loader
from django.views import View

from web_interface.forms import UserInputForm
from web_interface.models import ScrapyItem


class WebListView(View):
    def get(self, request):
        web_list = ScrapyItem.objects.all()
        # page = request.GET.get('page', 1)
        #
        # paginator = Paginator(web_list, 30)
        # try:
        #     web = paginator.page(page)
        # except PageNotAnInteger:
        #     web = paginator.page(1)
        # except EmptyPage:
        #     web = paginator.page(paginator.num_pages)

        return render(request, 'web_interface/weblist.html', {'web_list': web_list})


class SearchView(View):
    def get(self, request):
        return render(request, 'web_interface/searching.html', {'form': UserInputForm})

    def post(self, request):
        form = UserInputForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            if ScrapyItem.objects.filter(Q(h3__icontains=text)|Q(h2__icontains=text)).exclude(Q(start_url__icontains=text)):
                a = ScrapyItem.objects.filter(Q(h3__icontains=text)|Q(h2__icontains=text)).exclude(Q(start_url__icontains=text))
                return render(request, 'web_interface/searching.html', {'form': UserInputForm, 'msg': text, 'list': a})
            else:
                return render(request, 'web_interface/searching.html', {'form': UserInputForm, 'msg': "Not Found"})
        else:
            return HttpResponse("Form is not valid!!")


def jsonlistView(request):
    objects = ScrapyItem.objects.all()
    with open('items.json', "w") as f:
        mast_point = serializers.serialize("json", objects)
        f.write(mast_point)
    template = loader.get_template('web_interface/json_temp.html')
    context = {'object': objects}
    return HttpResponse(template.render(context, request))


