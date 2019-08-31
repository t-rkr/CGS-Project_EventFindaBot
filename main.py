from flask import Flask, request, Response
import json
import Answer
import pickledb
import EventFindaAPI

app = Flask('__name__')
db = pickledb.load('dataStore.db', False)

def parse_params(parameters):
    valid_params = {}
    for items in [params for params in parameters if parameters[params]]:
        valid_params[items] = parameters[items]
    return valid_params


@app.route('/', methods=['POST'])
def main():
    # Request is made, check the intent
    dialog = request.get_json(silent=True, force=True)
    session = dialog['session'].split('/')[4]
    intent = dialog['queryResult']['intent']['displayName']
    query = dialog['queryResult']['queryText']
    parameters = parse_params(dialog['queryResult']['parameters'])
    print(session, intent, query, parameters)

    answer = Answer.Answer()

    if intent == 'events.search':
        events = EventFindaAPI.get_events(parameters['events-type'])
        # Todo: store events
        event_items = []
        if events:
            for event in events:
                event_items.append(answer.create_carouselItems(event['event_id'], event['event_name'],
                                                               event['event_description'],
                                                               answer.create_ImageItem(
                                                                   event['event_image'], "find out more.")))

            answer.add_googlePayload()
            answer.add_richResponse()
            answer.add_simpleResponse("Here are the search results:")
            answer.add_systemIntent()
            answer.add_carouselSelect()
            if len(event_items) > 4:
                answer.add_carouselSelectItems(event_items[:4])
            else:
                answer.add_carouselSelectItems(event_items)
            # answer.add_followup_event_input()
        # Dump details into dataStore
        datatoStore = {'session_id': session, 'query': query, 'parameters': parameters, 'intents': [intent],
                       'events': event_items}

        db.set(session, datatoStore)
        db.dump()

    if intent == 'events.search.itemDetails':
        print(dialog['originalDetectIntentRequest']['payload']['inputs'])
        event_details = [item_detail for item_detail in db.get(session)['events'] if item_detail['title']]
        print(event_details)
        event_id = event_details[0]['optionInfo']['key']
        event_details = EventFindaAPI.get_event_details(event_id)
        if event_details:
            answer.add_googlePayload()
            answer.add_richResponse()
            answer.add_simpleResponse("Here are the additional details...")
            # card = answer.create_basicCard("Tarun","Tarun",answer.create_ImageItem(
            #     "'http://cdn.eventfinda.sg/uploads/events/transformed/42880-19603-27.jpg","Tarun"),
            #                                answer.create_button("Tarun",'htttps://google.com'))
            # answer.add_basicCard(card)
            #print(card)
            answer.add_basicCard(answer.create_basicCard(event_details['name'],event_details['description'],
                                                         answer.create_ImageItem(event_details['image'],
                                                                                 event_details['name']),
                                                         [answer.create_button("More Details",event_details['url'])]))
        else:
            answer.add_googlePayload()
            answer.add_richResponse()
            answer.add_simpleResponse("Sorry, we are currently unable to find details for this event!")
        #answer.sample_ACTIONS_ON_GOOGLE()

        #answer.sample_ACTIONS_ON_GOOGLE()
    # return "${events-type}"

    print(answer.reply)
    return Response(json.dumps(answer.reply), status=200, content_type="application/json")


if __name__ == '__main__':
    app.run()
