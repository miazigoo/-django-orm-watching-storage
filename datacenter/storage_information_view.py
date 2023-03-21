from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime


def storage_information_view(request):
    """Не закрытые посещения"""
    not_leaved_at = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []
    for not_leaved in not_leaved_at:
        entered_at = not_leaved.entered_at
        duration = not_leaved.format_duration()
        adr_pass = not_leaved.passcard
        non_closed_visits.append({
            'who_entered': adr_pass.owner_name,
            'entered_at': localtime(entered_at),
            'duration': duration,
        })
    context = {
            'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)

