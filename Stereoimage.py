from PIL import Image as im
import random

CONSTANT_OF_DEPTH = 0.3

class Stereoimage:

    def __init__(self, x_dim, y_dim, divisions):
        self.x_dim = x_dim
        self.y_dim = y_dim
        self.seg_width = int(x_dim/divisions)

        
        self.segment = im.new("RGBA", (self.seg_width, y_dim))
        
        for x in range(self.seg_width):
            for y in range(y_dim):
                color = (random.randint(0,255),random.randint(0,255),random.randint(0,255),255)
                self.segment.putpixel((x,y), color)

        self.canvas = im.new("RGBA", (x_dim, y_dim))

        for i in range(divisions):
            self.canvas.paste(self.segment.copy(),(i*int(x_dim/divisions),0))

    def __pixel_to_depth(self, pixel):
        return int((pixel[0] / 255.0) * (CONSTANT_OF_DEPTH * self.seg_width))

    def mod_depth(self, map):
        for x in range(self.x_dim):
            for y in range(self.y_dim):
                depth = self.__pixel_to_depth(map.getpixel((x,y)))
                shift = self.seg_width - depth

                self.canvas.putpixel((x,y), self.canvas.getpixel((x-shift,y)))
    
    def get_canvas(self):
        return self.canvas
        
    
