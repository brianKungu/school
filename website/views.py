from django.shortcuts import render,get_object_or_404,redirect
from . models import About,Staff,Department,Club
from . forms import AboutForm,StaffForm,DepartmentForm,ClubForm
from django.views.generic import UpdateView,DeleteView
# Create your views here.
def index(request):
    abouts=About.objects.all()
    staffs=Staff.objects.all()
    return render(request,'website/index.html',{
                    'abouts':abouts,
                    'staffs':staffs}
                  )
def create_staff(request):
    form = StaffForm(request.POST or None, request.FILES or None)
    if form.is_valid():

        staff = form.save(commit=False)
        staff.staff_cover = request.FILES['staff_cover']
        staff.save()

        return render(request,'website/index.html', {'staff':staff})
    return render(request, 'website/create_staff.html', {'form': form})

class AboutUpdateView(UpdateView):
    model = About
    fields = ['motto','logo','mission','vision']
    template_name = "website/about.html"


def staff_delete(delete,staff_id):
    staff= get_object_or_404(Staff, pk=staff_id)
    staff.delete()
    return redirect('/')

class StaffUpdateView(UpdateView):
    model = Staff
    fields = ['staff_cover','staff_name', 'id_number', 'contact', 'role']
    template_name = "website/create_staff.html"

def department(request):
    departments=Department.objects.all()
    return render(request,'website/departments.html',{'departments':departments})

def create_department(request):
    form=DepartmentForm(request.POST or None)
    if form.is_valid():

        department=form.save(commit=False)

        department.save()
        return render(request,'website/departments.html', {'department':department})
    return render(request, 'website/create_department.html', {'form': form})

class DepartmentUpdateView(UpdateView):
    model = Department
    fields = ['department_name', 'department_head', 'sub_head']
    template_name = "website/create_department.html"

def department_delete(delete,department_id):
    department= get_object_or_404(Department, pk=department_id)
    department.delete()
    return redirect('website:departments')

def club(request):
    clubs=Club.objects.all()
    return render(request,'website/clubs.html',{'clubs':clubs})

def create_club(request):
    form=ClubForm(request.POST or None)
    if form.is_valid():

        club=form.save(commit=False)

        club.save()
        return render(request,'website/clubs.html', {'club': club})
    return render(request, 'website/create_club.html', {'form': form})

class ClubUpdateView(UpdateView):
    model = Club
    fields = ['club_name', 'description', 'patron']
    template_name = "website/create_club.html"

def club_delete(delete,club_id):
    club= get_object_or_404(Club, pk=club_id)
    club.delete()
    return redirect('website:clubs')
