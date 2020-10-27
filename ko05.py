import pygame as pg
import tkinter as tk
from random import randint, choice
import os
import webbrowser
import json

# print("Propvide password")
# while input() != "1234": print("Provide password")

# Setup
try:
    resolution = (0, 0)
    title = "Παιχνίδι Κο-05"
    pg.init()
    screen = pg.display.set_mode(resolution, pg.DOUBLEBUF | pg.FULLSCREEN)
    width, height = pg.display.get_surface().get_size()
    pg.display.set_caption(title)
except Exception as e:
    print("Error while initiating pygame\n\t")
    print(e)
    

def scaleTimes(surf: pg.Surface, times):
    return pg.transform.scale(surf, (int(surf.get_width() * times), int(surf.get_height() * times)))


def scaleLockAspect(surf: pg.Surface, width):
    return scaleTimes(surf, width / surf.get_width())


# Constants
colors = {'bckColor': (31, 194, 61), 'black': (0, 0, 0), 'white': (255, 255, 255), 'red': (255, 0, 0),
          'green': (0, 255, 0), 'blue': (0, 0, 255), 'cyan': (0, 255, 255), 'purple': (255, 0, 255),
          'yellow': (255, 255, 0), 'btn': (191, 191, 191), 'btnPressed': (138, 138, 138), 'btnText': (31, 31, 31),
          'cardBorder': (102, 102, 102), 'text1': (33, 33, 33), 'text2': (133, 6, 150), 'extBtnPressed': (176, 0, 0),
          'light-grey':(212, 212, 212), 'dark-grey': (102, 102, 102), 'lime': (150, 201, 30), 'bckgnd': (235, 235, 235)}
srcDir = './ko05-src/'
wR = width / 1920
## Images
try:
    logo1Img = scaleLockAspect(pg.image.load(os.path.join(srcDir, 'logo1_tr.png')).convert_alpha(), 100)
    logo2Img = scaleLockAspect(pg.image.load(os.path.join(srcDir, 'logo2_tr.png')).convert_alpha(), 30)
    mainImg = scaleLockAspect(pg.image.load(os.path.join(srcDir, 'img1.jpg')).convert(), 600 * wR)
    meterImg = scaleLockAspect(pg.image.load(os.path.join(srcDir, 'img2.png')).convert_alpha(), 250 * wR)
    ## Fonts
    nxtBtnTxt = pg.font.SysFont('calibri-bold', 34)
    extBtnTxt = pg.font.SysFont('arial-bold', 38)
    logoTxt = pg.font.SysFont('calibri', 16)
    titleTxt = pg.font.SysFont('calibri-bold', 30)
    cardTxt = pg.font.SysFont('arial', 24)
    ## Load Cards
    with open(os.path.join(srcDir, 'cards.json'), 'r', encoding='utf-8') as f:
        cardsTemplate = json.load(f)
    cards = []
    cardContent = ''

    loaded = True
except Exception as e:
    loaded = False
    print("Error while loading files!\n\t")
    print(e)


class InfoWindow(tk.Tk):
    def __init__(self, title, msg):
        tk.Tk.__init__(self)
        self.title(title)
        tk.Label(self, text=msg, justify=tk.LEFT).grid(row=0, column=0, padx=15, pady=15)
        tk.Label(self, text='Software Developer: Frank Fourlas', justify=tk.RIGHT).grid(row=1, column=0, sticky=tk.E, padx=15)
        link = tk.Label(self, text='github.com/frank20a', justify=tk.RIGHT, fg="blue", cursor="hand2")
        link.bind("<Button-1>", lambda e: webbrowser.open_new("https://github.com/frank20a"))
        link.grid(row=2, column=0, sticky=tk.E, padx=15)
        tk.Button(self, text="Close", command=lambda: self.destroy()).grid(row=3, column=0, sticky=tk.E, padx=15,
                                                                           pady=15)
        self.attributes("-topmost", True)
        self.mainloop()


def drawCardText(scr, cont, posx, posy):
    for key in cont:
        if len(cont[key]) > 0:
            txt = cont[key].split(' ')
            while len(txt):
                temp = []
                while len(' '.join(temp)) < 39 and len(txt) > 0: temp.append(txt.pop(0))
                scr.blit(cardTxt.render(' '.join(temp), True, colors[key]), (posx, posy))
                posy += 25


