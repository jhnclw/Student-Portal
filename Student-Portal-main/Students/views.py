from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.admin.models import LogEntry
from .models import Student
from .forms import StudentForm


# def home(request):
#     # If logged in, redirect admin users to the Django admin dashboard
#     if request.user.is_authenticated and request.user.is_staff:
#         return redirect('home.html')
    
#     # Get all students from the database
#     students = Student.objects.all().order_by('name')
    
#     # Render the homepage showing the student table
#     return render(request, 'Students/student_list.html', {'students': students})

def home(request):
    return redirect('Students:list')
    return render(request, 'Students/student_list.html')

class StudentListView(ListView):
    model = Student
    template_name = "Students/student_list.html"
    context_object_name = "students"
    paginate_by = 5

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query:
            return Student.objects.filter(name__icontains=query)
        return Student.objects.all().order_by("name")

# class StudentListView(ListView):
#     model = Student
#     template_name = 'Students/student_list.html'
#     context_object_name = 'students'

class StudentCreateView(CreateView):
    model = Student
    template_name = 'Students/student_form.html'
    fields = ['name', 'age', 'course', 'year_level', 'grade']
    success_url = reverse_lazy('Students:list')  # redirects to student list after saving

class StudentUpdateView(UpdateView):
    model = Student
    template_name = 'Students/student_form.html'
    fields = ['name', 'age', 'course', 'year_level', 'grade']
    success_url = reverse_lazy('Students:list')

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'Students/student_confirm_delete.html'
    success_url = reverse_lazy('Students:list')
