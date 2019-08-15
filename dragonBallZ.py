# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 09:43:23 2019
@file: dragonBallZ.py
@description: joc d'obtenir els objectes que surtin del cel
@author: Gilbert Viader
"""
import pygame, random, time
from datetime import datetime
"""
importar els mòdules de pygame, random, time
"""
from pygame.locals import *
"""
importar els mètodes del mòdul pygame.locals  
"""
dt = datetime.now()
random.seed(dt.second*43)

def final_partida(pantalla, quan) :
    tipografia = pygame.font.Font(None, 62)
    score_text = tipografia.render("Life: {} Level: {} Score: {}" .format(live, level, score), 1, red)
    final = tipografia.render("You lose, {} ms !!!".format(quan), 1, red)
    pantalla.blit(background, (0,0))
    pantalla.blit(collector, (drago_x, drago_y))
    pantalla.blit(fn_ball, (falling_x, falling_y))
    pantalla.blit(score_text, (100, 1))    
    pantalla.blit(final, (150, 300))
    pygame.display.flip()
    time.sleep(5)
    return True  
#------------------------------- definició de la funció final_partida   
def bucle_moment(collector_speed, tret_speed, kame_y) :  
    done = False
    for moment in pygame.event.get() :
        if moment.type == pygame.QUIT :
            done = True
        elif moment.type == pygame.KEYDOWN :
            if moment.key == pygame.K_RIGHT :
                collector_speed = 10
            if moment.key == pygame.K_LEFT :
                collector_speed = -10
            if moment.key == pygame.K_SPACE :
                tret_speed = -30                 
            if moment.key == pygame.K_ESCAPE:                
                done = True                           
        elif moment.type == pygame.KEYUP :
            if moment.key == pygame.K_RIGHT or moment.key == pygame.K_LEFT :
                collector_speed = 0
            if moment.key == pygame.K_SPACE :
                tret_speed = 0
                kame_y = 300
    return  kame_y, done, collector_speed, tret_speed
#----------------------------------------------------------------------------
#----------------------------- procés inicial -------------------------------
#----------------------------------------------------------------------------
pygame.init()

red = (242,111,111)
width = 600
height = 500
collector_speed, tret_speed = 0, 0
falling_speed = 2

#---------------- integer per el nostre marcador    
score = 0
live = 3
level = 0
#---------------- dimensions de la finestre   
screen = pygame.display.set_mode((width,height), 0, 32)
#---------------- càrrega del temps invertit
clock = pygame.time.Clock()
pygame.time.set_timer(USEREVENT + 1, 1000)
#---------------- recull de fonts tipogràfiques
tipografia = pygame.font.Font(None, 62)
carpeta = ".\\dragon\\"
#------------------ fitxers del fons de pantalla    
fn_pantalla1 = "pantalla1.jpg"   # Fons Level-1 y Level-2
fn_pantalla2 = "pantalla5.jpg"        # Fons Level-3
fn_pantalla3 = "pantalla3.jpg"            # Fons Level-4
fn_dragonball = "pantalla7.jpg"
#------------------ fitxers dels objectes mòbils   
fn_ballZ = "Z_ball.png"
fn_ball1 = "ball_1.png"
fn_ball4 = "ball_4.png"
fn_kame = "kameB.png"
fn_ballF = "kame.png"
#----------------- fitxers dels disparadors
fn_Atomix = "Atomix.png"
fn_frizzer = "Frieza.png"
fn_Artwork = "Artwork.png"
fn_buu = "buu.png"
#------------------ fitxers dels recollidors
fn_goku = "goku.png"
fn_goku2 = "trunks.png"
fn_goku3 = "goku4.png"
fn_a161 = "a-16r.png"
fn_songoan = "songohan.png"
fn_vegeta = "vegeta.png"
fn_broly = "Broly.png"
#______________________________________ buu
fn_buu = pygame.image.load(carpeta + fn_buu).convert_alpha()
fn_buu = pygame.transform.scale(fn_buu,(70,130))
#______________________________________ ArtWork
fn_Artwork = pygame.image.load(carpeta + fn_Artwork).convert_alpha()
fn_Artwork = pygame.transform.scale(fn_Artwork,(70,180))
#______________________________________ Atomix
fn_Atomix = pygame.image.load(carpeta + fn_Atomix).convert_alpha()
fn_Atomix = pygame.transform.scale(fn_Atomix,(70,110))
#______________________________________ Frizzer
fn_frizzer = pygame.image.load(carpeta + fn_frizzer).convert_alpha()
fn_frizzer = pygame.transform.scale(fn_frizzer,(70,140))
#______________________________________ Kamehameha
fn_kame = pygame.image.load(carpeta + fn_kame).convert_alpha()              
fn_kame = pygame.transform.scale(fn_kame, (30,80))
#______________________________________ Kamehameha
fn_ballF = pygame.image.load(carpeta + fn_ballF).convert_alpha()              
fn_ballF = pygame.transform.scale(fn_ballF, (30,80))
#_____________________________________ Fons de la finestre 1
background = pygame.image.load(carpeta + fn_pantalla1).convert()            
background = pygame.transform.scale(background, (600, 500))  
#____________________________________ ObjetoqueCae  nivell 1 : ball  
fn_ball1 = pygame.image.load(carpeta + fn_ball1).convert_alpha()              
fn_ball1 = pygame.transform.scale(fn_ball1, (50,50))
#____________________________________Recogedor  nivell 1 : goku 
fn_goku = pygame.image.load(carpeta + fn_goku).convert_alpha()            
fn_goku = pygame.transform.scale(fn_goku, (120,200))
#____________________________________Recogedor  nivell 2 : A 16
fn_a161 = pygame.image.load(carpeta + fn_a161).convert_alpha()    
fn_a161 = pygame.transform.scale(fn_a161, (100,200))
#_____________________________________ Fons de la finestre 2
fn_pantalla2 = pygame.image.load(carpeta + fn_pantalla2).convert()          
fn_pantalla2 = pygame.transform.scale(fn_pantalla2, (600, 500)) 
#____________________________________ ObjetoqueCae  nivell 4 : ball  
fn_ball4 = pygame.image.load(carpeta + fn_ball4).convert_alpha()              
fn_ball4 = pygame.transform.scale(fn_ball4, (50,50))
#____________________________________ Recogedor  nivell 3 : Son Ghoan      
fn_songoan = pygame.image.load(carpeta + fn_songoan).convert_alpha()          
fn_songoan = pygame.transform.scale(fn_songoan, (100,200))
#____________________________________Recogedor  nivell 4: vegeta
vegeta = pygame.image.load(carpeta + fn_vegeta).convert_alpha()        
vegeta = pygame.transform.scale(vegeta, (100,200))
#_____________________________________ Fons de la finestre 3
fn_pantalla3  = pygame.image.load(carpeta + fn_pantalla3).convert()              
fn_pantalla3 = pygame.transform.scale(fn_pantalla3, (600, 500))          
#____________________________________ ObjetoqueCae  nivell 5 : ball Z 
fn_ballZ = pygame.image.load(carpeta + fn_ballZ).convert_alpha()              
fn_ballZ = pygame.transform.scale(fn_ballZ, (50,50))
#____________________________________Recogedor  nivell 5 : goku 2
fn_goku2 = pygame.image.load(carpeta + fn_goku2).convert_alpha()            
fn_goku2 = pygame.transform.scale(fn_goku2, (120,200))
#____________________________________Recogedor  nivell 6 : goku 2
fn_goku3 = pygame.image.load(carpeta + fn_goku3).convert_alpha()            
fn_goku3 = pygame.transform.scale(fn_goku3, (120,200))
#____________________________________ Recogedor  nivel 7 :Broli  
broly = pygame.image.load(carpeta + fn_broly).convert_alpha()          
broly = pygame.transform.scale(broly, (100,200))
dragonbl  = pygame.image.load(carpeta + fn_dragonball).convert()              
dragonbl  = pygame.transform.scale(dragonbl, (600, 500))     
""" ---------------------------------- Música del juego
pygame.mixer.music.load("bell.mp3")  #Themesong.mp3
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play (-1)
"""
falling_x = random.randrange(0, width - 50)     # Coordenada x del objeto que cae
falling_y = -5                                # Coordenada y del objeto que cae
#------------------ marges de la pantalla
background_x = 0          # Coordenada x del fondo
background_y = 0          # Coordenada y del fondo
#--------------  posició del recolector
drago_x = width/2         # Coordenada x del recogedor
drago_y = height - 210    # Coordenada y del recogedor
kame_y = height - 190 # inicialitzar kame_y

#--------------- posició del frizzer
frizz_x = random.randrange(0, width - 70)
frizz_y = 45
kameF_y = 55 # incialitzar kame_y
#--------------- inicialització del boolean
done, tret, flag = False, False, False
while not done :
    clock.tick(30)
    collector = fn_goku
    enemy = fn_Atomix
    fn_ball = fn_ball1
    #-------------------------------- generar el kamehameha
    kame_x = drago_x
    if kame_y < 0 :
        kame_y = height - 200
    kame_rect = fn_kame.get_rect()
    kame_rect.top = kame_y
    kame_rect.left = kame_x 
    #--------------------------------- generar recolector
    drago_rect = collector.get_rect()
    drago_rect.top = drago_y
    drago_rect.left = drago_x
    #-------------------------------- generar bola de drac
    falling_rect = fn_ball.get_rect()
    falling_rect.top = falling_y
    falling_rect.left = falling_x
    #-------------------------------- generar Frizzer   
    frizzer_rect = fn_kame.get_rect()
    frizzer_rect.top = frizz_y
    frizzer_rect.left = frizz_x
    #-------------------------------- generar kame(ballF) dels enemics
    kameF_x = frizz_x  
    if kameF_y > height :
        kameF_y = 35
    ballF_rect = fn_ballF.get_rect()
    ballF_rect.top = kameF_y
    ballF_rect.left = kameF_x
    #------------------------------ en el cas de bola de drac està recollit 
    if drago_rect.colliderect(falling_rect) :
        falling_x = random.randrange(0, width - 50)
        falling_y = -5
        flag = False
        score += 1
    #----------------------------- en el cas del kame tocar al enemic
    if kame_rect.colliderect(frizzer_rect) :
        frizz_x = random.randrange(0, width - 70)
        frizz_y = 25
        flag = False
        score += 5
    #----------------------------- en el cas del kameF tocar al collector
    if ballF_rect.colliderect(drago_rect) :
        live -= 1
        if live > 0 :
            frizz_x = random.randrange(0, width - 70)
            kameF_x = frizz_x
            kameF_y = 35
            flag = False
        else :
            done = final_partida(screen, falling_y)
            continue
        
    #------------------------------- Level 1 : Si puntos menor que 5                
    if score <= 10: # level 1
        level = 1
        #----------------------------- bucle evento    
        kame_y, done, collector_speed, tret_speed = bucle_moment(collector_speed, tret_speed, kame_y) 
        #----------------------------- fin bucle evento 
        kame_y +=tret_speed
        drago_x += collector_speed
        falling_y += falling_speed
        if falling_y > height :
            live -= 1
            if live > 0 :
                falling_y = -5    
            else :
                done = final_partida(screen, falling_y)               
    #-------------------------------  Level 2 : Si puntos entre 5 y 10                
    if  10 < score <= 20:
        level = 2
        falling_speed = 4
        collector = fn_a161           
        #----------------------------- bucle evento    
        kame_y, done, collector_speed, tret_speed = bucle_moment(collector_speed, tret_speed, kame_y) 
        #----------------------------- fin bucle evento  
        kame_y +=tret_speed
        drago_x += collector_speed
        falling_y += falling_speed
        if falling_y > height :
            live -= 1
            if live > 0 :
                falling_y = -5    
            else :
                done = final_partida(screen, falling_y)               
    #------------------------------- Level 3 : Si puntos entre 10 y 15                
    if 20 < score <= 35:
        level = 3
        falling_speed = 5
        background = fn_pantalla3
        collector = fn_songoan
        enemy = fn_frizzer
        fn_ball = fn_ball4
        #----------------------------- bucle evento    
        kame_y, done, collector_speed, tret_speed = bucle_moment(collector_speed, tret_speed, kame_y) 
        #----------------------------- fin bucle evento  
        kame_y +=tret_speed
        drago_x += collector_speed
        falling_y += falling_speed
        if falling_y > height :
            live -= 1   
            if live > 0 :
                falling_y = -5    
            else :
                done = final_partida(screen, falling_y)               
    #-------------------------------  Level 4 : Si puntos entre 10 y 15                   
    if 35 < score <= 40:
        level = 4
        background = fn_pantalla3
        collector = vegeta
        fn_ball = fn_ball4
        falling_speed = 8
        #----------------------------- bucle evento    
        kame_y, done, collector_speed, tret_speed = bucle_moment(collector_speed, tret_speed, kame_y) 
        #----------------------------- fin bucle evento
        kame_y +=tret_speed
        drago_x += collector_speed
        falling_y += falling_speed
        kameF_y += 10
        if falling_y > height :
            live -= 1
            if live > 0 :
                falling_y = -5    
            else :
                done = final_partida(screen, falling_y)
    #------------------------------- Level 5 : Si puntos entre 20 y 30                   
    if 40 < score <= 50:
        level = 5
        background = fn_pantalla2
        collector = fn_goku2
        enemy = fn_Artwork
        fn_ball = fn_ballZ
        falling_speed = 10
        kameF_y += 10
        #----------------------------- bucle evento    
        kame_y, done, collector_speed, tret_speed = bucle_moment(collector_speed, tret_speed, kame_y) 
        #----------------------------- fin bucle evento 
        kame_y +=tret_speed
        drago_x += collector_speed
        falling_y += falling_speed
        if falling_y > height :
            live -= 1
            if live > 0 :
                falling_y = -5    
            else :
                done = final_partida(screen, falling_y)               
    #------------------------------- Level 6 : Si puntos entre 30 i 40                   
    if 50 < score <= 70 :
        level = 6
        background = fn_pantalla2
        collector = fn_goku3
        enemy = fn_frizzer
        fn_ball = fn_ballZ
        falling_speed = 12
        #----------------------------- bucle moment    
        kame_y, done, collector_speed, tret_speed = bucle_moment(collector_speed, tret_speed, kame_y) 
        #----------------------------- final del bucle moment 
        kame_y +=tret_speed                       
        drago_x += collector_speed            
        falling_y += falling_speed
        kameF_y += 10
        if falling_y > height :
            live -= 1
            if live > 0 :
                falling_y = -5    
            else :
                done = final_partida(screen, falling_y)              
    #------------------------------- nivell 7 : si punt entre 40 i 50
    if score > 70 :
        level = 7
        background = dragonbl
        collector = broly
        enemy = fn_buu
        fn_ball = fn_ballZ
        falling_speed = 14
        #----------------------------- bucle moment    
        kame_y, done, collector_speed, tret_speed = bucle_moment(collector_speed, tret_speed, kame_y) 
        #----------------------------- final del bucle moment 
        kame_y +=tret_speed 
        drago_x += collector_speed
        falling_y += falling_speed
        kameF_y += 10
        if falling_y > height :
            live -= 1
            if live > 0 :
                falling_y = -5    
            else :
                done = final_partida(screen, falling_y)        
    #-------------------------------  límit desplaçament lateral dret                   
    if drago_x > width:
        drago_x = 0
    #-------------------------------  límit desplaçament lateral esquerra        
    if drago_x < 0:
        drago_x = width - 150
    #------------------------------- carregar pantalla, protegonista, objecetes       
    screen.blit(background, (0,0))
    screen.blit(collector, (drago_x, drago_y))
    screen.blit(fn_ball, (falling_x, falling_y))       
    screen.blit(fn_kame, (kame_x, kame_y))
    if score % 3 == 0 and score > 0:
        if not flag:
            frizz_x = random.randrange(0, width - 70)
            flag = True
        screen.blit(enemy, (frizz_x, frizz_y))
        if level > 3 :
            screen.blit(fn_ballF, (kameF_x, kameF_y))
    score_text = tipografia.render("Life: {} Level: {} Score: {}" .format(live, level, score), 1, red)
    screen.blit(score_text, (100, 1))
    pygame.display.flip()
    #------------------------ marcador score_text
pygame.quit()
quit()


