from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.db.models import Exists, OuterRef
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from zipfile import ZipFile
import calendar
from datetime import date
from calendar import HTMLCalendar
from django.shortcuts import render, redirect
from .models import Event
from .forms import EventForm
from django.utils import timezone
from home.models import Post
from django.urls import reverse
from datetime import timedelta

Users = get_user_model()
    
class NavigationCalendar(HTMLCalendar):
    def formatmonth_with_navigation(self, year, month, prev_url, next_url):
        cal_html = self.formatmonth(year, month)
        month_name = calendar.month_name[month]

        # Create custom header with navigation
        nav_html = f"""
        <tr>
            <th colspan="7" style="text-align:center;">
                <a href="{prev_url}" style="margin-right:20px; color:white; font-size:32px; text-decoration:none;">←</a>
                <span style="font-size:24px; font-weight:bold;">{month_name} {year}</span>
                <a href="{next_url}" style="margin-left:20px; color:white; font-size:32px; text-decoration:none;">→</a>
            </th>
        </tr>
        """

        # Replace the original month header row
        cal_html = cal_html.replace(
            f'<tr><th colspan="7" class="month">{month_name} {year}</th></tr>',
            nav_html
        )
        return cal_html
    
    def formatweekheader(self):
        return '<tr>' + ''.join(f'<th>{day}</th>' for day in calendar.day_name) + '</tr>'
    
    def formatweek(self, theweek):
        return '<tr>' + ''.join(self.formatday(d, wd) for (d, wd) in theweek) + '</tr>'
    
    def formatmonth(self, year, month, withyear=True):
        self.year, self.month = year, month
        weeks = self.monthdays2calendar(year, month)  # ← ADD THIS LINE

        return (
            f'<table border="0" cellpadding="0" cellspacing="0" class="month">\n'
            f'{self.formatmonthname(year, month, withyear=withyear)}\n'
            f'{self.formatweekheader()}\n'
            + '\n'.join(self.formatweek(week) for week in weeks) +
            '\n</table>'
        )

    def formatday(self, day, weekday):
        if day != 0:
            cssclass = self.cssclasses[weekday]
            day_events = self.events.get(day, [])
            events_html = ''.join(
                f"<a href='{reverse('post_detail', args=[e.id])}' class='event-box'>{e.title}</a>"
                for e in day_events
            )
            return f"<td class='{cssclass}'><span class='day-number'>{day}</span>{events_html}</td>"
        return '<td></td>'
    
class EventCalendar(NavigationCalendar):
    def __init__(self, posts):
        super().__init__(firstweekday=6)
        self.events = self.group_by_day(posts)

    def group_by_day(self, posts):
        grouped = {}
        for post in posts:
            day = post.scheduled_time.day
            if day in grouped:
                grouped[day].append(post)
            else:
                grouped[day] = [post]
        return grouped

    def formatday(self, day, weekday):
        if day == 0:
            return '<td></td>'

        css_class = self.cssclasses[weekday]
        today = date.today()
        if self.year == today.year and self.month == today.month and day == today.day:
            css_class += " today"

        day_posts = self.events.get(day, [])
        posts_html = ''.join(
            f'<a href="{reverse("post_detail", args=[post.id])}" class="event-box">{post.title}</a>'
            for post in day_posts
            )

        return f'<td class="{css_class}"><div class="day-number">{day}</div>{posts_html}</td>'

def calendar_view(request):
    today = timezone.localdate()
    year = int(request.GET.get('year', today.year))
    month = int(request.GET.get('month', today.month))

    # Navigation logic
    prev_month = month - 1 if month > 1 else 12
    prev_year = year - 1 if month == 1 else year
    next_month = month + 1 if month < 12 else 1
    next_year = year + 1 if month == 12 else year

    prev_url = f"?month={prev_month}&year={prev_year}"
    next_url = f"?month={next_month}&year={next_year}"

    # Get posts scheduled in the current month
    posts = Post.objects.filter(
        scheduled_time__year=year,
        scheduled_time__month=month
    )

    cal = EventCalendar(posts)
    html_calendar = cal.formatmonth_with_navigation(year, month, prev_url, next_url)

    return render(request, 'calendar_view.html', {
        'calendar': html_calendar,
    })


def weekly_calendar_view(request):
    today = timezone.localdate()
    year = int(request.GET.get('year', today.year))
    month = int(request.GET.get('month', today.month))
    day = int(request.GET.get('day', today.day))

    selected_date = date(year, month, day)
    start_of_week = selected_date - timedelta(days=selected_date.weekday() + 1 if selected_date.weekday() != 6 else 0)
    week_dates = [start_of_week + timedelta(days=i) for i in range(7)]

    posts = Post.objects.filter(scheduled_time__date__in=week_dates)

    # Create a list of (day, posts) tuples
    week_data = []
    for d in week_dates:
        day_posts = posts.filter(scheduled_time__date=d)
        week_data.append((d, day_posts))

    prev_week = start_of_week - timedelta(days=7)
    next_week = start_of_week + timedelta(days=7)
    prev_url = f"?year={prev_week.year}&month={prev_week.month}&day={prev_week.day}"
    next_url = f"?year={next_week.year}&month={next_week.month}&day={next_week.day}"

    return render(request, "weekly_calendar.html", {
        "week_data": week_data,   # List of (date, posts)
        "today": today,
        "prev_url": prev_url,
        "next_url": next_url,
    })

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})

