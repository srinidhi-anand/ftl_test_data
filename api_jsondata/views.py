from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from .models import Post
from django.utils.timezone import timezone, timedelta
from faker import Faker
import json
import random
import string
from datetime import datetime
from django.http import JsonResponse


def posts(request):
    fake = Faker('en_US')
    records = []
    for j in range(3):
        activities = []
        record = {"id": ''.join(random.choice(string.ascii_letters.upper() + string.digits) for i in range(8)),
                  "real_name": fake.name(),
                  "time": str(datetime.now(timezone(timedelta(0))).astimezone().tzinfo)}
        for k in range(3):
            times = {"start_time": str(format(datetime.now() + timedelta(hours=k), '%b %d %Y %H:%M:%p')),
                     "end_time": str(format(datetime.now() + timedelta(hours=k+3), '%b %d %Y %H:%M:%p'))}
            activities.append(times)
        record.update({'activity_periods':activities})
        records.append(record)
    json_data = {'ok': 'true', 'members': records}
    json_final_result = json.dumps(json_data, indent=4)
    return HttpResponse(json_final_result, content_type='application/json')