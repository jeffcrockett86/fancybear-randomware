class Mod:
    def __init__(self):
        self.username = 'the_rainmaker' 
        self.is_mod = True 

jeff = Mod()
if jeff.is_mod:
    print(jeff.username == 'the_rainmaker')