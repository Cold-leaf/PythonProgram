import pygame,sys,time,random
from pygame.locals import *

#pygame初认识
'''
pygame.init()

windowSurface=pygame.display.set_mode((500,400),0,32)
pygame.display.set_caption('Your mom Boom!')

BLACK=(0,0,0)
WHITE=(255,255,255)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)

basicFont=pygame.font.SysFont(None,50)

text=basicFont.render('Your mom Boom!',True,WHITE,BLUE)
textRect=text.get_rect()
textRect.centerx=windowSurface.get_rect().centerx
textRect.centery=windowSurface.get_rect().centery

windowSurface.fill(WHITE)

pygame.draw.polygon(windowSurface,GREEN,((146,0),(291,106),(236,277),(56,277),(0,106)))

pygame.draw.line(windowSurface,BLUE,(60,60),(120,60),4)
pygame.draw.line(windowSurface,BLUE,(120,60),(60,120),3)
pygame.draw.line(windowSurface,BLUE,(60,120),(120,120),4)

pygame.draw.circle(windowSurface,BLUE,(300,50),20,0)

pygame.draw.ellipse(windowSurface, RED, (300, 250, 40, 80), 0)

pygame.draw.rect(windowSurface, RED, (textRect.left - 20, textRect.top - 20, textRect.width + 40, textRect.height + 40))

pixArray = pygame.PixelArray(windowSurface)

pixArray[480][380] = BLACK

del pixArray

windowSurface.blit(text, textRect)

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
'''

#pygame动图
'''
pygame.init()		

WINDOWWIDTH = 400
WINDOWHEIGHT =	400

windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Animation')

DOWNLEFT='downleft'
DOWNRIGHT = 'downright'
UPLEFT  ='upleft'
UPRIGHT = 'upright'
	
MOVESPEED = 4

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

b1 = {'rect':pygame.Rect(300, 80, 50, 100), 'color':RED, 'dir':UPRIGHT}
b2 = {'rect':pygame.Rect(200, 200, 20, 20), 'color':GREEN, 'dir':UPLEFT}
b3 = {'rect':pygame.Rect(100, 150, 60, 60), 'color':BLUE, 'dir':DOWNLEFT}
boxes = [b1, b2, b3]

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    windowSurface.fill(WHITE)

    for b in boxes:
        if b['dir'] == DOWNLEFT:
            b['rect'].left -= MOVESPEED
            b['rect'].top += MOVESPEED
        if b['dir'] == DOWNRIGHT:
            b['rect'].left += MOVESPEED
            b['rect'].top += MOVESPEED
        if b['dir'] == UPLEFT:
            b['rect'].left -= MOVESPEED
            b['rect'].top -= MOVESPEED
        if b['dir'] == UPRIGHT:
            b['rect'].left += MOVESPEED
            b['rect'].top -= MOVESPEED

        if b['rect'].top < 0:
            if b['dir'] == UPLEFT:
                b['dir'] = DOWNLEFT
            if b['dir'] == UPRIGHT:
                b['dir'] = DOWNRIGHT
        if b['rect'].bottom > WINDOWHEIGHT:
            if b['dir'] == DOWNLEFT:
                b['dir'] = UPLEFT
            if b['dir'] == DOWNRIGHT:
                b['dir'] = UPRIGHT
            if b['rect'].left < 0:
                if b['dir'] == DOWNLEFT:
                    b['dir'] = DOWNRIGHT
                if b['dir'] == UPLEFT:
                    b['dir'] = UPRIGHT
            if b['rect'].right > WINDOWWIDTH:
                if b['dir'] == DOWNRIGHT:
                    b['dir'] = DOWNLEFT

                if b['dir'] == UPRIGHT:
                    b['dir'] = UPLEFT
            pygame.draw.rect(windowSurface,b['color'], b['rect'])
    pygame.display.update()

    time.sleep(0.02)
'''

