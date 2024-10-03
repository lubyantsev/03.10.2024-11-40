from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ScheduleForm, PasswordForm, EventForm
from .models import Schedule, Event


def create_schedule(request):
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            schedule = form.save()
            messages.success(request, 'Расписание успешно создано!')
            return redirect('home')
    else:
        form = ScheduleForm()
    return render(request, 'schedules/create_schedule.html', {'form': form})


def schedule_detail_view(request, schedule_id):
    schedule = Schedule.objects.get(id=schedule_id)
    events = Event.objects.filter(schedule=schedule)

    if request.method == 'POST':
        if 'edit_event' in request.POST:
            event_id = request.POST['edit_event']
            event = Event.objects.get(id=event_id)
            event_form = EventForm(request.POST, instance=event)
            if event_form.is_valid():
                event_form.save()
                messages.success(request, 'Событие обновлено!')
        elif 'new_event' in request.POST:
            event_form = EventForm(request.POST)
            if event_form.is_valid():
                event = event_form.save(commit=False)
                event.schedule = schedule
                event.save()
                messages.success(request, 'Событие добавлено!')

    event_form = EventForm()
    return render(request, 'schedules/schedule_detail.html', {
        'schedule': schedule,
        'events': events,
        'event_form': event_form,
    })


def home_view(request):
    if request.method == 'POST':
        password_form = PasswordForm(request.POST)
        if password_form.is_valid():
            try:
                schedule = Schedule.objects.get(password=password_form.cleaned_data['password'])
                return redirect('schedule_detail', schedule_id=schedule.id)
            except Schedule.DoesNotExist:
                messages.error(request, 'Расписание с таким паролем не найдено.')
    else:
        password_form = PasswordForm()

    return render(request, 'schedules/home.html', {'password_form': password_form})
