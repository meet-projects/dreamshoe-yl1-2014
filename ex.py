import pygame
import buttons 
import sys

def drawcolors():
    B7.sq.fill((255,255,255))
    B7.draw(main_screen)
    B14.draw(main_screen)
    B15.draw(main_screen)
    B16.draw(main_screen)

    label_rec = pygame.Rect(350, 25, 200, 30)
    orderlabel = pygame.font.Font(None, 50)
    label = orderlabel.render("CHOOSE A COLOR...", 1, (255, 0, 0), (255, 255, 255))
    main_screen.blit(label, label_rec)
    screenname = "color"

    B21.draw(main_screen)
    label_rec = pygame.Rect (740,830,200,100)
    orderlabel = pygame.font.Font(None,50)
    label= orderlabel.render ("BACK", 1,(255,255,255))
    main_screen.blit(label, label_rec)

def firstpage():
    B7.sq.fill((41,218,206))
    B7.draw(main_screen)
    B1.draw(main_screen)
    B2.draw(main_screen)
    B3.draw(main_screen)
    B4.draw(main_screen)
    B5.draw(main_screen)
    B6.draw(main_screen)

    label_rec = pygame.Rect(350, 25, 200, 30)
    orderlabel = pygame.font.Font(None, 50)
    label = orderlabel.render("CHOOSE A SHOE...", 1, (255, 0, 0), (41, 218, 206))
    main_screen.blit(label, label_rec)

def drawcornershoe(filename):
    s=buttons.button(60,750,700,700, 0, 0, 0,  filename)
    s.draw(main_screen)




if __name__=="__main__": 
    pygame.init()
    main_screen = pygame.display.set_mode((1000, 1000))
    main_screen.fill((41,218,206))
    #button_rec = pygame.Rect(500, 500, 100, 100)
    # button_sq = pygame.Surface([100, 100])
    # main_screen.blit(button_sq, button_rec)
    screenname="shoe"

    B1 = buttons.button(150, 100, 200, 200,0, 0, 0,  'B1.jpg')
    B1.draw(main_screen)

    B2 = buttons.button(650,100,200,200,0, 0, 0, 'B2.jpg')
    B2.draw(main_screen)

    B3 = buttons.button(150, 400,200,200,0, 0, 0, 'B3.jpg')
    B3.draw(main_screen)

    B4 = buttons.button(650,400,200,200,0, 0, 0, 'B4.jpg')
    B4.draw(main_screen)

    B5 = buttons.button(150,700,200,200,0, 0, 0, 'B5.jpg')
    B5.draw(main_screen)

    B6 =buttons.button(650,700,200,200,0, 0, 0, 'B6.jpg')
    B6.draw(main_screen)

    B7=buttons.button(0,0,1000,1000, 255,255, 255)

    B8=buttons.button(60,750,700,700, 0, 0, 0,  'B1.jpg')

    B9=buttons.button(60,750,700,700, 0, 0, 0,  'B2.jpg')

    B10=buttons.button(60,750,700,700, 0, 0, 0,  'B3.jpg')

    B11=buttons.button(60,750,700,700, 0, 0, 0,  'B4.jpg')

    B12=buttons.button(60,750,700,700, 0, 0, 0,  'B5.jpg')

    B13=buttons.button(60,750,700,700, 0, 0, 0,  'B6.jpg')
    
    B14=buttons.button(130,150,100,100, 255,0, 162) #pink

    B15=buttons.button(300,150,100,100, 102,255, 255) #blue

    B16=buttons.button(430,150,100,100, 128,255, 0) #green

    # B17=buttons.button(60,750,700,700, 0, 0, 0,  'rsz_img-thing2.jpg')

    # B18= buttons.button(60,750,700,700, 0, 0, 0,  'rsz_converse-male-converse-all-star-down-hi-fabric-upper-in-green.jpg')

    # B19= buttons.button(60,750,700,700, 0, 0, 0,  'kimush.jpeg')

    # B20= buttons.button(60,750,700,700, 0, 0, 0,  'vans-shoes-era.jpg')

    B21=buttons.button(700,800,200,100,0,0,0)



   

    label_rec = pygame.Rect(350, 25, 200, 30)
    orderlabel = pygame.font.Font(None, 50)
    label = orderlabel.render("CHOOSE A SHOE...", 1, (255, 0, 0), (41, 218, 206))
    main_screen.blit(label, label_rec)

    
    shoeclick= ""

    while True: 
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT: 
            sys.exit()
        if ev.type == pygame.MOUSEBUTTONDOWN:
            x, y = ev.pos
            
            if B1.rec.collidepoint(x, y):
               drawcolors()
               B8.draw(main_screen)
               shoeclick="B1"
                
                
            if B2.rec.collidepoint(x,y):
               drawcolors()
               B9.draw(main_screen)
               shoeclick= "B2"
               

            if B3.rec.collidepoint(x,y):
               drawcolors()
               B10.draw(main_screen)
               shoeclick= "B3"
               
               
            if B4.rec.collidepoint(x,y):
               drawcolors()
               B11.draw(main_screen)
               shoeclick= "B4"


            if B5.rec.collidepoint(x,y):
               drawcolors()
               B12.draw(main_screen)
               shoeclick= "B5"
               
               
            if B6.rec.collidepoint(x,y):
               drawcolors()
               B13.draw(main_screen)
               shoeclick= "B6"

            if B21.rec.collidepoint(x,y):
                firstpage ()

            if B14.rec.collidepoint(x,y):
                drawcornershoe(shoeclick + "-pink.jpg")

            if B15.rec.collidepoint(x,y):
                drawcornershoe(shoeclick + "-blue.jpg")

            if B16.rec.collidepoint(x,y):
                drawcornershoe(shoeclick + "-green.jpg")
               
               

            

           












        pygame.display.flip()
 
