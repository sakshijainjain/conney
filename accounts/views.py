from django.shortcuts import render,redirect
from .forms import UserRegisterForm
from contact.models import Contact
from django.contrib.auth.decorators import login_required

def register_view(request):
    form = UserRegisterForm()

    if request.method=="POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            

            return redirect('login')
    
    return render(request,'accounts/register.html',{"form":form})

@login_required
def dashboard(request):
    user_contact = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)

    context = {
    'contacts': user_contact
    }
    return render(request, 'accounts/dashboard.html', context)


