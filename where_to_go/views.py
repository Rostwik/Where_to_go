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
                        place.coordinate_lng,
                        place.coordinate_lat
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
    place = get_object_or_404(Place, id=id)

    place_imgs = [img.picture.url for img in Image.objects.filter(place=place).order_by('-position')]

    place_detail = {
        "title": place.title,
        "imgs": place_imgs,
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lng": place.coordinate_lng,
            "lat": place.coordinate_lat
        }
    }

    return HttpResponse(
        JsonResponse(
            place_detail,
            safe=False,
            json_dumps_params={'ensure_ascii': False, 'indent': 2}
        ),
        content_type="application/json"
    )
