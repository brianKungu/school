from django.shortcuts import render
from . models import About,Staff
from . forms import AboutForm,StaffForm
from django.views.generic import UpdateView
# Create your views here.
def index(request):
    abouts=About.objects.all()
    staffs=Staff.objects.all()
    return render(request,'website/index.html',{
                    'abouts':abouts,
                    'staffs':staffs}
                  )
def create_staff(request):
    form=StaffForm(request.POST or None)
    if form.is_valid():

        staff=form.save(commit=False)

        staff.save()
        return render(request,'website/index.html',{'staff':staff})
    return render(request, 'website/create_staff.html', {'form': form})

class AboutUpdateView(UpdateView):
    model = About
    fields = ['motto','logo','mission','vision']
    template_name = "website/about.html"