from django.shortcuts import render
from django.utils.timezone import datetime
from datetime import date,timedelta
from App1.models import tb
import csv, unidecode

def Index(request):
    if tb.objects.count() > 0:
        Data = tb.objects.all()
        L = tb.objects.last()
        if tb.objects.count() > 20:
            D = Data.reverse()
            D = D[len(D)-20:]   
        context = {"Data": D, "LT": int(L.Temperature), "LH": int(L.Humidity), "LWS": int(L.Wind_Speed), "LMWG": int(L.Max_Wind_Gust), "LPR": int(L.Precipitation), "LSR": int(L.Solar_Radiation)}
        return render(request, "index.html", context)
    else:
        return render(request, "notavailable.html")

def DownloadLDA(request):
    if tb.objects.count() > 0:
        Data = tb.objects.all()
        if tb.objects.count() > 20:
            D = Data.reverse()
            D = D[len(D)-20:]
        Response = HttpResponse(content_type='text/csv')
        Response['Content-Disposition'] = 'attachment; filename="Latest_Data_Available.csv"'
        writer = csv.writer(Response, delimiter=',')
        writer.writerow(['date', 'time', 'temperature ('+unidecode.unidecode(u'\N{DEGREE SIGN}')+'C)', 'humidity (%)', 'wind speed (Km/h)', 'max wind gust (Km/h)', 'solar radiation (W/m2)', 'precipitation (mm)'])
        for obj in D:
            writer.writerow([obj.Date, obj.Time, obj.Temperature, obj.Humidity, obj.Wind_Speed, obj.Max_Wind_Gust, obj.Solar_Radiation, obj.Precipitation])       
        return Response
    else:
        return render(request, "notavailable.html")

def Today(request):
    D = tb.objects.all().filter(Date=date.today())
    L = tb.objects.last()  
    if len(D) != 0:
        context = {"Data": D, "LT": int(L.Temperature), "LH": int(L.Humidity), "LWS": int(L.Wind_Speed), "LMWG": int(L.Max_Wind_Gust), "LPR": int(L.Precipitation), "LSR": int(L.Solar_Radiation)}
        return render(request, "today.html", context)
    else:
        return render(request, "notavailable.html")

def DownloadToday(request):
    D = tb.objects.all().filter(Date=date.today())
    if len(D) != 0:
        Response = HttpResponse(content_type='text/csv')
        Response['Content-Disposition'] = 'attachment; filename="Data_of_Today.csv"'
        writer = csv.writer(Response, delimiter=',')
        writer.writerow(['date', 'time', 'temperature ('+unidecode.unidecode(u'\N{DEGREE SIGN}')+'C)', 'humidity (%)', 'wind speed (Km/h)', 'max wind gust (Km/h)', 'solar radiation (W/m2)', 'precipitation (mm)'])
        for obj in D:
            writer.writerow([obj.Date, obj.Time, obj.Temperature, obj.Humidity, obj.Wind_Speed, obj.Max_Wind_Gust, obj.Solar_Radiation, obj.Precipitation])        
        return Response
    else:
        return render(request, "notavailable.html")

def Yesterday(request):
    D = tb.objects.all().filter(Date=datetime.now().date()-timedelta(1))
    L = tb.objects.last()
    if len(D) != 0:
        context = {"Data": D, "LT": int(L.Temperature), "LH": int(L.Humidity), "LWS": int(L.Wind_Speed), "LMWG": int(L.Max_Wind_Gust), "LPR": int(L.Precipitation), "LSR": int(L.Solar_Radiation)}
        return render(request, "yesterday.html", context)
    else:
        return render(request, "notavailable.html")

