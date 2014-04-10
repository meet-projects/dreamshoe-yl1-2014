import pygame
import buttons

if __name__=="__main__": 
    pygame.init()
    main_screen = pygame.display.set_mode((1000, 1000))
    main_screen.fill((41,218,206))
    #button_rec = pygame.Rect(500, 500, 100, 100)
    # button_sq = pygame.Surface([100, 100])
    # main_screen.blit(button_sq, button_rec)
    
    B1 = buttons.button(150, 100, 200, 200,0, 0, 0)
    B1.draw(main_screen)

    B2 = buttons.button(650,100,200,200, 0, 0, 0)
    B2.draw(main_screen)

    B3 = buttons.button(150, 400,200,200, 0, 0, 0)
    B3.draw(main_screen)

    B4 = buttons.button(650,400,200,200, 0, 0, 0)
    B4.draw(main_screen)

    B5 = buttons.button(150,700,200,200, 0, 0, 0)
    B5.draw(main_screen)

    B6 =buttons.button(650,700,200,200, 0, 0, 0)
    B6.draw(main_screen)

    B7=buttons.button(0,0,1000,1000, 255,255, 255)



    


    while True: 
        ev = pygame.event.poll()
           
        if ev.type == pygame.MOUSEBUTTONDOWN:
            x, y = ev.pos
            
            if B1.rec.collidepoint(x, y):
               B7.draw(main_screen)
               B1.draw(main_screen)
                
                
            if B2.rec.collidepoint(x,y):
               B7.draw(main_screen)
               B2.draw(main_screen)

            if B3.rec.collidepoint(x,y):
               B7.draw(main_screen)
               B3.draw(main_screen)

            if B4.rec.collidepoint(x,y):
               B7.draw(main_screen)
               B4.draw(main_screen)

            if B5.rec.collidepoint(x,y):
               B7.draw(main_screen)
               B5.draw(main_screen)

            if B6.rec.collidepoint(x,y):
               B7.draw(main_screen)
               B6.draw(main_screen)


        pygame.display.flip()
 