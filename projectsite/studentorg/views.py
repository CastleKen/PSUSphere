from django.shortcuts import render

# Create your views here.
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from studentorg.models import Organization, OrgMember, Student
from studentorg.forms import OrganizationForm, OrgMemberForm, StudentForm
from django.urls import reverse_lazy

class HomePageView(ListView):
    model = Organization
    context_object_name = 'home'
    template_name = "home.html"

class OrganizationList(ListView):
    model = Organization
    context_object_name = 'organization'
    template_name = 'org_list.html'
    paginate_by = 5

class OrganizationCreateView(CreateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'org_form.html'
    success_url = reverse_lazy('organization-list')

class OrganizationUpdateView(UpdateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'org_form.html'
    success_url = reverse_lazy('organization-list') 

class OrganizationDeleteView(DeleteView):
    model = Organization
    template_name = 'org_del.html'
    success_url = reverse_lazy('organization-list')

class OrgMemberList(ListView):
    model = OrgMember
    context_object_name = 'orgmember'
    template_name = 'orgmem_list.html'
    paginate_by = 5

class OrgMemberCreateView(CreateView):
    model = OrgMember
    form_class = OrgMemberForm
    template_name = 'orgmem_form.html'
    success_url = reverse_lazy('orgmember-list')

class StudentList(ListView):
    model = Student
    context_object_name = 'student'
    template_name = 'stud_list.html'
    paginate_by = 5

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'stud_form.html'
    success_url = reverse_lazy('student-list')

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'stud_form.html'
    success_url = reverse_lazy('student-list') 

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'stud_del.html'
    success_url = reverse_lazy('student-list')