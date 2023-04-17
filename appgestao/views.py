from django.http import JsonResponse

def Tarefa(request):
    if request.method == 'GET':
        tarefa = {'id': 1, 'title': 'Passagens e Diarias', 'description': '3 diarias para professor x.'}
        return JsonResponse(tarefa)


