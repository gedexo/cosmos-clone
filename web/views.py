import re
from cgi import print_directory

from django.core.signing import TimestampSigner
from django.shortcuts import render
from officialapi.models import (ads, banner, blog, branch, brands, products,
                                service_request, slider)

# Create your views here.


def index(request):
    product = products.objects.all()
    sliders = slider.objects.all()
    branches = branch.objects.all()
    bestSeller = products.objects.filter(best_seller=True)
    baner = banner.objects.all()
    blogs = blog.objects.all()
    adss = ads.objects.all().first()
    blogOBjs = []
    signer = TimestampSigner()
    for i in blogs:
        blogOBj = {
            "id": signer.sign(str(i.id)),
            "date": i.date,
            "head": i.heading,
            "image": i.image_one,
        }
        blogOBjs.append(blogOBj)
    context = {
        "products": product,
        "slider": sliders,
        "branch": branches,
        "best_seller": bestSeller,
        "baner": baner,
        "blog": blogOBjs,
        "ads": adss,
    }
    return render(request, "web/index.html", context)


def service(request):
    return render(request, "web/service.html")


def service_request(request, category, service_type):
    context = {
        "branch": branch.objects.all(),
        "category": category,
        "service_type": service_type,
    }
    return render(request, "web/servicerequest.html", context)


def about(request):
    context = {"brand": brands.objects.all()}
    return render(request, "web/about-us.html", context)


def blogs(request, slug):
    signer = TimestampSigner()
    id = signer.unsign(slug)
    blogObj = blog.objects.get(id=id)
    content = blogObj.content

    context = {
        "blog": blogObj,
        "contentOne": content[0:300],
        "contentTwo": content[300:],
    }
    return render(request, "web/blog.html", context)


def branches(request):
    return render(request, "web/branches.html")
