from django.http import HttpResponse
from django.template import loader
from places.models import Place
import json


def main_page(request):
    template = loader.get_template('index.html')
    places = Place.objects.all()
    features = []
    for place in places:
        features.append(place.get_place_feature())
    feature_collection = {
                    "type": "FeatureCollection",
                    "features": features,
    }
    geojson = json.dumps(feature_collection, indent=2)
    places_features = {
        "features": geojson,
    }

    rendered_page = template.render(places_features, request)
    return HttpResponse(rendered_page)
