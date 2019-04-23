# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from Analysis.models import CoursePageViews, MarkPageViews, MainPageViews
# from Analysis.serializers import AnalysisSerializer
from rest_framework import generics
from django.http import JsonResponse, HttpResponse
from django.forms.models import model_to_dict
import json
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import time
import datetime

def getTimeStamp():
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    return st

@csrf_exempt
def AccessUserCoursePage(request):
    if(request.method == "POST"):
        
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        reg_no = body['reg_no']
        
        qs = CoursePageViews.objects.filter(reg_no=reg_no)
        
        if(qs):
            print(qs.values('timestamps'))            
            new_timestamps = str(model_to_dict(qs[0])['timestamps']).split(',')
            
            new_timestamps.append(getTimeStamp())
            qs.update(timestamps = ','.join(new_timestamps))
        else:
            new_entry = CoursePageViews(reg_no=reg_no, timestamps=str(getTimeStamp()))
            new_entry.save()

        return HttpResponse({ 200 }, content_type ="application/json")

@csrf_exempt
def AccessUserMarkPage(request):
    if(request.method == "POST"):
        
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        reg_no = body['reg_no']
        
        if(qs):
            print(qs.values('timestamps'))            
            new_timestamps = str(model_to_dict(qs[0])['timestamps']).split(',')
            
            new_timestamps.append(getTimeStamp())
            qs.update(timestamps = ','.join(new_timestamps))
        else:
            new_entry = MarkPageViews(reg_no=reg_no, timestamps=str(getTimeStamp()))
            new_entry.save()

        return HttpResponse({ 200 }, content_type ="application/json")

@csrf_exempt
def AccessUserMainPage(request):
    if(request.method == "POST"):

        
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        reg_no = body['reg_no']
        

        qs = MainPageViews.objects.filter(reg_no=reg_no)
        
        if(qs):
            # print(qs.values('timestamps'))            
            new_timestamps = str(model_to_dict(qs[0])['timestamps']).split(',')            
            new_timestamps.append(getTimeStamp())
            qs.update(timestamps = ','.join(new_timestamps))
        else:
            new_entry = MainPageViews(reg_no=reg_no, timestamps=str(getTimeStamp()))
            new_entry.save()
            # print(new_entry)

        return HttpResponse({ 200 }, content_type ="application/json")
