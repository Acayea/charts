from PIL import Image, ImageDraw

# Parameters
DOT_RADIUS = 6
DOT_SPACING = 20
FIGURE_SPACING_X = 100
FIGURE_SPACING_Y = 120

def draw_dot(draw, x, y):
    r = DOT_RADIUS
    draw.ellipse((x-r, y-r, x+r, y+r), fill="black")

def draw_line(draw, x, y, value):
    """Draw one row of a figure (1 or 2 dots)."""
    if value == 1:
        draw_dot(draw, x, y)
    elif value == 2:
        draw_dot(draw, x-10, y)
        draw_dot(draw, x+10, y)

def draw_figure(draw, x, y, figure):
    """Draw a geomantic figure at (x,y)."""
    for i, val in enumerate(figure):
        row_y = y + i * DOT_SPACING
        draw_line(draw, x, row_y, val)

def make_chart(M1, M2, M3, M4, D1, D2, D3, D4,
               N1, N2, N3, N4, RW, LW, J):
    # Canvas big enough for all figures
    img = Image.new("RGB", (800, 800), "white")
    draw = ImageDraw.Draw(img)



    draw.line([(25, 25), (775, 25)], fill="blue", width=5)
    draw.line([(775, 25), (775, 775)], fill="blue", width=5)
    draw.line([(775, 775), (25, 775)], fill="blue", width=5)
    draw.line([(25, 775), (25, 25)], fill="blue", width=5)

    # draw.line([(125, 125), (675, 125)], fill="blue", width=5)
    # draw.line([(675, 125), (675, 575)], fill="blue", width=5)
    # draw.line([(675, 575), (125, 575)], fill="blue", width=5)
    # draw.line([(125, 575), (125, 125)], fill="blue", width=5)

    draw.line([(200, 200), (600, 200)], fill="blue", width=5)
    draw.line([(600, 200), (600, 600)], fill="blue", width=5)
    draw.line([(600, 600), (200, 600)], fill="blue", width=5)
    draw.line([(200, 600), (200, 200)], fill="blue", width=5)

    draw.line([(25, 25), (200, 200)], fill="blue", width=5)
    draw.line([(25, 775), (200, 600)], fill="blue", width=5)
    draw.line([(775, 25), (600, 200)], fill="blue", width=5)
    draw.line([(775, 775), (600, 600)], fill="blue", width=5)

    draw.line([(200, 200), (25, 400)], fill="blue", width=5)
    draw.line([(200, 600), (25, 400)], fill="blue", width=5)
    draw.line([(200, 600), (400, 775)], fill="blue", width=5)
    draw.line([(600, 600), (400, 775)], fill="blue", width=5)
    draw.line([(600, 600), (775, 400)], fill="blue", width=5)
    draw.line([(600, 200), (775, 400)], fill="blue", width=5)
    draw.line([(600, 200), (400, 25)], fill="blue", width=5)
    draw.line([(200, 200), (400, 25)], fill="blue", width=5)
    
    draw.line([(200, 400), (600, 400)], fill="blue", width=5)
    draw.line([(400, 200), (400, 400)], fill="blue", width=5)






    # Mothers (right side, bottom up)
    draw_figure(draw, 100, 162.5, M1)
    draw_figure(draw, 100, 370, M2)
    draw_figure(draw, 100, 577.5, M3)
    draw_figure(draw, 200, 660, M4)

    # Daughters (left side, bottom up)
    draw_figure(draw, 400, 660, D1)
    draw_figure(draw, 600, 660, D2)
    draw_figure(draw, 700, 577.5, D3)
    draw_figure(draw, 700, 370, D4)

    # Nieces (middle column, bottom up)
    draw_figure(draw, 700, 162.5, N1)
    draw_figure(draw, 600, 100, N2)
    draw_figure(draw, 400, 100, N3)
    draw_figure(draw, 200, 100, N4)

    # Witnesses (above Nieces)
    draw_figure(draw, 300, 280, RW)  # right witness
    draw_figure(draw, 500, 280, LW)  # left witness

    # Judge (top center)
    draw_figure(draw, 400, 480, J)

    return img

# Example usage
M1 = [1,2,1,2]
M2 = [2,1,2,1]
M3 = [1,1,2,2]
M4 = [2,2,1,1]
D1 = [1,2,2,1]
D2 = [2,1,1,2]
D3 = [1,1,1,2]
D4 = [2,2,2,1]
N1 = [1,2,1,1]
N2 = [2,1,2,2]
N3 = [1,1,2,1]
N4 = [2,2,1,2]
RW = [1,1,1,1]
LW = [2,2,2,2]
J  = [1,2,1,2]

img = make_chart(M1,M2,M3,M4,D1,D2,D3,D4,N1,N2,N3,N4,RW,LW,J)
img.show()  # or img.save("chart.png")

exit