import json

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import BadgeAccess, BadgeAccessLog

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def cardcheck(request, card):

    data = { 'status': False, }
    badgeaccess = None

    if BadgeAccess.objects.filter(active=True, card=card.upper()).exists():
        badgeaccess = BadgeAccess.objects.get(active=True, card=card)
        data['status'] = True

    BadgeAccessLog.objects.create(card=card, status=data['status'], badgeaccess=badgeaccess, request_ip=get_client_ip(request))
    html = json.dumps(data)
    return HttpResponse(html)