import pygame
import numpy as np
import time
def  matrix(sizematrix,bomb): #day la ham dung de tao ma tran chua bomb, cac vi tri co gia tri lon hon 10 la bomb
    a = np.zeros((sizematrix,sizematrix),dtype=int) # tao 1 ma tran vuong voi kich co da cho
    for i in range(bomb): #ta bat dau xep bomb random vao ma tran
        v =np.random.randint(0, sizematrix, 2)  # ta random vi tri dat bomb
        while a[v[0], v[1]] == 10:   #se co truong hop bi trung vi tri, vi vay neu trung se random lai den khi nao het trung thi thoi
            v = np.random.randint(0, sizematrix, 2)
        else:
            a[v[0], v[1]] = 10
    for i in range(len(a)): # o moi vi tri co bomb tuc a[i,j]=10 thi cac o xung quanh se tang 1 don vi
        for j in range(len(a)):
            if a[i, j] >= 10:
                for h in range(i - 1, i + 2):
                    if (h < 0 or h> len(a)-1): #neu vong lap chay over size thi se bo qua buoc lap ay, neu khong se bi loi
                        continue
                    for g in range(j - 1, j + 2):
                        if (g < 0 or g>len(a)-1):
                            continue
                        if (h == i and g == j):
                            continue
                        a[h,g]+=1
    return a
def printtext(char,x,y,sizefont,colors): # tac dung ham nay la print text ra man hinh
    font = pygame.font.SysFont("arialblack",sizefont) #dinh dang kieu font
    text= font.render(char, True, colors) #ham nay se tao ra mot hinh chu nhat bang kich thuoc cua chu, trong hinh chu nhat do se in anh cua chu
    screen.blit(text, (x - (text.get_width()) / 2, y - (text.get_height()) / 2))#in hinh text do len screen voi vi tri input la goc trai tren cung cua hinh
    return text.get_width(),text.get_height() #return 2 thong so nay co gi can thi xai lai
def returncolor(x): #ham nay se tra ve mau RGB theo dung number cua o
    if x == 1:
        mau = (0, 0, 255)
    elif x == 2:
        mau = (0, 255, 0)
    elif x == 3:
        mau = (255, 0, 0)
    elif x == 4:
        mau = (255, 0, 255)
    elif x >= 5:
        mau = (0, 0, 0)
    elif (x == 0): # cai nay phai in cung mau voi nen
        mau = (125, 125, 125)
    else:
        mau = (153, 50, 191)
    return mau
def yard(x,y): # ham nay dung de tao cac o vuong to contain numbers and bombs
    return pygame.draw.rect(screen,(125,125,125),[x-long/2,y-long/2,long,long])  #in mot hinh chu nhat xac dinh boi goc tren cung ben trai va kich thuoc
def bomb(x,y): #ma tran nay de them hinh bomb
    b=pygame.image.load('bomb.jpg') #hinh bomb tai tu thu muc ben ngoai
    b=(pygame.transform.scale(b, (long, long))) #thay doi kich thuoc cua anh
    return (screen.blit(b, (x-long/2, y-long/2))) #in anh ra man hinh
def flag(x,y): # hinh nay de tao hinh anh la co
    b = pygame.image.load('flag.jpg') #tai tu thu muc ben ngoai
    b = pygame.transform.scale(b, (long, long)) #thay doi kich thuoc cua anh
    return (screen.blit(b, (x - long / 2, y - long / 2), )) #in anh ra man hinh
def background(): #in ma tran chua bomb va numbers
    p = 10-(long+5)/2+25
    for i in range(len(a)):
        k = 100-(long+5)/2+25
        p += (long+5)
        for j in range(len(a)):
            k += (long+5)
            yard(k, p)
            printtext(str(a[i, j]), k, p,int(long*(4/9)),returncolor(a[i, j]))
            if a[i, j] >= 10:
                bomb(k, p)
def recursion_for_empty_cell(i,j): # neu mo 1 o khong co so se mo tiep nhung o con lai
    for h in range(i - 1, i + 2):
            if h < 0 or h>(len(a)-1):
                continue
            for g in range (j - 1, j + 2):
                if (g < 0 or g> len(a)-1):
                    continue
                if a[h,g]!=0:
                    t[h,g]=0
                if (a[h,g]==0 and t[h,g]!=0):
                    t[h,g]=0
                    recursion_for_empty_cell(h, g)#neu o ben canh van la so 0 thi lam tiep tuc tai o do
def button(text,x,y,dai,rong,colorwhennormal,colorwhenbut,colortext,sizetext,ham=None):
    mouse1 = pygame.mouse.get_pos() #lay vi tri chuot
    click1 = pygame.mouse.get_pressed() #lay gia tri nut an chuot
    if x + dai > mouse1[0] > x and y + rong > mouse1[1] > y: # nam trong dien tich cua o
        pygame.draw.rect(screen, colorwhenbut, (x, y, dai, rong)) #o vuong doi mau
        if (click1[0] == 1 and ham != None): #an chuot trai
            pygame.time.delay(200) #delay 0.2 giay
            ham() #thuc hien ham do
        if click1[0]==1:
            return True
    else:
        pygame.draw.rect(screen, colorwhennormal, (x, y, dai, rong))
    printtext(text, x+(dai) / 2, y + (rong)/2, sizetext, colortext) #in chu tren button