# Run
running = loaded and pg.get_init()
while running:

    # Configure Button Colors
    ## Next Button
    try:
        if btnNext.collidepoint(pg.mouse.get_pos()):
            btnCol = colors['btnPressed']
        else:
            btnCol = colors['btn']
    except:
        btnCol = colors['btn']
    ## Instructions Text Button
    try:
        if btnInstruct.collidepoint(pg.mouse.get_pos()):
            instructCol = colors['blue']
        else:
            instructCol = colors['black']
    except:
        instructCol = colors['black']
    ## Exit Button
    try:
        if btnClose.collidepoint(pg.mouse.get_pos()):
            extBtnCol = colors['extBtnPressed']
        else:
            extBtnCol = colors['red']
    except:
        extBtnCol = colors['red']

    # Canvas
    screen.fill(colors['bckgnd'])
    pg.draw.rect(screen, colors['lime'], pg.Rect(width-125, 25, 50, 25))
    pg.draw.rect(screen, colors['dark-grey'], pg.Rect(width-125, 25, 50, 25), 2)
    screen.blit(logoTxt.render("Κο-05", True, colors['dark-grey']), (width-118, 32))

    # Logos
    screen.blit(logo1Img, (25, 25))
    screen.blit(logo2Img, (25, height - 55))
    screen.blit(logoTxt.render("Κέντρο Έρευνας και Θεραπείας Τραυλισμού", True, colors['black']), (70, height - 45))
    t = logoTxt.render("Λεξιπόντιξ: Πρόγραμμα Θεραπείας Τραυλισμού για Παιδιά Σχολικής Ηλικίας.      © Φούρλας,"
                               " Γ. και Μαρούσος, Δ. (2019).", True, colors['black'])
    screen.blit(t, (int(width/2 - t.get_width()/2), 25))
    t = titleTxt.render("Σενάρια Ανησυχόμετρου", True, colors['lime'])
    screen.blit(t, (int(width/2 - t.get_width()/2), int(85 * height / 1080)))
    t = logoTxt.render("Οδηγίες παιχνιδιού", True, instructCol)
    btnInstruct = screen.blit(t, (width - t.get_width() - 25, height - 45))

    # Next Button
    btnNext = pg.draw.rect(screen, btnCol, pg.Rect(int(width/7 - 60), int(5*height/7 - 50), 120, 100))
    pg.draw.rect(screen, colors['btnPressed'], pg.Rect(btnNext.x, btnNext.y, btnNext.width, btnNext.height), 4)
    screen.blit(nxtBtnTxt.render("Επόμενη", True, colors['btnText']), (btnNext.x+10, btnNext.y+18))
    screen.blit(nxtBtnTxt.render("Κάρτα", True, colors['btnText']), (btnNext.x+23, btnNext.y+55))

    # Close Button
    btnClose = pg.draw.rect(screen, extBtnCol, pg.Rect(width-50, 25, 25, 25))
    screen.blit(extBtnTxt.render("X", True, colors['light-grey']), (width-46, 26))

    # Image
    screen.blit(mainImg, (int(width/2 - mainImg.get_width()/2), int(height-mainImg.get_height()-25)))
    screen.blit(meterImg, (int(14*width/15-meterImg.get_height()/2), int(height/2 - meterImg.get_height()/2)))

    # Card
    pg.draw.rect(screen, colors['cardBorder'], pg.Rect(int(width/2 - 250), int(height/4 - 80), 500, 300), 4)
    drawCardText(screen, cardContent, int(width/2 - 235), int(height/4 - 75))

    # Event handling
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos

            # Next Button
            if btnNext.collidepoint(event.pos):
                if len(cards) == 0: cards = cardsTemplate.copy()
                cardContent = cards.pop(randint(0, len(cards)-1))
            # Instructions Button
            if btnInstruct.collidepoint(event.pos):
                with open(os.path.join(srcDir, 'instructions.txt'), 'r', encoding='utf-8') as f:
                    pg.display.iconify()
                    InfoWindow("Οδηγίες Παιχνιδιού", f.read())
            if btnClose.collidepoint(event.pos):
                running = False

    # Refresh screen
    pg.display.update()

pg.quit()