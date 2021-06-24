import os
from django.conf import settings
from django.http import Http404
from django.shortcuts import render
from traffic.models import FactAccidentVehicle


def dashboard(request):

    labels = {'severity': [], 'bands': [], 'vehicle': [], 'amount': []}
    data = {'severity': [], 'bands': [], 'vehicle': [], 'amount': []}
    try:

        for q in _get_accident_severity():
            labels['severity'].append(q.accident_severity)
            data['severity'].append(float(q.percentage))

        for q in _get_age_bands():
            labels['bands'].append(q.age_band_of_driver)
            data['bands'].append(float(q.percentage))

        for q in _get_vehicle_age():
            labels['vehicle'].append(q.age_of_vehicle)
            data['vehicle'].append(float(q.percentage))

        for q in _get_daily_amount():
            labels['amount'].append(q.day_of_week)
            data['amount'].append(q.count)

    except FactAccidentVehicle.DoesNotExist:
        raise Http404("The requested model does not exist")

    return render(request, 'dashboard.html', {
        'labels': labels,
        'data': data,
    })


def _get_accident_severity():
    return FactAccidentVehicle.objects.raw(_get_query('accident_severity.sql'))


def _get_age_bands():
    return FactAccidentVehicle.objects.raw(_get_query('age_bands.sql'))


def _get_vehicle_age():
    return FactAccidentVehicle.objects.raw(_get_query('vehicle_age.sql'))


def _get_daily_amount():
    return FactAccidentVehicle.objects.raw(_get_query('daily_amount.sql'))


def _get_query(file):
    return open(os.path.join(settings.BASE_DIR, 'queries', file)).read()
