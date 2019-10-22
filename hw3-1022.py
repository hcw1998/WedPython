# coding: utf-8
from IPython.display import display, HTML, Markdown, Image, YouTubeVideo
def choose(x):
    if(x == 1):
        myvideo = YouTubeVideo('5QKydStn8YU')
    elif(x == 2):
        myvideo = YouTubeVideo('gwDoRPcPxtc')
    elif(x == 3):
        myvideo = YouTubeVideo('YIpNFB2rFEY')
    display(myvideo)
interact(choose, x = {"study":1, "chill":2, "sorrow":3})
