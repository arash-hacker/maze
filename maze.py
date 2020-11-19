#!/bin/env python3
import random
import cairo
N=20
M=30

class Maze:

    def __init__(self,N):
        self.edges=[]
        for i in range(N+1):
            for j in range(N+1):
                i+1<=N and self.edges.append(((i,j),(i+1,j)))
                j+1<=N and self.edges.append(((i,j),(i,j+1)))


    def gen(self):
        for i in range(N*10):
            ((x1,y1),(_,_))=self.edges.pop(random.randint(1,len(self.edges)-2))
            ((_,_),(x2,y2))=self.edges.pop(random.randint(1,len(self.edges)-2))
            self.sel(x1,y1,x2,y2)

    def sel(self,x1,y1,x2,y2):
        l=[]
        for x in range(min(x1,x2),max(x1,x2)-1):
            l.append((x,min(y1,y2)))
        for y in range(min(y1,y2),max(y1,y2)-1):
            l.append((max(x1,x2),y))
        for x,y in l:
            if (x,y) in self.edges:
                self.edges.pop(self.edges.index((x,y)))

    def inspect(self):
        print(">>>",len(self.edges))    

    def draw(self):
        surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 512, 512)
        ctx = cairo.Context(surface)
        ctx.set_source_rgb(1, 1, 1)
        ctx.paint()
        ctx.set_source_rgb(0, 0, 0)
        ctx.set_line_width(3)
        ctx.set_line_cap(cairo.LINE_CAP_ROUND)
        ctx.move_to(0,0)
        ctx.move_to(200,200)
        for ((x,y),(xx,yy)) in self.edges:
            ctx.move_to(M*x,M*y)
            ctx.line_to(M*(xx),M*yy)

        ctx.stroke()
        surface.write_to_png("out.png")

m=Maze(N)
m.inspect()
m.gen()
m.draw()
m.inspect()