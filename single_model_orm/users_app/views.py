from django.shortcuts import render, redirect, HttpResponse
from .models import Users

def index(request):
	# return HttpResponse('single_model_orm / users_app / views.index')
	context = {
		'title': 'Users With Templates',
		'users': Users.objects.all().values()
	}
	if 'alert' in request.session and 'alert_message' in request.session:
		context['alert'] = request.session['alert']
		context['alert_message'] = request.session['alert_message']
	return render(request, 'index.html', context)

def add(request):
	# return HttpResponse('single_model_orm / users_app / views.add')
	user = Users(first_name=request.POST['first_name'].upper(), last_name=request.POST['last_name'].upper(), email_address=request.POST['email_address'].lower(), age=int(request.POST['age']))
	users_filtered = Users.objects.filter(first_name=user.first_name, last_name=user.last_name, email_address=user.email_address, age=user.age)
	if len(users_filtered):
		request.session['alert'] = True
		request.session['alert_message'] = 'User has already been added.'
	else:
		Users.objects.create(first_name=user.first_name, last_name=user.last_name, email_address=user.email_address, age=user.age)
	return redirect('/')