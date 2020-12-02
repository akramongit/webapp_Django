from django.shortcuts import render

def index(request):
    if request.method == 'POST':
        inpt1 = request.POST['name']
        inpt2 = request.POST['roll']
    rst = inpt1 + inpt2
    return render(request, 'index.html',{'rst':rst})

def msg(request):
    ms = 'Hi'
	return render(request, 'msg.html', {'ms':ms})
