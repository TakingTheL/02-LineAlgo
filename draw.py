from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    if(x0 > x1):
        draw_line(x1, y1, x0, y0, screen, color)
        return
    
    #define constants
    a = y1 - y0 #delta y
    b = x0 - x1 #- delta x
    x = x0
    y = y0
    
    #if octant 1
    if ((-1 * b) >= a and a >= 0):
        d = a + a + b

        a += a #a => 2a
        b += b #b => 2b
        while(x <= x1):
            plot(screen, color, x, y)
            if (d > 0):
                y += 1
                d += b
            x += 1
            d += a
        return
    
    #if octant 2
    if (a > (-1 * b)):
        d = a + b + b

        a += a #a => 2a
        b += b #b => 2b
        while(y <= y1):
            plot(screen, color, x, y)
            if (d < 0):
                x += 1
                d += a
            y += 1
            d += b
        return
    
    #if octant 7
    if (a <= b):
        d = a + b + b
        a += a
        b += b
        while(x <= x1):
            plot(screen, color, x, y)
            if (d < 0):
                x += 1
                d -= a
            y -= 1
            d += b
        return
    
    #if octant 8
    if (b < a and a < 0):
        d = a + a + b
        a += a
        b += b
        while(x <= x1):
            plot(screen, color, x, y)
            if ( d > 0):
                y -= 1
                d += b
            x += 1
            d -= a

    #horizontal lines, slope == +-1 lines
