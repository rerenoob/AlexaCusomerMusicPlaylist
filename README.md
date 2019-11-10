# AlexaCustomMusicPlaylist

 Create your own playlist for Alexa.
 
## General

This is for a hosted skill. The code for this skill was partially auto-generated when the alexa-hosted skill was createed. Some development familiarity is needed to fill in some required information for a new Alexa skill. 

## Set up

To create a hosted skill, go to the Alexa [skill creation page](https://developer.amazon.com/alexa/console/ask/create-new-skill) and select "Custom Skill", then select "Alexa-Hosted (Python)". This option is incredibly convenient as you don't need to host or maintain anything yourself. AWS basically does all of the boil-plate and heavy-lifting for you.

## Where to store your music

After the skill has been created, go to the "Code" section of the skill. On the lower left corner of the Code page, you should see the auto-generated CloudWatch account and S3 bucket. Click on the S3 bucket link (Media Storage: S3 [0/5GB]). 5GB is a generous amount of space for your music need.

## The code folder

By default, you should have the following file in the auto-generated code:
```
.
├── lambda_function.py
├── requirements.txt
└── utils.py
```

Add the Alexa folder to your code repository, then modify the existing files. The final structure should look like this.
```
.
├── alexa
│   ├── __init__.py
│   ├── data.py
│   └── util.py
├── lambda_function.py
├── requirements.txt
└── utils.py
```

## Key function explaination

The following function is started when you start the skill:

```
class PlayIntentHandler(AbstractRequestHandler):
    """Handler for Play Intent."""
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("PlayIntent")(handler_input)
        
    def handle(self, handler_input):
        presignedUrl = utils.create_presigned_url(utils.get_random_song())
        return util.play(url=presignedUrl,
                         offset=0,
                         text="Let's play",
                         card_data="",
                         response_builder=handler_input.response_builder)
```

Pay attention to the ```handle``` function. When the skill is invoked, a presigned url to the song is generated. This url is then queued to the current playlist. 

## What the skill does

Well, it plays your music for you. Specifically, the music you store in the S3 bucker. It pulls a random song, plays it, and queues another random song. The RNG isn't ideal, so it may play a song twice in a row. If you can improve it, please do so 😊
