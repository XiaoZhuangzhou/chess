import os
import pygame
from pygame.locals import *
from algorithm import *
import Tools

SCREEN_WIDTH = 563
SCREEN_HEIGHT = 720
CHESS_SIZE = SCREEN_WIDTH/8
saber_start = []
saber_kind = 0
king_kind = 1
hash = [True for i in range(64)]
####


class Character(pygame.sprite.Sprite):
    def __init__(self,pos,kind):
        pygame.sprite.Sprite.__init__(self)
        file_name = kind and "king.png" or "saber.png"
        self.pos = pos
        self.image = pygame.image.load(os.path.join('gif', file_name))
        self.rect = self.image.get_rect()
        self.tools = Tools.tools()
        self.rect.center = self.tools.pos_to_posxy(self.pos, CHESS_SIZE)

    def update(self, new_pos):
        self.tools = Tools.tools()
        self.rect = self.rect.move(self.tools.pos_to_pos12xy(new_pos,self.pos, CHESS_SIZE))
        self.pos = new_pos


class Button(pygame.sprite.Sprite):
    def __init__(self,pos,kind):
        pygame.sprite.Sprite.__init__(self)
        file_name = kind and "start.png" or "next_step.png"
        self.image = pygame.image.load(os.path.join('gif', file_name))
        self.rect = self.image.get_rect()
        self.rect.center = pos

class Application:
    def __init__(self,win_size):
        # 初始化游戏
        pygame.init()
        pygame.display.set_caption('国王骑士演示程序')
        # 载入背景图
        self.__window = pygame.display.set_mode(win_size)
        self.__character_group = pygame.sprite.Group()
        self.__button_group = pygame.sprite.Group()
        self.button1 = self.__create_button([450, 620], 1)
        self.button2 = self.__create_button([450, 680], 0)
        self.__loop = True
        self.__clock = pygame.time.Clock()
        self.is_king = False
        self.index = 0
        self.Saber={}
        self.king_position = INF
        self.step=0
        self.king_not_arrived = True
        self.protect_saber = INF

    def __event_process(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.__loop = False
            if pygame.mouse.get_pressed()[0]:
                mouse_pos=pygame.mouse.get_pos()
                if 430<mouse_pos[0]<510 and 620<mouse_pos[1]<650:
                    print(saber_start)
                    (self.result_dict, min_move, encounter_Pos, final_Pos, self.protect_saber) = run(saber_start,self.king_position)
                    print(self.result_dict)
                if 430 < mouse_pos[0] < 510 and 660 < mouse_pos[1] < 690:
                    self.step+=1
                    for i in range(len(self.result_dict)):
                        if i==len(self.result_dict)-1:
                            try:
                                self.King.update(self.result_dict[i][self.step])
                            except:
                                pass
                        elif i==protect_saber:
                            if self.Saber[i].pos == encounter_Pos and self.king_not_arrived:
                                pass
                            else:
                                self.Saber[i].update(self.result_dict[i][self.step])
                        else:
                            try:
                                self.Saber[i].update(self.result_dict[i][self.step])
                            except:
                                pass
                if mouse_pos[1] < 570:
                    self.tools = Tools.tools()
                    q=self.tools.get_position(int(mouse_pos[1]/CHESS_SIZE),int(mouse_pos[0]/CHESS_SIZE))
                    if self.is_king:
                        try:
                            self.King.kill()
                        except:
                            pass
                        self.king_position = q
                        self.King=self.__create_character(self.king_position, king_kind)
                    else:
                        if hash[q]:
                            saber_start.append(q)
                            self.Saber[self.index] = self.__create_character(q, saber_kind)
                            self.index += 1
                            hash[q]=False

                if 170<mouse_pos[0]<270 and 640<mouse_pos[1]<680:
                    self.is_king = True
                if 270<mouse_pos[0]<370 and 640<mouse_pos[1]<680:
                    self.is_king = False

    def __logic_process(self):
        pass

    def __draw_process(self):
        background = pygame.image.load('gif/background.png')
        self.__window.blit(background, (0, 0))
        self.__character_group.draw(self.__window)
        self.__button_group.draw(self.__window)
        pygame.display.flip()

    def __create_character(self, position, kind):
        self.character = Character(position, kind)
        self.character.add(self.__character_group)
        return self.character

    def __create_button(self, position, kind):
        self.button = Button(position, kind)
        self.button.add(self.__button_group)
        return self.button

    def go(self):
        while self.__loop:
            self.__event_process()
            self.__logic_process()
            self.__draw_process()
            self.__clock.tick(30)
        if self.__loop:
            pygame.quit()

app = Application([SCREEN_WIDTH, SCREEN_HEIGHT])
app.go()
