from PIL import Image as im
import random
import Stereoimage

def main():
    
    img = Stereoimage.Stereoimage(800,400,8)
    img.mod_depth(im.open("depth_map.png"))
    img.get_canvas().show()
                    
if __name__ == "__main__":
    main()