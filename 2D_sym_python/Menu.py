import pygame, sys , os
from pygame.locals import *
from Defines import *
from World import *
from Game import*
from animals.Human import*

pygame.init()
pygame.display.set_caption('game menu')
screen = pygame.display.set_mode((800, 500),0,32)

mainClock = pygame.time.Clock()
font_default = pygame.font.SysFont(None, 20)
game_folder = os.path.dirname(__file__)
texture_folder = os.path.join(game_folder, 'background')
sounds_folder = os.path.join(game_folder, 'photos')
font_style = os.path.join(game_folder, '04B_19.TTF')

bg_surface = pygame.image.load(os.path.join(texture_folder, "bc_menu.jpg")).convert()
bg_surface = pygame.transform.scale(bg_surface, (1000, 600))
bg_surface_blur = pygame.image.load(os.path.join(texture_folder, "bc_menu_blur.jpg")).convert()
bg_surface_blur = pygame.transform.scale(bg_surface_blur, (1000, 600))

rect_surf_size = pygame.Surface((200,50)) # the size of rect.
rect_surf_size.set_alpha(0)

game_size_cust = [0, 0]
click = False 

size_input_rects = [
    pygame.Rect(600, 150, 150, 40),  # get Vertical size
    pygame.Rect(600,250, 150, 40)  # get Horizontal size
]

world = World()
human = Human()
game = Game()

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def custom_world():
    running = True
    input_active = False
    input_box_choice = 0
    input_text = ""
    input_text_0box=""
    input_text_1box=""
    
    while running:
        screen.blit(bg_surface_blur,(0,-50))

        mx, my = pygame.mouse.get_pos()

        button_options_1 = pygame.Rect(600, 370, 100, 50)

        draw_text('ENTER WORLD SIZE', pygame.font.Font(font_style,50), (255, 255, 255), screen, 210, 20)
        draw_text('PRESS Esc to exit', pygame.font.Font(font_style,20), (255, 255, 255), screen, 330, 460)

        draw_text('VERTICAL SIZE', pygame.font.Font(font_style,40), (255, 255, 255), screen, 30,150)
        draw_text('HORIZONTAL SIZE', pygame.font.Font(font_style,40), (255, 255, 255), screen, 30,250)
            
        screen.blit(rect_surf_size, (50,105), button_options_1) # (0,0) are the top-left coordinates.
        draw_text('Press to start', pygame.font.Font(font_style,20), (75, 145, 63), screen, button_options_1.x + 10, button_options_1.y + 15)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    (mx, my) = pygame.mouse.get_pos()

                    if button_options_1.collidepoint((mx, my)):
                        print("pressed")
                        input_active = False
                    elif size_input_rects[0].collidepoint((mx, my)):
                        print("pressed")
                        input_active = True
                        input_box_choice = 0
                        input_text=""
                    elif size_input_rects[1].collidepoint((mx, my)):
                        print("pressed")
                        input_active = True
                        input_box_choice = 1
                        input_text=""
            
            elif event.type == pygame.KEYDOWN:
                if input_active:
                    if event.key == pygame.K_BACKSPACE:
                        input_text = input_text[:-1]
                    elif event.key == pygame.K_RETURN:
                        try:
                            if input_box_choice == 0:
                                game_size_cust[0] = int(input_text_0box)
                                print("Entered number:", game_size_cust[0])
                            elif input_box_choice == 1:
                                game_size_cust[1] = int(input_text_1box)
                                print("Entered number:", game_size_cust[1])
                        except ValueError:
                            print("Invalid input")
                    else:
                        input_text += event.unicode  

                    if input_box_choice==0:
                        input_text_0box=input_text
                    elif input_box_choice==1:
                        input_text_1box=input_text    

        pygame.draw.rect(screen, (255,255,255), size_input_rects[0],2)
        pygame.draw.rect(screen, (255,255,255), size_input_rects[1],2)

        # Render the input text on the window
        input_font = pygame.font.SysFont(None, 50)
        text_surface_0 = input_font.render(input_text_0box, True, (255,255,255))
        text_surface_1 = input_font.render(input_text_1box, True, (255,255,255))
        screen.blit(text_surface_0, (size_input_rects[0].x + 50, size_input_rects[0].y + 5))
        screen.blit(text_surface_1, (size_input_rects[1].x + 50, size_input_rects[1].y + 5))
        screen.blit(rect_surf_size, (650,105), button_options_1)

        if pygame.mouse.get_pressed()[0] and button_options_1.collidepoint((mx, my)):
            try:
                print("Entered number:", game_size_cust[0],",",game_size_cust[1])
                world.SetHorizSize(game_size_cust[0])
                world.SetVerticSize(game_size_cust[1])
                world.userWorld()
                game.addToWorld(world, human)
                game.playGame(world, human)
                return
            except ValueError:
                print("Invalid input")

        pygame.display.update()
        mainClock.tick(60)

def main_menu():
    while True:
        screen.fill((0, 0, 0))
        screen.blit(bg_surface,(0,-50))
        
        draw_text('World Symulator', pygame.font.Font(font_style,50), (255, 255, 255), screen, 220, 20)
 
        mx, my = pygame.mouse.get_pos()
 
        button_start = pygame.Rect(50, 100, 80, 50)
        button_custom = pygame.Rect(50, 200, 145, 50)
        button_load = pygame.Rect(50, 300, 245, 50)
        button_exit = pygame.Rect(50, 400, 75, 50)

        if button_start.collidepoint((mx, my)):
            button_color=[(75, 145, 63),(255,255,255),(255,255,255),(255,255,255)]
            
            if click:
                game.addToWorld(world, human)
                game.playGame(world, human)

        elif button_custom.collidepoint((mx, my)):
            button_color=[(255,255,255),(75, 145, 63),(255,255,255),(255,255,255)]

            if click:
                custom_world()

        elif button_load.collidepoint((mx,my)):
            button_color=[(255,255,255),(255,255,255),(75, 145, 63),(255,255,255)]
            
            if click:
                human_load = game.fromFile(world,human)
                game.playGame(world, human_load)

        elif button_exit.collidepoint((mx, my)):
            button_color=[(255,255,255),(255,255,255),(255,255,255),(75, 145, 63)]

            if click:
                pygame.quit()
                sys.exit()
        else:
            button_color=[(255,255,255),(255,255,255),(255,255,255),(255,255,255)]

        
        screen.blit(rect_surf_size, (50,105), button_start)
        draw_text('PLAY', pygame.font.Font(font_style,40), button_color[0], screen, 50, 105)
        screen.blit(rect_surf_size, (50,205), button_custom)
        draw_text('SELECT WORLD SIZE', pygame.font.Font(font_style,40), button_color[1], screen, 50, 205)
        screen.blit(rect_surf_size, (50,305), button_load)
        draw_text('LOAD SAVED WORLD', pygame.font.Font(font_style,40), button_color[2], screen, 50, 305)
        screen.blit(rect_surf_size, (50,405), button_exit)
        draw_text('EXIT', pygame.font.Font(font_style,40), button_color[3], screen, 50, 405)
        
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.flip()
        pygame.display.update()
        mainClock.tick(60)

main_menu()