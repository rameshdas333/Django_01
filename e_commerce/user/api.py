from user.models import User
from django.http import JsonResponse

def duplicate_check(request):
    email = request.GET.get(email)
    user_obj = User.objects.filter(email)
    if user_obj.exists():
        return JsonResponse({"message":"Already Exits:"},status=200)
    return JsonResponse({"message":"OK:"},status=200)