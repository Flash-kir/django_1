from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from places.models import Place
from django.urls import reverse


def get_place_feature(place):
    feature = {
        'type': 'Feature',
        'geometry': {
            'type': 'Point',
            'coordinates': [
                place.lng,
                place.lat
            ]
        },
        'properties': {
            'title': place.title,
            'placeId': f'key_{place.pk}',
            'detailsUrl': reverse('place-detail', args=(place.pk,)),
        }
    }
    return feature


def main_page(request):
    features = [get_place_feature(place) for place in Place.objects.all()]
    return render(
        request,
        'index.html',
        context={
            'features': {
                'type': 'FeatureCollection',
                'features': features,
            },
        }
    )


def place_detail_view(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    return JsonResponse(
        {
            'title': place.title,
            'imgs': [image.image.url for image in place.images.all()],
            'description_short': place.description_short,
            'description_long': place.description_long,
            'coordinates': {
                'lng': place.lng,
                'lat': place.lat,
            },
        },
        json_dumps_params={
            'indent': 2,
            'ensure_ascii': False,
        }
    )
