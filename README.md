# CGS-Project_EventFindaBot


# Introduction

Traditionally tourists visit popular tourist destinations or localities that are well-know for which they prepare an itenary before arrival or hire a local guide. In the midst of this tourism business a market of current events have been untapped. This project is an exploratory attempt at increasing revenue in the below described market.

Generally, popular cities have events of various categories throughout the year, these events are either world-famous (NDP etc) or locally known(NUS Run etc) or events like music concerts, dance shows, tech events, art exhibitions et cetra. These events are not usually attended by toursits because there is no way for them to know what is happening around them.

While, this chatbot is particularly targetted at tourists, it is not limited to the usage of anyone.

From [Google DialogFlow](http://https://dialogflow.com/)
> Give users new ways to interact with your product by building engaging voice and text-based conversational interfaces, such as voice apps and chatbots, powered by AI. Connect with users on your website, mobile app, the Google Assistant, Amazon Alexa, Facebook Messenger, and other popular platforms and devices.

This chatbot is created to bridge the gap that exists for toursists to explore events in Singapore. This is made possible through integration of Google Dialog Flow and EventFinda.sg 
This chatbot can be considered as another form of interaction to EventFinda.sg with a more human touch to it!.

### Installation
Install the dependencies and devDependencies and start the server.
Download ngrok(https://ngrok.com/download) and unzip
```sh
$ cd CGS-Project_EventFindaBot
$ pip3 install requests, flask, json
$ python main.py&
$ ngrok http 5000
```
## GoogleDialogFlow Agent setup 
- Unzip and import agent
- Follow instructions from [here](https://cloud.google.com/dialogflow/docs/agents-manage)
- Enable fulfillment and set the link to the https output from ngrok
