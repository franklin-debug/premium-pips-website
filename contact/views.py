from django.shortcuts import render
from .models import Message,Register
from django.views.decorators.http import require_POST

# Create your views here.
def contact(request):
    return render(request,'contact.html')

#@require_POST
def addmessage(request):
	if request.method == "POST":

		name = request.POST['Name'] 
		mobile_no = request.POST['Mobile_no'] 
		email = request.POST['Email'] 
		message = request.POST['Message'] 
		Messages = Message(name=name,mobile_no=mobile_no,email=email,message_details=message,)
		Messages.save()
		return render(request,'message.html')
	
def register(request):
	return render(request,'register.html')

#@require_POST
def registered_students(request):
	if request.method == "POST":

		name = request.POST['Name'] 
		mobile_no = request.POST['Mobile_no'] 
		email = request.POST['Email'] 
		plan = request.POST['Plan'] 
		STUDENTS = Register(name=name,mobile_no=mobile_no,email=email,plan=plan,)
		STUDENTS.save()
		return render(request,'registered_message.html')
	

