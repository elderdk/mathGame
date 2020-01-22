from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def store(request):
    score = request.user.score.score
    number_of_coins = score // 100
    return render(request, 'store/store.html', {'coins': number_of_coins})

def spendscore(request):
    if request.method == 'POST':
        response_data = {}
        request.user.score.score -= 100
        print(request.user.score.score)
        request.user.score.save()

        response_data['currentScore'] = request.user.score.score
        return JsonResponse(response_data)