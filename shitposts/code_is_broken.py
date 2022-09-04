from random import choice as either_or 

class Code:
    def __init__(self, is_broken = either_or([True, False])):
        self.is_broken = is_broken
      
code = Code()

print(f'Code is {"broken" if code.is_broken else "not broken"}')