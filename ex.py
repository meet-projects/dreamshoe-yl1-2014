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
    
    B1 = buttons.button(150, 100, 200, 200, 'rsz_converse-all-stars.jpg')
    B1.draw(main_screen)

    B2 = buttons.button(650,100,200,200, 'rsz_vans-shoes-era.jpg')
    B2.draw(main_screen)

    B3 = buttons.button(150, 400,200,200, 'rsz_adidas-f50-adizero.jpg')
    B3.draw(main_screen)

    B4 = buttons.button(650,400,200,200, 'rsz_lacoste10.jpg')
    B4.draw(main_screen)

    B5 = buttons.button(150,700,200,200, 'rsz_jordan-shoes.jpg')
    B5.draw(main_screen)

    B6 =buttons.button(650,700,200,200, 'rsz_img-thing.jpg')
    B6.draw(main_screen)

    label_rec = pygame.Rect(350, 25, 200, 30)

    orderlabel = pygame.font.Font(None, 50)

    label = orderlabel.render("CHOOSE A SHOE...", 1, (255, 0,0), (41, 218, 206))

    main_screen.blit(label, label_rec)

    while True: 
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT: 
            sys.exit()
        if ev.type == pygame.MOUSEBUTTONDOWN:
            x, y = ev.pos
            
            if B1.rec.collidepoint(x, y):
                print "I clicked B1"

            if B2.rec.collidepoint(x,y):
                print "I clicked B2!"

            if B3.rec.collidepoint(x,y):
                print "I clicked B3!"

            if B4.rec.collidepoint(x,y):
                print "I clicked B4!"

            if B5.rec.collidepoint(x,y):
                print "I clicked B5!"

            if B6.rec.collidepoint(x,y):
                print "I clicked B6!"


        pygame.display.flip()
