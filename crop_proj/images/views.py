from django.shortcuts import render
from .models import Image
from .forms import ImageForm
from django.http import JsonResponse
# Create your views here.

def get_ip_address(request):
    """ use requestobject to fetch client machine's IP Address """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')    ### Real IP address of client Machine
    return ip   


# def home(request):
#     """ your vies to handle http request """
#     ip_address = get_ip_address(request)

def main_view(request):
	# obj = Image.objects.get(pk=1)
	ip_address = get_ip_address(request)
	form = ImageForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		form.save()
		return JsonResponse({'message': 'works'})

	context = {'form': form}
	return render(request, 'images/main.html', context)