#贪吃块
'''
pygame.init()
mainClock=pygame.time.Clock()

WINDOWWIDTH=600
WINDOWHEIGHT=600
windowSurface=pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT),0,32)
pygame.display.set_caption('Collision Detection')

BLACK=(0,0,0)
GREEN=(0,255,0)
WHITE=(255,255,255)

foodCounter=0
NEWFOOD=40
FOODSIZE=20

def drawText(text,font,surface,x,y):
    textobj=font.render(text,1,BLACK)
    textrect=textobj.get_rect()
    textrect.topleft=(x,y)
    surface.blit(textobj,textrect)

font=pygame.font.SysFont(None,48)
player=pygame.Rect(300,100,40,40)
playerImage=pygame.image.load("testpic.jpg")
playerStretchedImage=pygame.transform.scale(playerImage,(40,40))
foodImage=pygame.image.load("testpic2.jpg")
foodStretchedImage=pygame.transform.scale(foodImage,(FOODSIZE,FOODSIZE))
foods=[]
for i in range(20):
    foods.append(pygame.Rect(random.randint(0,WINDOWWIDTH-FOODSIZE),random.randint(0,WINDOWHEIGHT-FOODSIZE),FOODSIZE,FOODSIZE))

moveLeft=False
moveRight=False
moveUp=False
moveDown=False

MOVESPEED=6
score=0

while True:
    drawText('Score:%s'%(score),font,windowSurface,101,101)
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        if event.type==KEYDOWN:
            if event.key==K_LEFT or event.key==K_a:
                moveRight=False
                moveLeft=True
            if event.key==K_RIGHT or event.key==K_d:
                moveRight=True
                moveLeft=False
            if event.key==K_UP or event.key==K_w:
                moveDown=False
                moveUp=True
            if event.key==K_DOWN or event.key==K_s:
                moveUp=False
                moveDown=True 
        if event.type==KEYUP:
            if event.key==K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key==K_LEFT or event.key==K_a:       
                moveLeft=False
            if event.key==K_RIGHT or event.key==K_d:
                moveRight=False
            if event.key==K_UP or event.key==K_w:
                moveUp=False
            if event.key==K_DOWN or event.key==K_s:
                moveDown=False 
            if event.key==K_x:
                player.top=random.randint(0,WINDOWHEIGHT-player.height)
                player.left=random.randint(0,WINDOWWIDTH-player.width)
        if event.type==MOUSEBUTTONUP:
            foods.append(pygame.Rect(event.pos[0],event.pos[1],FOODSIZE,FOODSIZE))

    foodCounter+=1
    if foodCounter>=NEWFOOD:
        foodCounter=0
        foods.append(pygame.Rect(random.randint(0,WINDOWWIDTH-FOODSIZE),random.randint(0,WINDOWHEIGHT-FOODSIZE),FOODSIZE,FOODSIZE))
    windowSurface.fill(WHITE)

    if moveDown and player.bottom<WINDOWHEIGHT:
        player.top+=MOVESPEED
    if moveUp and player.top>0:
        player.top-=MOVESPEED
    if moveLeft and player.left>0:
        player.left-=MOVESPEED
    if moveRight and player.right<WINDOWWIDTH:
        player.right+=MOVESPEED

    #pygame.draw.rect(windowSurface,BLACK,player)
    windowSurface.blit(playerStretchedImage,player)

    for food in foods[:]:
        if player.colliderect(food):
            foods.remove(food)
            score+=1
            player=pygame.Rect(player.left,player.top,player.width+2,player.height+2)
            playerStretchedImage=pygame.transform.scale(playerImage,(player.width,player.height))
    for food in foods:
        windowSurface.blit(foodStretchedImage,food)

    pygame.display.update()
    mainClock.tick(40)
'''

