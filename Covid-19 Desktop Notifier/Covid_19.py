import requests 
import json
import plyer
import datetime
import time

#while true, notificaton keeps running until
#force stop or sleep ; line 43
while(1):
    #getting the data from the site
    r = requests.get("https://corona-rest-api.herokuapp.com/Api/india")

    #returns the type of the object r
    print(type(r))

    #returns the data in string file
    news = r.text
    print(news) 

    #to convert the json file into a python data type
    dict1 = json.loads(news)

    #to access the value of 'success' - country
    newdict = dict1['Success']
    print(newdict)

    #control the time limit
    tod = datetime.date.today()

    #converting the date into string to concatenate with the title 
    strtod = tod.strftime("%d.%m.%y")

    #displaying the notification
    plyer.notification.notify(
        title = "Covid-19 notification  "  + strtod,
        message = "Total Cases: " + str(newdict['cases']) + '\n' +
        "Today's Cases: " + str(newdict['todayCases']) + '\n' +
        "Today's Deaths: " + str(newdict['todayDeaths']),
        app_icon = r"/home/chinmayee/Desktop/pyt/covid19_notif/covid19.ico",
        #display notication for 3 seconds
        timeout = 3,
        )
    #repeat the notification every 2 hours
    time.sleep(2*60*60)


