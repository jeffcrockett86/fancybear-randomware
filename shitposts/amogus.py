import random

colors = ['Red', 'Blue', 'Green', 'Pink', 
          'Orange', 'Yellow', 'Black', 'White', 
          'Purple', 'Brown', 'Cyan', 'Lime']

class Amogus:
  def __init__(self):
    self.color = random.choice(colors)
    self.sus = random.choice([True, False])
    if self.sus:
      print(self.color, 'is sus')
    else:
      print(self.color, 'is not sus')


red = Amogus()





