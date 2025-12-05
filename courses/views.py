from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Lesson, Enrollment, LessonProgress
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from django.contrib import messages

def course_list(request):
    courses = Course.objects.all().order_by('-created_at')
    return render(request, 'courses/course_list.html', {'courses': courses})

def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    user_enrolled = False
    if request.user.is_authenticated:
        user_enrolled = Enrollment.objects.filter(user=request.user, course=course).exists()
    return render(request, 'courses/course_detail.html', {'course': course, 'user_enrolled': user_enrolled})

@login_required
def enroll(request, pk):
    course = get_object_or_404(Course, pk=pk)
    Enrollment.objects.get_or_create(user=request.user, course=course)
    messages.success(request, f'Enrolled in {course.title}')
    return redirect('course_detail', pk=pk)

@login_required
def lesson_detail(request, course_pk, pk):
    course = get_object_or_404(Course, pk=course_pk)
    lesson = get_object_or_404(Lesson, pk=pk, course=course)
    LessonProgress.objects.get_or_create(user=request.user, lesson=lesson)
    seen_lessons = LessonProgress.objects.filter(user=request.user, lesson__course=course).values_list('lesson_id', flat=True)
    return render(request, 'courses/lesson_detail.html', {'course': course, 'lesson': lesson, 'seen_lessons': seen_lessons})

@login_required
def my_courses(request):
    enrollments = Enrollment.objects.filter(user=request.user).select_related('course')
    courses = [e.course for e in enrollments]
    return render(request, 'courses/my_courses.html', {'courses': courses})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created. You can now log in.')
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})