def easy():
    pygame.time.delay(200)
    gameloop(5,145,5)
def normal():
    pygame.time.delay(200)
    gameloop(10,70,20)
def hard():
    pygame.time.delay(200)
    gameloop(15,45,45)
def location(): # don gian la lay vi tri cua chuot coi no tuong duong voi o nao trong ma tran bomb minh tao ra
    intdivision=(mouse[0]-125)//(long+5)
    remainder=(mouse[0]-125)%(long+5)
    i=None
    j=None
    if (intdivision>=0 and remainder <=long):
            j=intdivision
            intdivision = (mouse[1] - 35) // (long+5)
            remainder = (mouse[1] - 35) % (long+5)
            if (intdivision >=0 and remainder <= long):
                i=intdivision
                if i>sm-1 or j>sm-1 :
                    i=None
                    j=None
    return i,j
def grass(t): #in nhung nut an che nhung con so len man hinh
    i,j=location()
    if ( i!=None and j!=None):

        if click[0]==1: #click chuot trai
            t[i,j]=0
            if a[i,j]==0:
                recursion_for_empty_cell(i,j)
        elif click[2]==1 and t[i,j]!=0:#click chuot phai
            if t[i,j]==2:
                t[i,j]=1
                pygame.time.delay(200)
            else:
                t[i,j]=2
                pygame.time.delay(200)
    return t
def printgrass(t):
    p = 10-(long+5)/2+25
    for i in range(len(t)):
        k = 100-(long+5)/2+25
        p += (long+5)
        for j in range(len(t)):
            k += (long+5)
            if t[i,j]== int(1):
                pygame.draw.rect(screen, (0, 125, 125), [k - long / 2, p - long / 2, long, long])
            if t[i,j]==2: #an chuot phai nen in flag ra o do
                flag(k,p)
def gameover():
    lap = False
    while not lap:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
        for g in range(len(a)):
            for h in range(len(a)):
                if a[g,h]>=10: #thua cuoc thi mo het bomb ra
                    t[g,h]=0
        background()
        printgrass(t)
        printtext('GAME OVER',500,500,120,(255,0,0))
        f=button('play again', 2, 50, 120, 30, (0, 255, 255), (255, 255, 0), (0, 0, 0), 20)
        if f:
            gameloop(sm,long,mine)
        button('Main Menu', 380, 825, 300, 100, (0, 0, 255), (0, 255, 0), (0, 0, 0), 40, introduce)
        pygame.display.update()
        clock.tick(60) #60 khung hinh tren giay
def youwin(): # nhu tren
    lap=False
    while not lap:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
        background()
        printtext('YOU WIN',500,500,120,(255,0,0))

        f = button('play again', 2, 50, 120, 30, (0, 255, 255), (255, 255, 0), (0, 0, 0), 20)
        if f:
            gameloop(sm, long, mine)
        button('Main Menu', 380, 825, 300, 100, (0, 0, 255), (0, 255, 0), (0, 0, 0), 40, introduce)
        pygame.display.update()
def introduce(): # ham nay tao man hinh gioi thieu
    rad=0
    b=image('logo.png',500,500)
    khoa=image('logokhoa.png',400,400)
    m=0 # dong chu chay o duoi
    lap = False
    while not lap:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
        screen.fill((255, 255, 255)) #to mau nen
        printtext('GVHD: Th.s Nguyen Duy Khuong',500,740,50,(255,0,0))
        printtext('Bo mon: Ky thuat lap trinh CKT',500,800,30,(255,0,0))
        printtext('Truong Dai Hoc Bach Khoa-DHQG TP.HCM      Khoa Khoa Hoc Ung Dung                                             Ho Chi Minh University of Technology      Faculty of Applied Science ',2300-m,950,30,(220,75,249))
        screen.blit(image('logogame.png', 950, 200), (10, 450))
        screen.blit(rot_center(b,rad), (480,-30) )
        screen.blit(rot_center(khoa,rad),(40,3))
        button('Easy ', 70, 650, 160, 50, (246, 220, 87), (0, 230, 230), (0, 0, 0), 25, easy)
        button('Normal ',400, 650, 160, 50, (243, 162, 0), (0, 230, 230), (0, 0, 0), 25, normal)
        button('Hard ', 1000-70-160, 650, 160, 50, (252, 107, 45), (0, 230, 230), (0, 0, 0), 25, hard)
        button('About Us', 380, 825, 300, 100, (0, 0, 255), (0, 255, 0), (255, 255, 255), 40,aboutus)
        rad+=2
        m+=6 #moi lan lap thi m se them 6
        if m>=3800:
            m=0
        pygame.display.update()
        clock.tick(60)
