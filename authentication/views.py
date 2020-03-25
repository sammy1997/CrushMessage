from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Message

def index(request):
	if request.user.is_authenticated:
		message_list = Message.objects.filter(user=request.user)
	else:
		message_list = []

	return render(request,'authentication/index.html', {'message_list':message_list})


# def post_message(request, username):



def submit_message(request, username):
	if request.method == 'POST':
		message_text = request.POST.get('message')
		user = User.objects.get(username = username)
		new_message = Message(message_text = message_text, user = user)
		new_message.save()
		return render(request, 'authentication/post_message.html', {"success": "Message posted!", 'username':username, "name": user.first_name})
	else:
		user = None
		try:
			user = User.objects.get(username=username)
		except User.DoesNotExist:
			return render(request, 'authentication/invalid_user.html')
		return render(request,'authentication/post_message.html', {'username':username, "name": user.first_name})


def delete_message(request, message_id):
	message = Message.objects.get(pk=message_id)
	message.delete()
	return redirect('authentication:home')