def DownloadYesterday(request):
    D = tb.objects.all().filter(Date=datetime.now().date()-timedelta(1))
    if len(D) != 0:
        Response = HttpResponse(content_type='text/csv')
        Response['Content-Disposition'] = 'attachment; filename="Data_of_Yesterday.csv"'
        writer = csv.writer(Response, delimiter=',')
        writer.writerow(['date', 'time', 'temperature ('+unidecode.unidecode(u'\N{DEGREE SIGN}')+'C)', 'humidity (%)', 'wind speed (Km/h)', 'max wind gust (Km/h)', 'solar radiation (W/m2)', 'precipitation (mm)'])
        for obj in D:
            writer.writerow([obj.Date, obj.Time, obj.Temperature, obj.Humidity, obj.Wind_Speed, obj.Max_Wind_Gust, obj.Solar_Radiation, obj.Precipitation])        
        return Response
    else:
        return render(request, "notavailable.html")

def LastWeek(request):
    D = tb.objects.all().filter(Date__gte=datetime.now().date()-timedelta(7), Date__lte=datetime.now().date()-timedelta(1))
    L = tb.objects.last()   
    if len(D) != 0:
        context = {"Data": D, "LT": int(L.Temperature), "LH": int(L.Humidity), "LWS": int(L.Wind_Speed), "LMWG": int(L.Max_Wind_Gust), "LPR": int(L.Precipitation), "LSR": int(L.Solar_Radiation)}
        return render(request, "lastweek.html", context)
    else:
        return render(request, "notavailable.html")

def DownloadLastWeek(request):
    D = tb.objects.all().filter(Date__gte=datetime.now().date()-timedelta(7), Date__lte=datetime.now().date()-timedelta(1))
    if len(D) != 0:
        Response = HttpResponse(content_type='text/csv')
        Response['Content-Disposition'] = 'attachment; filename="Data_of_Last_Week.csv"'
        writer = csv.writer(Response, delimiter=',')
        writer.writerow(['date', 'time', 'temperature ('+unidecode.unidecode(u'\N{DEGREE SIGN}')+'C)', 'humidity (%)', 'wind speed (Km/h)', 'max wind gust (Km/h)', 'solar radiation (W/m2)', 'precipitation (mm)'])
        for obj in D:
            writer.writerow([obj.Date, obj.Time, obj.Temperature, obj.Humidity, obj.Wind_Speed, obj.Max_Wind_Gust, obj.Solar_Radiation, obj.Precipitation])       
        return Response
    else:
        return render(request, "notavailable.html")

def LastMonth(request):
    m = datetime.now().month
    y = datetime.now().year
    if int(m) != 1:
        if len(str(m)) == 1:
            m = '0' + str(int(m)-1)
        else:
            m = str(int(m)-1)
        sw = str(y) + '-' + m    
    else:
        m = '12'
        y =  str(int(y)-1)       
        sw = y + '-' + m 
    D = tb.objects.all().filter(Date__startswith=sw)
    L = tb.objects.last()    
    if len(D) != 0:
        context = {"Data": D, "LT": int(L.Temperature), "LH": int(L.Humidity), "LWS": int(L.Wind_Speed), "LMWG": int(L.Max_Wind_Gust), "LPR": int(L.Precipitation), "LSR": int(L.Solar_Radiation)}
        return render(request, "lastmonth.html", context)
    else:
        return render(request, "notavailable.html") 

def DownloadLastMonth(request):
    m = datetime.now().month
    y = datetime.now().year
    if int(m) != 1:
        if len(str(m)) == 1:
            m = '0' + str(int(m)-1)
        else:
            m = str(int(m)-1)
        sw = str(y) + '-' + m    
    else:
        m = '12'
        y =  str(int(y)-1)       
        sw = y + '-' + m 
    D = tb.objects.all().filter(Date__startswith=sw)   
    if len(D) != 0:
        Response = HttpResponse(content_type='text/csv')
        Response['Content-Disposition'] = 'attachment; filename="Data_of_Last_Month.csv"'
        writer = csv.writer(Response, delimiter=',')
        writer.writerow(['date', 'time', 'temperature ('+unidecode.unidecode(u'\N{DEGREE SIGN}')+'C)', 'humidity (%)', 'wind speed (Km/h)', 'max wind gust (Km/h)', 'solar radiation (W/m2)', 'precipitation (mm)'])
        for obj in D:
            writer.writerow([obj.Date, obj.Time, obj.Temperature, obj.Humidity, obj.Wind_Speed, obj.Max_Wind_Gust, obj.Solar_Radiation, obj.Precipitation])      
        return Response
    else:
        return render(request, "notavailable.html")        

