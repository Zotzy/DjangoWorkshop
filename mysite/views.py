from django.http import HttpResponseRedirect

def index(request):
	return HttpResponseRedirect('https://www.cs.mtsu.edu/~acm/')
