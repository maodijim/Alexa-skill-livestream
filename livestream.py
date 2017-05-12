def lambda_handler(event, context):
    # TODO implement
    header = {
  "version": "1.0",
  "sessionAttributes": {},
  "response": {
    "outputSpeech": "",
    "card": {
      "type": "Simple",
      "title": "SingTao Chinese Radio",
      "content": "Example of card content. This card has just plain text content.\nThe content is formatted with line breaks to improve readability."
    },
    "directives": "",
    "shouldEndSession": "True"
  }
}
    if event['request']['type'] == 'IntentRequest':
        '''if event['request']['type']'''
        header['response']['outputSpeech'] = {"type":"PlainText", "text":"Radio testing"}
        header['response']['directives'] = [{
                                            "type": "AudioPlayer.Play",
                                            "playBehavior": "REPLACE_ENQUEUED",
                                            "audioItem": {
                                                "stream": {
                                                    "token": "1",
                                                    "url": "https://d2qvjp1n8euzqx.cloudfront.net/nratv/nratv_audio/chunklist.m3u8",
                                                    "offsetInMilliseconds": 0
                                                }
                                            },
                                            "requestId": event['request']['requestId'],
                                            "timestamp": event['request']['timestamp'],
                                            "locale": "en-US"
                                            }]
        return header
    if event['request']['type'] == 'AudioPlayer.PlaybackNearlyFinished ':
        header = {
                    "version": "1.0",
                    "sessionAttributes": {},
                    "response": {
                                 "directives": ""
                    }
        }
        header['response']['directives'] = [{
                                            "type": "AudioPlayer.Play",
                                            "playBehavior": "REPLACE_ENQUEUED",
                                            "audioItem": {
                                                "stream": {
                                                    "token": "1",
                                                    "url": "https://d2qvjp1n8euzqx.cloudfront.net/nratv/nratv_audio/chunklist.m3u8",
                                                    "offsetInMilliseconds": 0
                                                }
                                            },
                                            "requestId": event['request']['requestId'],
                                            "timestamp": event['request']['timestamp'],
                                            "locale": "en-US"
                                            }]
        return header
        
