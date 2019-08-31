class Answer():
    def __init__(self):
        self.reply = {}

    def add_fulfillment_text(self, text):
        """
        Add optional fulfillment text
        :param text:
        :type string
        :return:
        """
        self.reply['fulfillment_text'] = text

    def add_fulfillment_messages(self, message):
        """
        Add optional fulfillment message
        :param message:
        :type Message
        :return:
        """
        if 'fulfillment_messages' in self.reply.keys():
            self.reply['fulfillment_messages'].append(message)
        else:
            self.reply['fulfillment_messages'] = [message]

    def add_source(self, source):
        """
        Add optional source
        :param source:
        :type string
        :return:
        """
        self.reply['source'] = source

    # Todo: Do I need this ?
    def add_payload(self, payload_struct):
        """
        Add optional payload struct.
        :param payload_struct:
        :type struct
        :return:
        """
        if 'payload' in self.reply:
            self.reply['payload'].update(payload_struct)
        else:
            self.reply['payload'] = payload_struct

    def add_output_contexts(self, context):
        """
        Add optional context to Context[]
        :param context:
        :type
        :return:
        """
        self.reply['output_contexts'] = context

    def add_followup_event_input(self, event_input):
        """
        Add optional eventInput to folloup_event_input
        :param event_input:
        :return:
        """
        self.reply['followup_event_input'] = event_input

    def add_googlePayload(self):
        """
        Enabling Google Payload
        :return:
        """
        self.reply['payload'] = {
            'google': {
                'expectUserResponse': True
            }
        }

    def add_richResponse(self, payload='google'):
        self.reply['payload'][payload]['richResponse'] = {
            'items': []
        }

    def add_simpleResponse(self, simpleResponse, payload='google'):
        self.reply['payload'][payload]['richResponse']['items'].append({
            "simpleResponse": {
                'textToSpeech': simpleResponse
            }
        })

    def add_basicCard(self, basicCard, payload='google'):
        self.reply['payload'][payload]['richResponse']['items'].append({
            'basicCard': basicCard
        })

    def add_systemIntent(self, payload='google'):
        self.reply['payload'][payload]['systemIntent'] = {}

    def add_carouselSelect(self, payload='google'):
        self.reply['payload'][payload]['systemIntent']['intent'] = "actions.intent.OPTION"
        self.reply['payload'][payload]['systemIntent']['data'] = {
            "@type": "type.googleapis.com/google.actions.v2.OptionValueSpec"}
        self.reply['payload'][payload]['systemIntent']['data']['carouselSelect'] = {"items": []}

    def add_carouselSelectItems(self, items, payload='google'):
        self.reply['payload'][payload]['systemIntent']['data']['carouselSelect']['items'] = items

    def create_basicCard(self,title,subtitle,image,buttons):
        return {
            "title":title,
            "image":image,
            "subtitle": subtitle,
            "buttons":buttons,
            "imageDisplayOptions": "CROPPED"
        }

    def create_button(self,title,url):
        return {
            "title":title,
            "openUrlAction":{
                "url":url
            }
        }

    def create_carouselItems(self, id, title, description, imageItem):
        return {
            "optionInfo": {
                "key": id
            },
            "title": title,
            "image": imageItem,
            "description": description
        }

    def create_ImageItem(self, image_url, accessibility_text):
        return {
            "url": image_url,
            "accessibility_text": accessibility_text
        }

    # def create_context

    def sample_ACTIONS_ON_GOOGLE(self):
        self.reply = {
            "payload": {
                "google": {
                    "expectUserResponse": True,
                    "richResponse": {
                        "items": [
                            {
                                "simpleResponse": {
                                    'textToSpeech': "Here you go!"
                                }
                            },
                            {"basicCard": {
                                'title': "Monster Jam",
                                'subtitle': "Monster Jam®, the unexpected, unscripted and unforgettable, most family-friendly motor sport in the world today will tear through Singapore for another adrenaline-pumping event at Singapore’s National Stadium. ...",
                                'image': {
                                    'url': 'http://cdn.eventfinda.sg/uploads/events/transformed/42880-19603-27.jpg',
                                    "accessibilityText": "Image alternate text"
                                }
                            }}
                        ]
                    }
                }
            }
        }
