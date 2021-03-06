from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
import json
import os
import re
from django.http import JsonResponse
from courses.models import Course

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
course_data = json.loads(open(os.path.join(BASE_DIR, 'courses.json'),'r').read())

def index(request, course_id):
    try:
        course = Course.objects.get(id=course_id)
    except KeyError as e:
        return HttpResponse(render(request, 'course_unavailable.html', context = {'id': course_id}))
    return HttpResponse(render(request, 'course_page.html', context = {'course': course}))

def search(request):
    if request.method == 'POST':
        query = request.POST.get('query')
        print(query)
        subject_id, subject_name = str(query).split('-')
        subject_id = re.findall('[A-Z0-9]+', subject_id)[0]
        return HttpResponseRedirect('/courses/{}'.format(subject_id))
    return HttpResponse(render(request, 'course_search.html'))

def compare(request):
    course_data = json.loads(open(os.path.join(BASE_DIR, 'courses.json'),'r').read())
    course_grades1 = str(json.dumps(course_data['BT21002']['grades']))
    course_grades2 = str(json.dumps(course_data['AG31003']['grades']))
    return HttpResponse(render(request, 'compare_grades.html', context = {'grades1': course_grades1, 'grades2': course_grades2}))

def edit(request,course_id):
    course_data = json.loads(open(os.path.join(BASE_DIR, 'courses.json'),'r').read())
    course = course_data[course_id]
    return HttpResponse(render(request, 'course_edit.html', context = {'course': course}))

def json(request,course_id):
    return JsonResponse(course_data[course_id])
