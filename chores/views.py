from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Chore, ChoreLog
from django.http import JsonResponse
from django.utils import timezone

# Create your views here.
def chores(request):
    if request.method == "POST":
        response_data = {}
        user = User.objects.get(pk = request.POST['user_id'])
        chore = Chore.objects.get(pk = request.POST['chore_id'])
        user.log_chore.create(chore_name = chore)

        user.score.score += chore.score
        user.score.save()

        response_data['currentScore'] = user.score.score
        return JsonResponse(response_data)

    chores = Chore.objects.all()
    available_chores = []
    for chore in chores:
        if request.user in chore.user_assign.all():
            log = request.user.log_chore.filter(chore_name = chore, done_time__date=timezone.now())
            if len(log):
                pass
            else:
                available_chores.append(chore)

    context = {"chores": available_chores}
    return render(request, 'chores/chores.html', context)

