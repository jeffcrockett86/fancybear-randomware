class Dick:

    def __init__(self, emoji, string):
        self.emoji = emoji
        self.string = string   
        self.size = 'thicc'
        self.be_long = True

def suck_that(dick):
    dick_ = Dick('🍆', dick)
    if len(dick_.string) == 1:
        print('schlurp')
        return
    if dick_.emoji == '🍆' and dick_.be_long and dick_.size == 'thicc':
        print(dick_.string)
        return suck_that(dick_.string[:-1])

suck_that('8============D')