def gameloop(smd,longd,mined): #day la ham tao ra  game
    global sm,long,mine,t,a,sweep,deltaT,score #global se du bien do thanh bien cuc bo, xai dc trong ca chuong trinh
    sm=smd
    long=longd
    mine=mined
    t = np.ones((sm, sm), dtype=int) # tao ma tran 0
    a = matrix(sm,mine)
    sweep = np.zeros((sm, sm), dtype=int)
    score=0
    T=time.process_time()
    print(a)
    # print(mined)
    # print('long =',long)
    # print('so bom la',np.count_nonzero(a>=10))
    done = False
    while not done: # bat dau vong lap game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
        deltaT=time.process_time()-T
        screen.fill((255, 255, 250))
        background()
        global mouse
        mouse = pygame.mouse.get_pos() # lay vi tri chuot
        # print('mouse=',mouse)
        global click
        click = pygame.mouse.get_pressed()# lay gia tri click
        # print(click)
        t = grass(t)
        printgrass(t)
        score = diem(score)
        printtext('score: ' + str(score), 850, 850, 30, (255, 0, 0))
        printtext('Bombs:  '+str(mine),200,850,30,(255,0,0))

        button('Main Menu',380,825,300,100,(0,0,255),(0,255,0),(0,0,0),40,introduce)
        e,r=location() # lat vi tri o vuong ma ta click tren man hinh
        if e!=None and r!=None:
            if (click[0]==1 and a[e,r]>=10): #click trung o co gia tri lon hon 10 tuc la bomb thi thua
                printtext('score: ' + str(score), 850, 850, 30, (255, 0, 0))
                gameover()
            if (np.count_nonzero(t>=1)==mine): # and np.count_nonzero(t==2)==0): #so o chua mo bang so bomb thi thang
                score += 1000
                pygame.draw.rect(screen, (255, 255, 255), [700 ,800, 300, 100])
                printtext('Score: ' + str(score), 850, 850, 30, (255, 0, 0))
                youwin()
        printtext('Time: ' + str(int(deltaT)) + 's', 850, 900, 30, (255, 0, 0))
        pygame.display.update()

def diem(score): # tinh diem
    for i in range(len(a)):
        for j in range(len(a)):
            if t[i,j]==0 and sweep[i,j]==0:
                  score+=a[i,j]*(int(12-(1/15)*deltaT))
                  sweep[i,j]=1 #sweep la ma tran de ta biet rang tai vi tri do ta da + vao score, se khong + lai o lan lap sau
    return score
def rot_center(image, angle):
    """rotate an image while keeping its center and size"""
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image
def image(hinh,weight,height):
    b = pygame.image.load(hinh)  # hinh bomb tai tu thu muc ben ngoai
    b = (pygame.transform.scale(b, (weight, height)))  # thay doi kich thuoc cua anh
    # screen.blit(b, (x,y))
    return b
def aboutus():
    lap = False
    run=-300
    while not lap:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
        screen.fill((255,192,203))
        screen.blit(image('logo1.png',250,250),(500,-80-run))
        screen.blit(image('logokhoa.png',240,240),(250,-70-run))
        printtext('Truong Dai Hoc Bach Khoa-DHQG TPHCM',500,200-run,40,(255,0,0))
        printtext('Khoa Khoa Hoc Ung Dung',500,250-run,40,(255,0,0))
        printtext('Nganh: Co Ky Thuat',500,300-run,40,(255,0,0))
        printtext('Danh sach nhom              MSSV ', 500, 400-run, 40, (0, 125, 255))
        printtext('Nguyen Nhu Buu Duc        1711078 ', 500, 500-run, 40, (0, 0, 255))
        printtext('Nguyen Minh Duc              1711075',500,600-run,40,(0,0,255))
        printtext('Nguyen Ho Duy Tan            1713071',500,700-run,40,(0,0,255))
        printtext('Tran Anh Hong                  1711454', 500, 800-run, 40, (0, 0, 255))
        printtext('Vu Duc Luong                    1712096', 500, 900-run, 40, (0, 0, 255))
        printtext('Nguon tham khao: www.pygame.org',500,950-run,20,(0,0,0))
        printtext('www.pythonprogramming.net',675,980-run,20,(0,0,0))
        button('Main Menu', 0, 900, 1000, 100, (0, 255, 255), (0, 255, 0), (0, 0, 0), 40, introduce)
        run+=10
        if run>=900:
            run=-1000
        pygame.display.update()
        clock.tick(60)
pygame.init()
screen = pygame.display.set_mode((1000, 1000)) #screen se la man hinh kich thuoc 1000x1000
pygame.display.set_caption('MINESWEEPER') #ten tieu de
clock =pygame.time.Clock()
pygame.display.set_icon(image('logokhoa.png',100,100))

introduce()








