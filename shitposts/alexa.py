class Alexa:

    def __init__(self, name):
        self.name = name 

    def say(self, something):
        print(something)


alexa = Alexa('alexa')
alexa.say('how do i post images in the python discord')