'''
#                   -Created and coded by Artur | WGvuik
'''
from PIL import Image
import random
from config import *


class html_arts:
    def __init__(self, image:str):
        self.im = Image.open(image) 
        self.pixels = self.im.load() # this is not a list, nor is it list()'able
        self.width, self.height = self.im.size

    def __rgb2hex(self, r, g, b):
        return '#{:02x}{:02x}{:02x}'.format(r, g, b)
    
    def __fast_write(self) -> None:
        r, g, b, a = self.pixels[self.x, self.y]
        self.file.write('\t\t<td bgcolor="{}"></td>\n'.format(self.__rgb2hex(r, g, b)))
        
    def __features(self) -> None:
        if glitch_effect:
            if random.randint(0, 1):
                self.x += x_offset
                self.__fast_write()
            else:
                self.x += 1
                self.__fast_write()
        elif compressed:
            self.x += self.x_offset
            self.__fast_write()
        else:
            self.x += 1
            
                
    def startup(self):
        with open("output.html", "w") as file:
            self.file = file
            file.write(HTML_START)
            for y in range(self.height):
                self.y = y
                self.x = 0
                file.write("\t<tr>\n")
    
                while (self.x + x_offset < self.width):
                    self.__features()
                file.write("\t</tr>\n")
            file.write(HTML_END)
    
def main() -> None:
    art = html_arts(path2image)
    art.startup()

main()
