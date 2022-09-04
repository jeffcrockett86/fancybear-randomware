class Meme:
    def __init__(self, origin): 
        self.origin = origin 
        self.is_dank = None 
        if origin.split('/')[-1] == 'memes':
            self.is_dank = False 
        else:
            self.is_dank = True

meme = Meme('https://www.reddit.com/r/memes')
print(meme.is_dank)


