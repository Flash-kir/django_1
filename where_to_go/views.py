from django.http import HttpResponse
from django.template import loader
from places.models import Place
import json


def get_place_feature(place):
    feature = {
        'type': 'Feature',
        'geometry': {
            'type': 'Point',
            'coordinates': [
                round(place.lng, 2),
                round(place.lat, 6)
                ]
            },
        'properties': {
            'title': place.title,
            'placeId': f'key_{place.pk}',
            'detailsUrl': f'/places/{place.pk}/',
        }
    }
    return feature


def get_place_content(place):
    return {
            'title': place.title,
            'imgs': place.get_images_list(),
            'description_short': place.description_short,
            'description_long': place.description_long,
            'coordinates': {
                'lng': place.lng,
                'lat': place.lat,
            }
        }


def main_page(request):
    template = loader.get_template('index.html')
    places = Place.objects.all()
    features = []
    for place in places:
        features.append(get_place_feature(place))
    feature_collection = {
                    'type': 'FeatureCollection',
                    'features': features,
    }
    geojson = json.dumps(feature_collection, indent=2)
    places_features = {
        'features': geojson,
    }

    rendered_page = template.render(places_features, request)
    return HttpResponse(rendered_page)


def place_detail_view(request, place_id):
    place = Place.objects.get(id=place_id)
    place_json = json.dumps(get_place_content(place), indent=2)
    return HttpResponse(place_json)
