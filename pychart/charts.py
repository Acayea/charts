# imports 
from PIL import Image, ImageDraw
import time
# import sqlite3
import numpy as np
import os
import pysqlite3
sqlite3 = pysqlite3

#  global constants

conn = sqlite3.connect('charts.db')
cursor = conn.cursor()

output_dir = "images"
os.makedirs(output_dir, exist_ok=True)




Via = [1,1,1,1]
Cauda_Draconis = [1,1,1,0]
Puer = [1,1,0,1]
Fortuna_minor= [1,1,0,0]
Puella = [1,0,1,1]
Amissio = [1,0,1,0]
Carcer = [1,0,0,1]
Laetitia = [1,0,0,0]
Caput_Draconis = [0,1,1,1]
Conjunctio = [0,1,1,0]
Acquisitio = [0,1,0,1]
Rubeus = [0,1,0,0]
Fortuna_Major = [0,0,1,1]
Albus = [0,0,1,0]
Tristitia = [0,0,0,1]
Populus = [0,0,0,0]
signs = [ Via , Cauda_Draconis , Puer , Fortuna_minor, Puella , Amissio , Carcer , Laetitia,Caput_Draconis ,Conjunctio ,Acquisitio ,Rubeus ,Fortuna_Major,Albus ,Tristitia,Populus]
# 0 is 2 dots 1 is 1 dot

M1 = []
M2 = []
M3 = []
M4 = []
D1 = []
D2 = []
D3 = []
D4 = []
N1 = []
N2 = []
N3 = []
N4 = []
WR = []
WL = []
J = []


def main():

    while True :
        choice= int(input("enter choice - 1 generate \n 2 \n 9 db generation "))
        if choice == 1 :
           data.generate()
        elif choice == 2:

        # elif choice == 3:
        # elif choice == 4:
        # elif choice == 5:
        # elif choice == 6:
        # elif choice == 7:
        # elif choice == 8:
            image.make_chart()
        elif choice == 9:
            data.dbgen()
        elif choice == 99:
            conn.commit()
    # start_time = time.time()
    
    
    
    
    end_time = time.time()
    
    elapsed_time = end_time - start_time 
    
    print(f"Elapsed time : {elapsed_time:.10f} seconds")
    




class data:

    def generate():
        count = 0
        for M1 in signs:
            for M2 in signs:
                for M3 in signs:
                    for M4 in signs:
                        D1 = [M1[0],M2[0],M3[0],M4[0]]
                        D2 = [M1[1],M2[1],M3[1],M4[1]]
                        D3 = [M1[2],M2[2],M3[2],M4[2]]
                        D4 = [M1[3],M2[3],M3[3],M4[3]]
                        N1 = np.bitwise_xor(M1,M2)
                        N2 = np.bitwise_xor(M3,M4)
                        N3 = np.bitwise_xor(D1,D2)
                        N4 = np.bitwise_xor(D3,D4)
                        WR = np.bitwise_xor(N1,N2)
                        WL = np.bitwise_xor(N3,N4)
                        J = np.bitwise_xor(WR ,WL)
                        count += 1
                        cursor.execute(''' insert OR IGNORE into charts 
                                           (name, h1, h2, h3, h4, h5, h6, h7, h8, h9, h10, h11, h12, RW, LW, J)
                                            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                        ''',(f"chart_{count}",
                            str(M1), str(M2), str(M3), str(M4),
                            str(D1), str(D2), str(D3), str(D4),
                            str(N1.tolist()), str(N2.tolist()), str(N3.tolist()), str(N4.tolist()),
                            str(WR.tolist()), str(WL.tolist()), str(J.tolist())))
                        
                        # img = image.make_chart(M1,M2,M3,M4,D1,D2,D3,D4,N1,N2,N3,N4,WR,WL,J)
                        # # img.show()  # or 
                        img.save(os.path.join(output_dir, f"{count}.png"))

    def dbgen():
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS charts (
                id INTEGER PRIMARY KEY,
                name TEXT UNIQUE NOT NULL,
                h1 TEXT NOT NULL,
                h2 TEXT NOT NULL,
                h3 TEXT NOT NULL,
                h4 TEXT NOT NULL,
                h5 TEXT NOT NULL,
                h6 TEXT NOT NULL,
                h7 TEXT NOT NULL,
                h8 TEXT NOT NULL,
                h9 TEXT NOT NULL,
                h10 TEXT NOT NULL,
                h11 TEXT NOT NULL,
                h12 TEXT NOT NULL,
                RW TEXT NOT NULL,
                LW TEXT NOT NULL,
                J TEXT NOT NULL
            )
        ''')

class image:
    
    DOT_RADIUS = 6
    DOT_SPACING = 20
    FIGURE_SPACING_X = 100
    FIGURE_SPACING_Y = 120

    def draw_dot(draw, x, y):
        r = image.DOT_RADIUS
        draw.ellipse((x-r, y-r, x+r, y+r), fill="black")

    def draw_line(draw, x, y, value):
        """Draw one row of a figure (1 or 2 dots)."""
        if value == 1:
            image.draw_dot(draw, x, y)
        elif value == 0:
            image.draw_dot(draw, x-10, y)
            image.draw_dot(draw, x+10, y)

    def draw_figure(draw, x, y, figure):
        """Draw a geomantic figure at (x,y)."""
        for i, val in enumerate(figure):
            row_y = y + i * image.DOT_SPACING
            image.draw_line(draw, x, row_y, val)

    def make_chart(M1, M2, M3, M4, D1, D2, D3, D4,
                N1, N2, N3, N4, WR, WL, J):
        # Canvas big enough for all figures
        img = Image.new("RGB", (800, 800), "white")
        draw = ImageDraw.Draw(img)

        draw.line([(25, 25), (775, 25)], fill="blue", width=5)
        draw.line([(775, 25), (775, 775)], fill="blue", width=5)
        draw.line([(775, 775), (25, 775)], fill="blue", width=5)
        draw.line([(25, 775), (25, 25)], fill="blue", width=5)

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
        image.draw_figure(draw, 100, 162.5, M1)
        image.draw_figure(draw, 100, 370, M2)
        image.draw_figure(draw, 100, 577.5, M3)
        image.draw_figure(draw, 200, 660, M4)
        # Daughters (left side, bottom up)
        image.draw_figure(draw, 400, 660, D1)
        image.draw_figure(draw, 600, 660, D2)
        image.draw_figure(draw, 700, 577.5, D3)
        image.draw_figure(draw, 700, 370, D4)
        # Nieces (middle column, bottom up)
        image.draw_figure(draw, 700, 162.5, N1)
        image.draw_figure(draw, 600, 100, N2)
        image.draw_figure(draw, 400, 100, N3)
        image.draw_figure(draw, 200, 100, N4)
        # Witnesses (above Nieces)
        image.draw_figure(draw, 300, 280, WR)  # right witness
        image.draw_figure(draw, 500, 280, WL)  # left witness
        # Judge (top center)
        image.draw_figure(draw, 400, 480, J)
        return img

       


if __name__ == "__main__":
    main()