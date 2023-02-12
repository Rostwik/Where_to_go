from django.shortcuts import render
from django.urls import reverse

from places.models import Place, Image
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404


def index(request):
    places = Place.objects.all()
    features = []

    for place in places:
        features.append(
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [
                        place.lon,
                        place.lat
                    ]
                },
                "properties": {
                    "title": place.title,
                    "placeId": place.id,
                    "detailsUrl": reverse('api_place', args=(place.id,))
                }
            }
        )

    places_geojson = {
        "type": "FeatureCollection",
        "features": features
    }

    data = {"json": places_geojson}
    return render(request, "index.html", context=data)


def places(request, id):
    place = get_object_or_404(Place.objects.prefetch_related(), id=id)

    place_imgs = [img.picture.url for img in place.images.all()]

    place_detail = {
        "title": place.title,
        "imgs": place_imgs,
        "short_description": place.short_description,
        "long_description": place.long_description,
        "coordinates": {
            "lng": place.lon,
            "lat": place.lat
        }
    }

    return JsonResponse(
        place_detail,
        safe=False,
        json_dumps_params={'ensure_ascii': False, 'indent': 2}
    )
