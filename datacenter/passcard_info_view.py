from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render, get_object_or_404


def passcard_info_view(request, passcode):
    """Информация визитов по passcard"""
    passcard = get_object_or_404(Passcard,passcode=passcode)
    all_visits = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = []
    for visits in all_visits:
        this_passcard_visits.append(
            {
                'entered_at': visits.entered_at,
                'duration': visits.format_duration(),
                'is_strange': visits.is_visit_long(minutes=60)
            })
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)

