from Defines import*
from World import*
import pygame, sys , os
from pygame.locals import *
import tkinter as tk
from tkinter import messagebox
import pickle

class Screen():
    def __init__(self):
        os.environ['SDL_VIDEO_CENTERED'] = '1' 
        self.screen = pygame.display.set_mode((1200, 700))

class Game():

    def __init__(self):
        self.data = {}
        self.file_name = ""
        pass
    
    def duringGame(self, world):
        world.drawWorld(self.screen)
    
    def addToWorld(self, world, choiceOrganism):
        position = world.randPosition()
        world.addOrganism(position, choiceOrganism, FIGHT_LIST, False)
    
    def playGame(self, world, human):
        self.screen = Screen()
        pygame.display.set_caption('world symulator')
        game_folder = os.path.dirname(__file__)
        texture_folder = os.path.join(game_folder, 'background')
        self.background = pygame.image.load(os.path.join(texture_folder, "bc_game.jpg")).convert()

        rect_surf_size = pygame.Surface((200,50)) # the size of your rect.
        rect_surf_size.set_alpha(0)

        button_next_round = pygame.Rect(720, 630, 150, 50)
        button_load_world = pygame.Rect(880, 630, 150, 50)
        button_save_world = pygame.Rect(1040, 630, 150, 50)

        self.screen.screen.blit(self.background,(0,-50))
        pygame.display.update()

        side = 0
        if_print = True
        buttonListTemp = [[None] * world.GetHorizSize() for _ in range(world.GetVerticSize())]

        while True:
            if if_print: 
                self.screen.screen.blit(self.background,(0,-50))
                pygame.draw.rect(self.screen.screen, (255,255,255), button_next_round)
                self.draw_text('Next round', pygame.font.Font(None,35), (0, 0, 0), self.screen.screen, button_next_round.x + 10, button_next_round.y + 15)
                pygame.draw.rect(self.screen.screen, (255,255,255), button_load_world)
                self.draw_text('Load world', pygame.font.Font(None,35), (0, 0, 0), self.screen.screen, button_load_world.x + 10, button_load_world.y + 15)
                pygame.draw.rect(self.screen.screen, (255,255,255), button_save_world)
                self.draw_text('Save world', pygame.font.Font(None,35), (0, 0, 0), self.screen.screen, button_save_world.x + 10, button_save_world.y + 15)
                self.duringGame(world)
                if_print = False

                for i in range(world.GetVerticSize()):
                    for j in range(world.GetHorizSize()):
                        buttonListTemp[i][j] = world.GetButtonData(i,j)

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == pygame.K_UP:
                        if human.GetOrganismLifespan() != False: 
                            human.setActionToDo('up',world)
                            if_print = True
                    elif event.key == pygame.K_DOWN:
                        if human.GetOrganismLifespan() != False: 
                            human.setActionToDo('down',world)
                            if_print = True
                    elif event.key == pygame.K_LEFT:
                        if human.GetOrganismLifespan() != False: 
                            human.setActionToDo('left',world)
                            if_print = True
                    elif event.key == pygame.K_RIGHT:
                        if human.GetOrganismLifespan() != False: 
                            human.setActionToDo('right',world)
                            if_print = True
                    elif event.key == pygame.K_p:
                        if human.GetOrganismLifespan() != False: 
                            human.setActionToDo('p',world)
                            if_print = True
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                elif event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        (mx, my) = pygame.mouse.get_pos()

                        if button_next_round.collidepoint((mx, my)):
                            if (human.GetOrganismLifespan() != False):
                                stayPos = human.GetOrganismPosition()
                                human.SetOrganismWantedPosition(stayPos['x'], stayPos['y'])
                            world.makeTurn()
                            if_print = True
                        elif button_save_world.collidepoint((mx, my)):
                            self.intoFile(world,human)
                            if_print = True
                        elif button_load_world.collidepoint((mx, my)):
                            human = self.fromFile(world,human)
                            buttonListTemp = [[None] * world.GetHorizSize() for _ in range(world.GetVerticSize())]
                            if_print = True
                        else:
                            for i, row in enumerate(buttonListTemp):
                                for j, button in enumerate(row):
                                    if (button.data).collidepoint((mx, my)):
                                        pos_ = button.pos
                                        print(str(pos_['x'])+ "_"+ str(pos_['y']))

                                        options = ['Antelope', 'Fox', 'Sheep', 'Turtle', 'Wolf', 'Belladonna', 'Grass', 'Guarana', 'Sosnowsky hogweed', 'Sow thistle', 'Cyber_sheep']
                                        option_window = OptionWindow(options)
                                        option_window.run()

                                        choice = option_window.GetSelectOpt()
                                        if choice!=0:
                                            if choice == "Antelope":
                                                org_= Antelope()
                                            elif choice == "Fox":
                                                org_= Fox()
                                            elif choice == "Sheep":
                                                org_= Sheep()
                                            elif choice == "Turtle":
                                                org_= Turtle()
                                            elif choice == "Wolf":
                                                org_= Wolf()
                                            elif choice == "Belladonna":
                                                org_= Belladonna()
                                            elif choice == "Grass":
                                                org_= Grass()
                                            elif choice == "Guarana":
                                                org_= Guarana()
                                            elif choice == "Sosnowsky hogweed":
                                                org_= Sosnowsky_hogweed()
                                            elif choice == "Sow thistle":
                                                org_= Sow_thistle()
                                            elif choice == "Cyber_sheep":
                                                org_ = Cyber_sheep()
                                            
                                            world.addOrganism(button.pos, org_, FIGHT_LIST, True)
                                            if choice == "Sosnowsky hogweed":
                                                world.AddHogweedList(org_)
                                            world.AddCommentatorVector(reportType.ORGANISM_ADDED, org_, None, 0)
                                            #world.drawWorld(self.screen)
                                            if_print = True
            pygame.display.update()

    
    def intoFile (self, world, human):
        self.windowToSaveLoad('s')
        temp_list_fight = []

        for i in range(world.GetFightVectorSize()):
            dataToSave=world.GetFightVectorData(i)
            temp_list_fight.append(dataToSave)
		
        self.data = {
            'horizontal_size': world.GetHorizSize(),
            'vertical_size': world.GetVerticSize(),
            'fightVectorSize': world.GetFightVectorSize(),
            'human': human,
            'fightList': temp_list_fight
        }

        f_name = self.file_name + ".pkl"
        with open(f_name, 'wb') as file:
            pickle.dump(self.data, file)
    
    def fromFile(self, world, human):
        self.windowToSaveLoad('l')
        f_name = self.file_name + ".pkl"

        with open(f_name, 'rb') as file:
            loaded_data = pickle.load(file)
        
        world.clearFightVect()
        world.clearNewOrgVect()
        world.clearHogweedList()

        world.SetHorizSize(loaded_data['horizontal_size'])
        world.SetVerticSize(loaded_data['vertical_size'])
        sizeFightList = loaded_data['fightVectorSize']
        human = loaded_data['human']
        temp_list_fight = loaded_data['fightList']

        for i in range(sizeFightList):
            world.AddFightVectorData(temp_list_fight[i])
        
        self.setFromFile(world, human)
        world.SetImgSizeChange()
        world.CommentatorSaveOpen(reportType.FILE_OPENED, self.file_name)

        return human
    
    def setFromFile(self, world, human):
        world.clearOrganismVect()
        world.organismsVectorResize()
        
        positionOrg_ = human.GetOrganismPosition()
        world.SetOrganismVectorData(human, positionOrg_['y'], positionOrg_['x'])
        
        for i in range(world.GetFightVectorSize()):
            positionOrg_ = world.GetFightVectorData(i).GetOrganismPosition()
            world.SetOrganismVectorData(world.GetFightVectorData(i), positionOrg_['y'], positionOrg_['x'])

            if world.GetFightVectorData(i).GetName() == 'h':
                world.AddHogweedList(world.GetFightVectorData(i))

    def get_name_file(self,entry, window, saveLoad):
        self.file_name = entry.get()
        if self.file_name:
            if saveLoad == 's':
                messagebox.showinfo('Save File', f'Saving file as: {self.file_name}')
            elif saveLoad =='l':
                messagebox.showinfo('Load File', f'Loading file: {self.file_name}')
            window.destroy()
        else:
            messagebox.showwarning('Error', 'Please enter a file name.')
    
    def windowToSaveLoad(self,saveLoad):
        window = tk.Tk()
        window.title('File Name Input')

        window_width = 300
        window_height = 100
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        window.geometry(f'{window_width}x{window_height}+{x}+{y}')

        window.configure(bg='#245c85')

        entry = tk.Entry(window)
        entry.configure(width=40)
        entry.pack(anchor='center')
        
        entry.bind("<Return>", lambda event: self.get_name_file(entry, window, saveLoad))

        button = tk.Button(window, text='Enter', command=self.get_name_file)
        button.pack()

        window.mainloop()


    def draw_text(self, text, font, color, surface, x, y):
        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)


class OptionWindow():
    def __init__(self, options):
        self.options = options
        self.selected_option = None

        self.window = tk.Tk()
        self.window.title('Choose an Option')
        self.window.geometry('300x350')

        self.create_widgets()

    def create_widgets(self):
        label = tk.Label(self.window, text='Select an option:')
        label.pack()

        for option in self.options:
            button = tk.Button(self.window, text=option, width=20, command=lambda opt=option: self.select_option(opt))
            button.pack()

    def select_option(self, option):
        self.selected_option = option
        self.window.destroy()

    def run(self):
        self.window.mainloop()
        
    def GetSelectOpt(self):
        return self.selected_option