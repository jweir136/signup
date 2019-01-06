from django.shortcuts import render, redirect
from django.contrib.auth.models import User

global home_link
home_link = "https://quant-qb43myb7x.now.sh"

# Create your views here.
def index(requests):
	if requests.method == "POST":
		name = requests.POST.get("name", False)
		email = requests.POST.get("email", False)
		if name and email:
			user = User.objects.create_user(username=name, email=email)
			return redirect(home_link)
		
	return render(requests, "form/index.html")
