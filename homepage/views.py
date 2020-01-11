# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from selenium import webdriver
from selenium.webdriver.support.select import Select

import time
import datetime
import os
import threading
from django.core.mail import EmailMessage
import subprocess

# Create your views here.

APP_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if os.path.exists('/Users/bclavin/'):
    CHROME_EXECUTABLE_PATH = os.path.join(APP_DIR, 'chromedriver', 'mac', 'chromedriver')
    LOCAL_SERVER = True
else:
    CHROME_EXECUTABLE_PATH = os.path.join(APP_DIR, 'chromedriver', 'linux', 'chromedriver')
    LOCAL_SERVER = False


def homepage(request):

    context = {
    }

    template = 'homepage/homepage.html'

    return render(request, template, context)


