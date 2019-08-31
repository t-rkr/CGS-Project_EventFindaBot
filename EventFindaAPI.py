import requests
import json
from requests.auth import HTTPBasicAuth

EF_QUERY_URL = "http://api.eventfinda.sg/v2/events.json?row=10&fields=event:(url,name,id,description,images)&q={0}" \
         "&order=popularity"
EF_ID_URL = "http://api.eventfinda.sg/v2/events.json?rows=1&id={0}"
EF_API_USERNAME = 'eventfindachatbot'
EF_API_PASSWORD = 'nyrp2bhh98nt'

class Error(Exception):
    pass

def get_event_details(id):
    try:
        url = EF_ID_URL.format(id)
        print(url)
        response = requests.get(url,auth=HTTPBasicAuth(EF_API_USERNAME,EF_API_PASSWORD))
        if response.ok:
            try:
                data = json.loads(response.content)
                #print(data['events'][0]['ticket_types'])
                if data['events']:
                    return dict(
                    id = data['events'][0]['id'],
                    url = data['events'][0]['url'],
                    name = data['events'][0]['name'],
                    description = data['events'][0]['description'],
                    datatime = data['events'][0]['datetime_summary'],
                    location = data['events'][0]['location_summary'],
                    website = data['events'][0]['web_sites']['web_sites'][0]['url'],
                    #ticket_price = data['events'][0]['ticket_types']['ticket_types'][0]['price'],
                    image = "http:"+data['events'][0]['images']['images'][0]['transforms']['transforms'][2]['url'])
                else:
                    return None
            except:
                raise Error("Unable to parse")
    except:
        raise Error("Unable to call API!")

def get_events(eventType):
    eventDetails = []
    try:
        url = EF_QUERY_URL.format(eventType)
        print(url)
        response = requests.get(url,auth=HTTPBasicAuth(EF_API_USERNAME,EF_API_PASSWORD))
        if response.ok:
            try:
                data = json.loads(response.content)['events']
                for items in data:
                    event_id = items['id']
                    event_name = items['name']
                    event_url = items['url']
                    event_description = items['description']
                    event_image = "http:{0}".format(items['images']['images'][0]['transforms']['transforms'][3]['url'])
                    eventDetails.append({
                        'event_id':event_id,
                        'event_name':event_name,
                        'event_url':event_url,
                        'event_description':event_description,
                        'event_image':event_image
                    })
            except:
                raise Error("Could not parse api call!")
        else:
            raise Error("Could not fetch details!")
    except Error:
        pass
    return eventDetails