def AllTime(request):
    if tb.objects.count() > 0:
        D = tb1.objects.all()
        L = tb1.objects.last()    
        context = {"Data": D, "LT": int(L.Temperature), "LH": int(L.Humidity), "LWS": int(L.Wind_Speed), "LMWG": int(L.Max_Wind_Gust), "LPR": int(L.Precipitation), "LSR": int(L.Solar_Radiation)}
        return render(request, "alltime.html", context)
    else:
        return render(request, "notavailable.html") 

def DownloadAllTime(request):
    if tb.objects.count() > 0:
        D = tb.objects.all()
        Response = HttpResponse(content_type='text/csv')
        Response['Content-Disposition'] = 'attachment; filename="Data_of_All_Time.csv"'
        writer = csv.writer(Response, delimiter=',')
        writer.writerow(['date', 'time', 'temperature ('+unidecode.unidecode(u'\N{DEGREE SIGN}')+'C)', 'humidity (%)', 'wind speed (Km/h)', 'max wind gust (Km/h)', 'solar radiation (W/m2)', 'precipitation (mm)'])
        for obj in D:
            writer.writerow([obj.Date, obj.Time, obj.Temperature, obj.Humidity, obj.Wind_Speed, obj.Max_Wind_Gust, obj.Solar_Radiation, obj.Precipitation])      
        return Response
    else:
        return render(request, "notavailable.html")

def Custom(request):
    if request.GET.get("startdate") and request.GET.get("enddate"):
        date1 = request.GET.get("startdate")
        date2 = request.GET.get("enddate")
        SD = datetime.strptime(date1, '%Y-%m-%d').date()
        ED = datetime.strptime(date2, '%Y-%m-%d').date()
        D = tb1.objects.all().filter(Date__range=[SD,ED])
        L = tb1.objects.last()
        if len(D) != 0:
            context = {"Data": D, "LT": int(L.Temperature), "LH": int(L.Humidity), "LWS": int(L.Wind_Speed), "LMWG": int(L.Max_Wind_Gust), "LPR": int(L.Precipitation), "LSR": int(L.Solar_Radiation)}
            return render(request, "custom.html", context)
        else:
            return render(request, "notavailable.html")              

def DownloadCD(request):
    if request.GET.get("startdate") and request.GET.get("enddate"):
        date1 = request.GET.get("startdate")
        date2 = request.GET.get("enddate")
        SD = datetime.strptime(date1, '%Y-%m-%d').date()
        ED = datetime.strptime(date2, '%Y-%m-%d').date()
        D = tb1.objects.all().filter(Date__range=[SD,ED])
        if len(D) != 0:
            Response = HttpResponse(content_type='text/csv')
            Response['Content-Disposition'] = 'attachment; filename="Customized_Data.csv"'
            writer = csv.writer(Response, delimiter=',')
            writer.writerow(['date', 'time', 'temperature ('+unidecode.unidecode(u'\N{DEGREE SIGN}')+'C)', 'humidity (%)', 'wind speed (Km/h)', 'max wind gust (Km/h)', 'solar radiation (W/m2)', 'precipitation (mm)'])
            for obj in D:
                writer.writerow([obj.Date, obj.Time, obj.Temperature, obj.Humidity, obj.Wind_Speed, obj.Max_Wind_Gust, obj.Solar_Radiation, obj.Precipitation])       
            return Response
        else:
            return render(request, "notavailable.html")
