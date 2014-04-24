import pygame
import buttons 
import sys

if __name__=="__main__": 
    pygame.init()
    main_screen = pygame.display.set_mode((1000, 1000))
    main_screen.fill((41,218,206))
    #button_rec = pygame.Rect(500, 500, 100, 100)
    # button_sq = pygame.Surface([100, 100])
    # main_screen.blit(button_sq, button_rec)
    

    B1 = buttons.button(150, 100, 200, 200,0, 0, 0,  'rsz_converse-all-stars.jpg')
    B1.draw(main_screen)

    B2 = buttons.button(650,100,200,200,0, 0, 0, 'rsz_vans-shoes-era.jpg')
    B2.draw(main_screen)

    B3 = buttons.button(150, 400,200,200,0, 0, 0, 'rsz_adidas-f50-adizero.jpg')
    B3.draw(main_screen)

    B4 = buttons.button(650,400,200,200,0, 0, 0, 'rsz_lacoste10.jpg')
    B4.draw(main_screen)

    B5 = buttons.button(150,700,200,200,0, 0, 0, 'rsz_jordan-shoes.jpg')
    B5.draw(main_screen)

    B6 =buttons.button(650,700,200,200,0, 0, 0, 'rsz_img-thing.jpg')
    B6.draw(main_screen)

    B7=buttons.button(0,0,1000,1000, 255,255, 255)

    B8=buttons.button(60,750,700,700, 0, 0, 0,  'rsz_converse-all-stars.jpg')

    B9=buttons.button(60,750,700,700, 0, 0, 0,  'rsz_vans-shoes-era.jpg')

    B10=buttons.button(60,750,700,700, 0, 0, 0,  'rsz_adidas-f50-adizero.jpg')

    B11=buttons.button(60,750,700,700, 0, 0, 0,  'rsz_lacoste10.jpg')

    B12=buttons.button(60,750,700,700, 0, 0, 0,  'rsz_jordan-shoes.jpg')

    B13=buttons.button(60,750,700,700, 0, 0, 0,  'rsz_img-thing.jpg')
    
    B14=buttons.button(130,150,100,100, 255,0, 162) #pink

    B15=buttons.button(300,150,100,100, 102,255, 255) #blue

    B16=buttons.button(430,150,100,100, 128,255, 0) #green

    BB14=buttons.button(130,150,100,100, 255,0, 162) #pink

    BB15=buttons.button(300,150,100,100, 102,255, 255) #blue

    BB16=buttons.button(430,150,100,100, 128,255, 0) #green

    BBB14=buttons.button(130,150,100,100, 255,0, 162) #pink

    BBB15=buttons.button(300,150,100,100, 102,255, 255) #blue

    BBB16=buttons.button(430,150,100,100, 128,255, 0) #green

    BBBB14=buttons.button(130,150,100,100, 255,0, 162) #pink

    BBBB15=buttons.button(300,150,100,100, 102,255, 255) #blue

    BBBB16=buttons.button(430,150,100,100, 128,255, 0) #green

    BBBBB14=buttons.button(130,150,100,100, 255,0, 162) #pink

    BBBBB15=buttons.button(300,150,100,100, 102,255, 255) #blue

    BBBBB16=buttons.button(430,150,100,100, 128,255, 0) #green

    BBBB14=buttons.button(130,150,100,100, 255,0, 162) #pink

    BBBBB15=buttons.button(300,150,100,100, 102,255, 255) #blue

    BBBBBB16=buttons.button(430,150,100,100, 128,255, 0) #green

    B17=buttons.button(60,750,700,700, 0, 0, 0,  'rsz_img-thing2.jpg')

    B18= buttons.button(60,750,700,700, 0, 0, 0,  'rsz_converse-male-converse-all-star-down-hi-fabric-upper-in-green.jpg')

    B19= buttons.button(60,750,700,700, 0, 0, 0,  'kimush.jpeg')

    B20= buttons.button(60,750,700,700, 0, 0, 0,  'vans-shoes-era.jpg')



   

    label_rec = pygame.Rect(350, 25, 200, 30)
    orderlabel = pygame.font.Font(None, 50)
    label = orderlabel.render("CHOOSE A SHOE...", 1, (255, 0, 0), (41, 218, 206))
    main_screen.blit(label, label_rec)

    label_rec = pygame.Rect(350, 25, 200, 30)
    orderlabel = pygame.font.Font(None, 50)
    label = orderlabel.render("CHOOSE A COLOR...", 1, (255, 0, 0), (255, 255, 255))
    

    while True: 
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT: 
            sys.exit()
        if ev.type == pygame.MOUSEBUTTONDOWN:
            x, y = ev.pos
            
            if B1.rec.collidepoint(x, y):
               B7.draw(main_screen)
               B8.draw(main_screen)
               B14.draw(main_screen)
               B15.draw(main_screen)
               B16.draw(main_screen)
               main_screen.blit(label, label_rec)
                
                
            if B2.rec.collidepoint(x,y):
               B7.draw(main_screen)
               B9.draw(main_screen)
               BB14.draw(main_screen)
               BB15.draw(main_screen)
               BB16.draw(main_screen)
               main_screen.blit(label, label_rec)

            if B3.rec.collidepoint(x,y):
               B7.draw(main_screen)
               B10.draw(main_screen)
               BBB14.draw(main_screen)
               BBB15.draw(main_screen)
               BBB16.draw(main_screen)
               main_screen.blit(label, label_rec)

            if B4.rec.collidepoint(x,y):
               B7.draw(main_screen)
               B11.draw(main_screen)
               BBBB14.draw(main_screen)
               BBBB15.draw(main_screen)
               BBBB16.draw(main_screen)
               main_screen.blit(label, label_rec)

            if B5.rec.collidepoint(x,y):
               B7.draw(main_screen)
               B12.draw(main_screen)
               BBBBB14.draw(main_screen)
               BBBBB15.draw(main_screen)
               BBBBB16.draw(main_screen)
               main_screen.blit(label, label_rec)

            if B6.rec.collidepoint(x,y):
               B7.draw(main_screen)
               B13.draw(main_screen)
               BBBBBB14.draw(main_screen)
               BBBBBB15.draw(main_screen)
               BBBBBB16.draw(main_screen)
               main_screen.blit(label, label_rec)

            if B15.rec.collidepoint(x,y):
               B7.draw(main_screen)
               B17.draw(main_screen)
               main_screen.blit(label, label_rec)

            if BB15.rec.collidepoint(x,y):
               B7.draw(main_screen)
               B20.draw(main_screen)
               main_screen.blit(label, label_rec)

            if BBB15.rec.collidepoint(x,y):
               B7.draw(main_screen)
               B17.draw(main_screen)
               main_screen.blit(label, label_rec)

            if BBBB15.rec.collidepoint(x,y):
               B7.draw(main_screen)
               B17.draw(main_screen)
               main_screen.blit(label, label_rec)

            if BBBBB15.rec.collidepoint(x,y):
               B7.draw(main_screen)
               B17.draw(main_screen)
               main_screen.blit(label, label_rec)

            if B16.rec.collidepoint(x,y):
               B7.draw(main_screen)
               B18.draw(main_screen)
               main_screen.blit(label, label_rec)

            if B14.rec.collidepoint(x,y):
               B7.draw(main_screen)
               B19.draw(main_screen)
               main_screen.blit(label, label_rec)

           












        pygame.display.flip()
 
