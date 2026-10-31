
# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee
from django.db.models import Count
from django.db import IntegrityError

def home(request):
    employees = Employee.objects.all()

    total_employees = employees.count()
    total_departments = employees.values(
        'department'
    ).distinct().count()

    return render(request, 'employees/home.html', {
        'employees': employees,
        'total_employees': total_employees,
        'total_departments': total_departments,
    })


def add_employee(request):
    error = ''

    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        department = request.POST.get('department', '').strip()
        salary = request.POST.get('salary', '').strip()

        if not name or not email or not department or not salary:
            error = 'Please fill in all fields.'
        else:
            try:
                salary_value = int(salary)

                if salary_value < 0:
                    raise ValueError

                Employee.objects.create(
                    name=name,
                    email=email,
                    department=department,
                    salary=salary_value
                )
                return redirect('home')

            except (ValueError, TypeError):
                error = 'Please enter a valid non-negative salary.'

            except IntegrityError:
                error = 'This email already exists. Please use another email.'

    return render(request, 'employees/add_employee.html', {
        'error': error
    })

    


def update_employee(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)

    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        department = request.POST.get('department', '').strip()
        salary = request.POST.get('salary', '').strip()

        try:
            salary_value = int(salary)

            if not name or not email or not department or salary_value < 0:
                raise ValueError

            employee.name = name
            employee.email = email
            employee.department = department
            employee.salary = salary_value
            employee.save()

            return redirect('home')

        except (ValueError, TypeError):
            pass

    return render(
        request,
        'employees/update_employee.html',
        {'employee': employee}
    )

def update_employee(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)

    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        department = request.POST.get('department', '').strip()
        salary = request.POST.get('salary', '').strip()

        try:
            salary_value = int(salary)

            if not name or not email or not department or salary_value < 0:
                raise ValueError

            employee.name = name
            employee.email = email
            employee.department = department
            employee.salary = salary_value
            employee.save()

            return redirect('home')

        except (ValueError, TypeError):
            pass

    return render(
        request,
        'employees/update_employee.html',
        {'employee': employee}
    )

def delete_employee(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)

    if request.method == 'POST':
        employee.delete()

    return redirect('home')