import pygame
import buttons

if __name__=="__main__": 
    pygame.init()
    main_screen = pygame.display.set_mode((1000, 1000))
    main_screen.fill((41,218,206))
    #button_rec = pygame.Rect(500, 500, 100, 100)
    #button_sq = pygame.Surface([100, 100])
    #main_screen.blit(button_sq, button_rec)
    
    x = buttons.button(500, 500, 100, 100)
    x.draw(main_screen)

    while True: 
        ev = pygame.event.poll()
           
        if ev.type == pygame.MOUSEBUTTONDOWN:
            x, y = ev.pos
            if button_rec.collidepoint(x, y):
                print "miley cyrus"
        pygame.display.flip()
