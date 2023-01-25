from django.shortcuts import render
#from leveltwo_exe_app.models import User
from leveltwo_exe_app.forms import NewUserForm
# Create your views here.
def  index(request):
  context_dict = {'text':'hello world','number':100}
  return render(request,'leveltwo_exe_app/index.html',context_dict)

def users(request):
  #user_list = User.objects.order_by('first_name')
  #user_dict = {'users':user_list}
  #return render(request,'leveltwo_exe_app/users.html',context=user_dict)

  #create a new object or variable form and assign it to a instance NEwUserForm
  # if input request method is equal to post(meaning someone submit this form and sending information back)
  # then we are going to reassign form is equal to
  # instance of newuserform and pass in request.POST.then the form is valid ro not
  # in order to save the form u can use .save() and use commit=True to commit is to database
  # then will return the index view and pass in that request(meaning taking back to home page).
  #outside all of this we need to return something so it matches the actual page.
  # then send the context dictionary that contains that form.
  form = NewUserForm()
  if request.method == 'POST':
    form = NewUserForm(request.POST)

    if form.is_valid():
      form.save(commit=True)
      return index(request)
      #return render(request,'leveltwo_exe_app/index.html')
    else:
      print('form in valid')

  return render(request,'leveltwo_exe_app/users.html',{'form':form})

    
def indextwo(request):
  return render(request,'leveltwo_exe_app/indextwo.html')

def other(request):
  return render(request,'leveltwo_exe_app/other.html')

def relative(request):
  return render(request,'leveltwo_exe_app/relative_url_template.html')