#贪吃蛇
'''
import pygame,sys,random
from pygame.locals import *

pygame.init()

Clock=pygame.time.Clock()       #用一个时钟来同步程序           

#各种可能用到的颜色
Blue=pygame.Color(0,0,255)
White=pygame.Color(255,255,255)
Black=pygame.Color(0,0,0)
Green=pygame.Color(0,255,0)
Yellow=pygame.Color(255,155,0)

#窗口设置
surface=pygame.display.set_mode((600,400),0,32)      #大小
pygame.display.set_caption("贪吃蛇")       #标题

#蛇的参数
Speed=20
head_size=20
snack_head=[100,100]        
snack=[pygame.Rect(snack_head[0],snack_head[1],head_size,head_size)]
snack.append(pygame.Rect(snack_head[0]+Speed,snack_head[1],head_size,head_size))
snack.append(pygame.Rect(snack_head[0]+Speed*2,snack_head[1],head_size,head_size))      #由于移动方法的设置，列表最后一个为实际蛇头

#设置5个布尔值来控制蛇的移动
moveR=False
moveL=False
moveU=False
moveD=False
movefast=False

#另设4个布尔值记录上一次的移动，来防止运动的直接反向而导致的头与身体的碰撞
moveRp=True         #初始蛇头朝右
moveLp=False
moveUp=False
moveDp=False


#设置有可以使蛇增加一块大小的food和增加两块大小的cookie

cookie_exist=False      #cookie一次只有一个，需要有变量来表明是否已经存在
cookieSize=20
cookie=pygame.Rect(random.randint(0,600-cookieSize),random.randint(0,400-cookieSize),cookieSize,cookieSize)

Add_Counter=0
New_food=40         #用Add_Counter来表示程序迭代次数，次数达到New_food后即增加一个food
foodSize=10
foods=[]
for i in range(20):         #初始时屏幕上有20个food     
    foods.append(pygame.Rect(random.randint(0,600-foodSize),random.randint(0,400-foodSize),foodSize,foodSize))


score=0
font=pygame.font.SysFont(None,48)
score_surface=font.render('Score={}'.format(score),True,White)


#游戏循环体    
while True:
    
    
    

    surface.fill(Black)         #屏幕背景填充

    surface.blit(score_surface,(0,0))

    #打印蛇的身体
    for i in range(len(snack)):
        if i<len(snack)-1:
            pygame.draw.rect(surface,White,snack[i])
        else:
            pygame.draw.rect(surface,Blue,snack[i])         #蛇头为列表最后一个，用蓝色标记

    Add_Counter+=1          #迭代一次即加一
    if Add_Counter>New_food:        #达到一定次数后增加一个food
        Add_Counter=0
        foods.append(pygame.Rect(random.randint(0,600-foodSize),random.randint(0,400-foodSize),foodSize,foodSize))
    
    for i in range(len(foods)):         #画出当前所有food
        pygame.draw.rect(surface,Green,foods[i])


    pygame.draw.rect(surface,Yellow,cookie)     #画出cookie

    if not cookie_exist:        #被吃掉后，cookie_exist为false，重置cookie的位置，并置cookie_exist为true
        cookie.left=random.randint(0,600-foodSize)
        cookie.top=random.randint(0,400-foodSize)
        cookie_exist=True
   
    #用pygame.event.get()接受键盘和鼠标的输入
    for event in pygame.event.get():
        if event.type==pygame.QUIT:         #关闭窗口时退出
            sys.exit()
        #按下按键时
        elif event.type==pygame.KEYDOWN:
            if event.key==27:       #按下esc键则退出
                sys.exit()
            elif event.key==K_a:        #按下a键则左移为true，右移为false
                moveL=True
                moveR=False
            elif event.key==K_d:        #按下d键则右移为true，左移为false
                moveR=True
                moveL=False
            elif event.key==K_w:        #按下w键则上移为true，下移为false
                moveU=True
                moveD=False
            elif event.key==K_s:        #按下s键则下移为true，上移为false
                moveD=True
                moveU=False
            elif event.key==K_SPACE:        #按下空格则加速为true
                movefast=True
        #释放按键时
        elif event.type==KEYUP:
            if event.key==K_a:          #释放a键 左移false
                moveL=False
                moveLp=True
                moveRp=False
                moveUp=False
                moveDp=False
            elif event.key==K_d:          #释放d键 右移false
                moveR=False
                moveRp=True
                moveLp=False
                moveUp=False
                moveDp=False
            elif event.key==K_w:          #释放w键 上移false
                moveU=False
                moveUp=True
                moveRp=False
                moveLp=False
                moveDp=False
            elif event.key==K_s:          #释放s键 下移false
                moveD=False
                moveDp=True
                moveRp=False
                moveLp=False
                moveUp=False
            elif event.key==K_SPACE:          #释放空格 加速false
                movefast=False

    #移动 向哪个方向移动则在相应方向前添加一块新的作为蛇头，同时删掉一块蛇尾
    if moveU or moveD or moveL or moveR:
        
        if moveU and not moveDp:
            if movefast:    #加速时添二删二
                snack.append(pygame.Rect(snack[-1].left,snack[-1].top-Speed,head_size,head_size))
                snack.append(pygame.Rect(snack[-1].left,snack[-1].top-Speed,head_size,head_size))
                snack.remove(snack[0])
                snack.remove(snack[0])
            else:
                snack.append(pygame.Rect(snack[-1].left,snack[-1].top-Speed,head_size,head_size))
                snack.remove(snack[0])

        elif moveD and not moveUp:
            if movefast:
                snack.append(pygame.Rect(snack[-1].left,snack[-1].top+Speed,head_size,head_size))
                snack.append(pygame.Rect(snack[-1].left,snack[-1].top+Speed,head_size,head_size))
                snack.remove(snack[0])
                snack.remove(snack[0])
            else:
                snack.append(pygame.Rect(snack[-1].left,snack[-1].top+Speed,head_size,head_size))
                snack.remove(snack[0])
        elif moveL and not moveRp:
            if movefast:
                snack.append(pygame.Rect(snack[-1].left-Speed,snack[-1].top,head_size,head_size))
                snack.append(pygame.Rect(snack[-1].left-Speed,snack[-1].top,head_size,head_size))
                snack.remove(snack[0])
                snack.remove(snack[0])
            else:
                snack.append(pygame.Rect(snack[-1].left-Speed,snack[-1].top,head_size,head_size))             
        elif moveR and not moveLp:
            if movefast:
                snack.append(pygame.Rect(snack[-1].left+Speed,snack[-1].top,head_size,head_size))
                snack.append(pygame.Rect(snack[-1].left+Speed,snack[-1].top,head_size,head_size))
                snack.remove(snack[0])
                snack.remove(snack[0])
            else:
                snack.append(pygame.Rect(snack[-1].left+Speed,snack[-1].top,head_size,head_size))            
                snack.remove(snack[0])

    #当蛇头达到边界时进行反转
    if snack[-1].left<0 :
        snack[-1].right=600
    elif snack[-1].right>600:
        snack[-1].left=0
    elif snack[-1].top<0 :
        snack[-1].bottom=400-snack[-1].top
    elif snack[-1].bottom>400:
        snack[-1].top=0

    #吃到food时
    for food in foods[:]:
        for i in range(len(snack)):
            if snack[i].colliderect(food):      #碰撞监测
                foods.remove(food)                
                snack.insert(0,pygame.Rect(snack[0].left,snack[0].top,head_size,head_size))     #吃到后在蛇尾处添加一块
                break
    #吃到cookie
    for i in range(len(snack)):
        if snack[i].colliderect(cookie):        #碰撞监测
            cookie_exist=False          #已不存在，应当产生新的cookie
            snack.insert(0,pygame.Rect(snack[0].left,snack[0].top,head_size,head_size))
            snack.insert(0,pygame.Rect(snack[0].left,snack[0].top,head_size,head_size))     #吃到添加两块
            break

    #监测蛇头是否撞到身体
    for body in snack[0:-1]:
        if snack[-1].colliderect(body):
            sys.exit()
    
    pygame.display.update()     
    Clock.tick(12)
'''

