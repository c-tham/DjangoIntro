#!/bin/sh
#*************************************************************
#* Welcome to Django folder and files readiness script
#* Created by Chia Tham. Copyright 2018.02.10
#* 
#* V1.00 - Initial 
#* V1.01 - Fixed the styles.css code in the index.html file
#* V1.02 - Display the codes (urls.py & views.py)
#*       - Add name to html title
#*************************************************************
echo "*************************************************************"
echo "Welcome to Django folders and files readiness Version 1.02"
printf "Enter the project name: "
read pname
echo "*************************************************************"
if [ -d $pname ]
then
    echo "Project '$pname' is exists! Please try another project name."
else
    #******************************
    echo ">django-admin startproject $pname"
    django-admin startproject $pname 
    #******************************
fi
echo "*************************************************************"
if [ -d $pname ]
then
    #******************************
    echo "** Main Project folder"
    echo ">mkdir $pname/apps"
    mkdir $pname/apps 
    echo "*************************************************************"
    #******************************
    echo ">touch $pname/apps/__init__.py"
    touch $pname/apps/__init__.py 
    echo "*************************************************************"
    #******************************
    echo "** Project folders"
    echo ">mkdir $pname/apps/$pname"
    mkdir $pname/apps/$pname 
    echo "*************************************************************"
    #******************************
    echo ">touch $pname/apps/$pname/__init__.py"
    touch $pname/apps/$pname/__init__.py 
    echo "*************************************************************"
    #******************************
    echo ">touch $pname/apps/$pname/urls.py"
    touch $pname/apps/$pname/urls.py 
    echo "*************************************************************"
    #******************************
    echo 'from django.conf.urls import url' >> $pname/apps/$pname/urls.py
    echo 'from . import views' >> $pname/apps/$pname/urls.py
    echo ' ' >> $pname/apps/$pname/urls.py
    echo 'urlpatterns = [' >> $pname/apps/$pname/urls.py
    echo "    url(r'^$', views.index)" >> $pname/apps/$pname/urls.py
    echo ']' >> $pname/apps/$pname/urls.py
    echo "*************************************************************"
    #******************************
    echo ">touch $pname/apps/$pname/views.py"
    touch $pname/apps/$pname/views.py 
    echo "*************************************************************"
    #******************************
    echo "** Insert codes into view.py"
    echo 'from django.shortcuts import render, HttpResponse, redirect' >> $pname/apps/$pname/views.py
    echo 'def index(request):' >> $pname/apps/$pname/views.py
    echo '    context = {' >> $pname/apps/$pname/views.py
    echo '        "name" : "'$pname'"' >> $pname/apps/$pname/views.py
    echo '    }' >> $pname/apps/$pname/views.py
    echo '    return render(request, "'$pname'/index.html", context)' >> $pname/apps/$pname/views.py
    cat $pname/apps/$pname/views.py
    echo "*************************************************************"
    #******************************
    echo "** templates folders"
    echo ">mkdir $pname/apps/$pname/templates/$pname"
    mkdir $pname/apps/$pname/templates 
    mkdir $pname/apps/$pname/templates/$pname 
    echo "*************************************************************"
    #******************************
    echo ">touch $pname/apps/$pname/templates/$pname/index.html"
    touch $pname/apps/$pname/templates/$pname/index.html 
    echo "*************************************************************"
    #******************************
    echo "** Insert codes into index.html"
    echo '<!DOCTYPE html>' >> $pname/apps/$pname/templates/$pname/index.html
    echo '<html>' >> $pname/apps/$pname/templates/$pname/index.html
    echo '<head>' >> $pname/apps/$pname/templates/$pname/index.html
    echo '    <meta charset="utf-8">' >> $pname/apps/$pname/templates/$pname/index.html
    echo '    <title>{{name}}</title>' >> $pname/apps/$pname/templates/$pname/index.html
    echo '    {% load static %}' >> $pname/apps/$pname/templates/$pname/index.html
    echo '    <!-- The line above tells Django to be ready to listen for static files -->' >> $pname/apps/$pname/templates/$pname/index.html
    echo "    <link rel='stylesheet' href='{% static '"$pname"/css/styles.css' %}' media='screen' title='no title'  charset='utf-8'>" >> $pname/apps/$pname/templates/$pname/index.html
    echo '    <!-- Put the static files in the static folder inside your app. -->' >> $pname/apps/$pname/templates/$pname/index.html
    echo '    <!-- Django collects files within all static folders and puts them within a single folder --> ' >> $pname/apps/$pname/templates/$pname/index.html
    echo '</head>' >> $pname/apps/$pname/templates/$pname/index.html
    echo '<body>' >> $pname/apps/$pname/templates/$pname/index.html
    echo '    <h1>Hello {{name}} app!</h1>' >> $pname/apps/$pname/templates/$pname/index.html
    echo '</body>' >> $pname/apps/$pname/templates/$pname/index.html
    echo '</html>' >> $pname/apps/$pname/templates/$pname/index.html
    cat $pname/apps/$pname/templates/$pname/index.html
    echo "*************************************************************"
    #******************************
    echo "** static CSS folder"
    echo ">mkdir $pname/apps/$pname/static/$pname/css"
    mkdir $pname/apps/$pname/static 
    mkdir $pname/apps/$pname/static/$pname 
    mkdir $pname/apps/$pname/static/$pname/css 
    echo "*************************************************************"
    #******************************
    echo ">touch $pname/apps/$pname/static/$pname/css/styles.css"
    touch $pname/apps/$pname/static/$pname/css/styles.css 
    echo "*************************************************************"
    #******************************
    echo "** Migraation"
    cd $pname 
    echo "*************************************************************"
    #******************************
    echo ">python manage.py makemigrations"
    python manage.py makemigrations 
    echo "*************************************************************"
    #******************************
    echo ">python manage.py migrate"
    python manage.py migrate 
    echo "*************************************************************"
    echo "*************************************************************"
    #******************************
    echo "** Insert codes below into "$pname"/settings.py"
    echo "INSTALLED_APPS = ["
    echo "    'apps."$pname"', ### added this line!"
    echo "*************************************************************"
    #******************************
    echo "** Insert codes below into "$pname"/urls.py"
    echo "from django.conf.urls import url, include  ### added 'include'"
    echo "from django.contrib import admin"
    echo "urlpatterns = ["
    echo "    url(r'^', include('apps."$pname".urls')), ### add this line"
    echo "]"
    echo "*************************************************************"
    echo "*************************************************************"
    #******************************
    echo "** Execute Django"
    echo "python manage.py runserver"
    echo "*************************************************************"
    #******************************
else
    echo "Djano environment is NOT ready!"
fi
echo "*************************************************************"
