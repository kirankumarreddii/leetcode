class Solution:
    def similarRGB(self, color: str) -> str:
        def colore(c):
            dec=int(c,16)
            close=round(dec/17)*17
            return "{:02x}".format(close)






        red=colore(color[1:3])
        blue=colore(color[3:5])
        green=colore(color[5:7])
        return "#"+red+blue+green