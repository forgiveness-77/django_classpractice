from django.shortcuts import redirect, render
from attendance.forms import StudentForm
from attendance.models import Attendance

# Create your views here.
def attendance_list(request):
    records= Attendance.objects.select_related('student').order_by('-date')
    return render(request, 'attandance/attendace_list.html', {
        'records':records
    })

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/attendance/add_student')
    else:
        form = StudentForm()
    return render(request, 'attendance/add_student.html', {'form': form})