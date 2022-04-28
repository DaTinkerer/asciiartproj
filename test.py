from PIL import Image
import sys, random, argparse
import numpy as np
import math
 

gscale1 = '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~i!lI;:,\"^`". '
gscale2 = '@%#*+=-:. '

image = Image.open(fileName).convert('L')

W, H = image.size[0], image.size[1]
w = W/cols
h = w/scale
rows = int(H/h)