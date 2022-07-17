from django.shortcuts import render
from .models import jsondata
from django.http import JsonResponse
import statistics


def home(request):
    return render(request, 'home.html')

def likelihood_end(request):
    end_years = jsondata.objects.distinct('end_year')
    likelihood_end_year = {}
    for end_year in end_years:
        if end_year:
            likelihood_end_year[end_year] = f"{jsondata.objects(end_year = end_year).average('likelihood'):.1f}"
    list_values = list(likelihood_end_year.values())
    list_keys = list(likelihood_end_year.keys())
    data_json = {'data' : list_values , 'labels' : list_keys}
    return JsonResponse(data_json)

def relevance_region(request):
    regions = jsondata.objects.distinct('region')
    relevance_region = {}
    intensity_region = {}
    for region in regions:
        if region:
            relevance_region[region] = f"{jsondata.objects(region = region).average('relevance'):.1f}"
            intensity_region[region] = f"{jsondata.objects(region = region).average('intensity'):.1f}"
    list_values = list(relevance_region.values())
    list_keys = list(relevance_region.keys())
    list_intensity = list(intensity_region.values())
    data_json = {'data' : list_values , 'labels' : list_keys , 'data2' : list_intensity}
    return JsonResponse(data_json)

def relevance_pestle(request):
    pestles = jsondata.objects.distinct('pestle')
    relevance_pestle = {}
    intensity_pestle = {}
    for pestle in pestles:
        if pestle:
            relevance_pestle[pestle] = f"{jsondata.objects(pestle = pestle).average('relevance'):.1f}"
            intensity_pestle[pestle] = f"{jsondata.objects(pestle = pestle).average('intensity'):.1f}"
    list_values = list(relevance_pestle.values())
    list_keys = list(relevance_pestle.keys())
    list_intensity = list(intensity_pestle.values())
    data_json = {'data' : list_values , 'labels' : list_keys , 'data2' : list_intensity}
    return JsonResponse(data_json)

def country_topic(request):
    countrys = jsondata.objects.distinct('country')
    topic_country = {}
    for country in countrys:
        if country:
            topic_country[country] = jsondata.objects(country = country).fields(id=0,topic=1).to_json()
    for k , v in topic_country.items():
        v = eval(v)
        count = 0
        for the_dict in v:
            v[count] = the_dict['topic']
            count += 1
        x = [item for item in v if item]
        topic_country[k] = statistics.mode(x) if x else ''
    print(topic_country)
    return JsonResponse('nada')