#文本显示测试
'''
import pygame
from pygame.locals import *
from sys import exit
 
background_image_file="testpic.jpg"
 
pygame.init()
screen=pygame.display.set_mode((500,500),0,32)
 
score=1
font=pygame.font.SysFont(None,40)
name_surface=font.render('score={}'.format(score),True,(231,32,111))
 
x=name_surface.get_width()
y=40

while True:
    for event in pygame.event.get():
        if event==QUIT:
            exit()
 
 
    screen.blit(name_surface,(0,0))
    
    
    pygame.display.update()
    '''

#按钮测试
pygame.init()
screen = pygame.display.set_mode((300,200),0,32)
upImageFilename = 'testpic.jpg'
downImageFilename = 'testpic2.jpg'

class Button(object):
    def __init__(self, upimage, downimage,position):
        self.imageUp = pygame.image.load(upimage).convert_alpha()
        self.imageDown = pygame.image.load(downimage).convert_alpha()
        self.position = position

    def isOver(self):
        point_x,point_y = pygame.mouse.get_pos()
        x, y = self. position
        w, h = self.imageUp.get_size()

        in_x = x - w/2 < point_x < x + w/2
        in_y = y - h/2 < point_y < y + h/2
        return in_x and in_y

    def render(self):
        w, h = self.imageUp.get_size()
        x, y = self.position
        
        if self.isOver():
            screen.blit(self.imageDown, (x-w/2,y-h/2))
        else:
            screen.blit(self.imageUp, (x-w/2, y-h/2))

button = Button(upImageFilename,downImageFilename, (150,100))
    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.fill((200, 200, 200))
    button.render()
    pygame.display.update()

