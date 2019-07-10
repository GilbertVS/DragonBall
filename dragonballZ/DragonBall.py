# -*- coding: utf-8 -*-
"""
Created on Mon May 20 12:34:31 2019
@file: DragonBallA.py
@description: Video joc dessenvolupat amb la llibreria "pygame" amb el mòdul d'encap-
sulació de les classes, carregar i redimensió dinàmica de les imatges, amb formats
png, jpg, jpng,gif. Segon paquet de l'aplicació BBDD on tenim els registres de les
puntuacions del nostres jugadors, suportable per 1 o 2 jugadors en el mateix temps 
amb nombres de vides incrementables per cada un d'ells 
@author: Gilbert Viader
"""
import pygame
import sqlite3
import random
from datetime import datetime
import time
from pygame.locals import *
from easygui import *
"""
importarem les llibreries de python que necessitarem per soportar els mètodes d'aquestes
amb ordre descendent d'importància en el comportament de l'aplicació
"""
dt = datetime.now()
random.seed(dt.second)
"""
recollirem un nou valor del qual la sèrie de nombres aleatòria sempre serà nova, evitarem 
monotomies del nostre joc, en efecte sorpresa de les figures enemigues.
-------------------------------------------------------------------------------------------------------------
------------------- classes dependent de la classe principal Joc,--------------------------------------------
------------- són Jugado1, Jugador2, Text1, carregaImg, Boladrac --------------------------------------------
-------------------------------------------------------------------------------------------------------------
"""
class Jugador1 (object) :
    """
    creació de la classe per el jugador 1, on emprearem els mètodes de posició
    """
    def __init__ (self, joc) :
        """
        creació del constructor de la classe
        """
        self.dreta_jug1 = pygame.K_RIGHT 
        self.esque_jug1 = pygame.K_LEFT
        self.tret_jug1 = pygame.K_RETURN
        self.jugador1_speed = 0
        self.tret1_speed = 0
        self.acabat1 = False
        """ inicialització de les variables per el jugador1 """
        self.amplada_jugador = joc.amplada_Pantalla/6
        self.alsada_jugador = joc.alsada_Pantalla/3
        """ mides dels jugadors """
        self.amplada_kame = joc.amplada_Pantalla/26
        self.alsada_kame = joc.alsada_Pantalla/8
        """ mides dels kamehame """
        self.j1_x = joc.amplada_Pantalla*2/3
        self.j1_y = joc.alsada_Pantalla - self.alsada_jugador
        self.ka1_x = self.j1_x
        self.ka1_y = joc.alsada_Pantalla - self.alsada_kame        
        self.canvi_pos1 = 50
        self.life1 = 3
        self.score1 = 0
        """ posicions del jugador i projectil en la pantalla """
    def actualJuga (self, joc) :
        """
        creació del mètode per l'actualització del jugador
        """
        self.amplada_jugador = joc.amplada_Pantalla/6
        self.alsada_jugador = joc.alsada_Pantalla/3
        """ mides dels jugadors """
        self.amplada_kame = joc.amplada_Pantalla/26
        self.alsada_kame = joc.alsada_Pantalla/8
        """ mides dels kamehame """
        self.j1_x = joc.amplada_Pantalla*2/3
        self.j1_y = joc.alsada_Pantalla - self.alsada_jugador
        self.ka1_x = self.j1_x
        self.ka1_y = joc.alsada_Pantalla - self.alsada_kame
        self.canvi_pos1 = 50
        """ posicions del jugador i projectil en la pantalla """
class Text1 () :
    """
    creació de la classe del Text1 per la pantalla interactiva, 
    """
    def __init__ (self) :
        """
        creació del constructor de la classe
        """
        self.color_txt1 = (12, 12, 12)
        self.color_txt2 = (12, 12, 12)
        self.color_txt3 = (12, 12, 12)
        self.color_txt4 = (12, 12, 12)
        self.color_txt5 = (12, 12, 12)      
    def actualProj (self) :
        """
        creació del mètode per l'actualització del jugador
        """
        self.color_txt1 = (12, 12, 12)
        self.color_txt2 = (12, 12, 12)
        self.color_txt3 = (12, 12, 12)
        self.color_txt4 = (12, 12, 12)
        self.color_txt5 = (12, 12, 12)
class Jugador2 (object) :
    """
    creació de la classe per el jugador 2, on emprearem els mètodes de posició
    """
    def __init__ (self, joc) :
        """
        creació del constructor de la classe
        """
        self.dreta_jug2 = 115
        self.esque_jug2 = 97
        self.tret_jug2 = pygame.K_SPACE
        self.jugador2_speed = 0
        self.tret2_speed = 0
        self.acabat2 = False
        self.amplada_jugador = joc.amplada_Pantalla/6
        self.alsada_jugador = joc.alsada_Pantalla/3
        """ mides dels jugadors """
        self.amplada_kame = joc.amplada_Pantalla/26
        self.alsada_kame = joc.alsada_Pantalla/8
        """ mides dels kamehame """
        """ carregà de la imatge inicial del jugador2 i el seu projectil"""
        self.j2_x = joc.amplada_Pantalla/3
        self.j2_y = joc.alsada_Pantalla - self.alsada_jugador
        self.ka2_x = self.j2_x
        self.ka2_y = joc.alsada_Pantalla - self.alsada_kame
        self.canvi_pos2 = 50      
        """ posicions del jugador i projectil en la pantalla """     
        self.life2 = 3
        self.score2 = 0
        """ marcador per el jugador 2 """
    def actualJuga (self, joc) :
        """
        creació del mètode per l'actualització del jugador
        """
        self.amplada_jugador = joc.amplada_Pantalla/6
        self.alsada_jugador = joc.alsada_Pantalla/3
        """ mides dels jugadors """
        self.amplada_kame = joc.amplada_Pantalla/26
        self.alsada_kame = joc.alsada_Pantalla/8
        """ mides dels kamehame """
        self.j2_x = joc.amplada_Pantalla/3
        self.j2_y = joc.alsada_Pantalla - self.alsada_jugador
        self.ka2_x = self.j2_x
        self.ka2_y = joc.alsada_Pantalla - self.alsada_kame
        self.canvi_pos2 = 50       
        """ posicions del jugador i projectil en la pantalla """     
class carregaImg (object) :
    """
    creació de la classe del projectil per el jugador 2, 
    """
    def __init__ (self, joc, juga1, juga2, ball, enem1, pro1, enem2, pro2) :
        """
        creació del constructor de la classe
        """
        self.kame = "KameB.png"
        self.kame = pygame.image.load(self.kame).convert_alpha()
        self.kame1 = pygame.transform.scale(self.kame, (int(juga1.amplada_kame), int(juga1.alsada_kame)))
        self.kame2 = pygame.transform.scale(self.kame, (int(juga2.amplada_kame), int(juga2.alsada_kame)))
        """ kamehame del jugadors """
        self.ballD = "ball_1.png"
        self.ballD = pygame.image.load(self.ballD).convert_alpha()
        self.ballD = pygame.transform.scale(self.ballD, (int(ball.amplada_ball), int(ball.alsada_ball)))
        self.ball4 = "ball_4.png"
        self.ball4 = pygame.image.load(self.ball4).convert_alpha()
        self.ball4 = pygame.transform.scale(self.ball4, (int(ball.amplada_ball), int(ball.alsada_ball)))
        self.ballZ = "z_ball.png"
        self.ballZ = pygame.image.load(self.ballZ).convert_alpha()
        self.ballZ = pygame.transform.scale(self.ballZ, (int(ball.amplada_ball), int(ball.alsada_ball)))
        self.ball = self.ballD
        """ boles de drac """
        self.a16 = "a-16.png"
        self.a16 = pygame.image.load(self.a16).convert_alpha()
        self.a16 = pygame.transform.scale(self.a16, (int(juga1.amplada_jugador), int(juga1.alsada_jugador)))
        self.a16r = "a-16r.png"
        self.a16r = pygame.image.load(self.a16r).convert_alpha()
        self.a16r = pygame.transform.scale(self.a16r, (int(juga1.amplada_jugador), int(juga1.alsada_jugador)))
        """ A 16 miran a la dreta i a l'esquerra """
        self.Trunks = "Trunks.png"
        self.Trunks = pygame.image.load(self.Trunks).convert_alpha()
        self.Trunks = pygame.transform.scale(self.Trunks, (int(juga1.amplada_jugador), int(juga1.alsada_jugador)))
        self.Trunksr = "Trunksr.png"
        self.Trunksr = pygame.image.load(self.Trunksr).convert_alpha()
        self.Trunksr = pygame.transform.scale(self.Trunksr, (int(juga1.amplada_jugador), int(juga1.alsada_jugador)))
        """ Trunks miran a la dreta i a l'esquerra """
        self.Vegeta = "Vegeta.png"
        self.Vegeta = pygame.image.load(self.Vegeta).convert_alpha()
        self.Vegeta = pygame.transform.scale(self.Vegeta, (int(juga1.amplada_jugador), int(juga1.alsada_jugador)))        
        self.Vegetar = "Vegetar.png"
        self.Vegetar = pygame.image.load(self.Vegetar).convert_alpha()
        self.Vegetar = pygame.transform.scale(self.Vegetar, (int(juga1.amplada_jugador), int(juga1.alsada_jugador)))         
        """ Vegeta miran a la dreta i a l'esquerra """  
        self.Vegeta1 = "vegeta1.png"
        self.Vegeta1 = pygame.image.load(self.Vegeta1).convert_alpha()
        self.Vegeta1 = pygame.transform.scale(self.Vegeta1, (int(juga1.amplada_jugador), int(juga1.alsada_jugador))) 
        self.Vegeta1r = "vegeta1r.png"
        self.Vegeta1r = pygame.image.load(self.Vegeta1r).convert_alpha()
        self.Vegeta1r = pygame.transform.scale(self.Vegeta1r, (int(juga1.amplada_jugador), int(juga1.alsada_jugador)))         
        """ Vegeta miran a la dreta i a l'esquerra """ 
        self.picolo = "piccolo.png"
        self.picolor = "piccolor.png"
        """ piccolo miran a la dreta i a l'esquerra """ 
        self.goku = "goku.png"
        self.goku = pygame.image.load(self.goku).convert_alpha()
        self.goku = pygame.transform.scale(self.goku, (int(juga2.amplada_jugador), int(juga2.alsada_jugador)))
        self.gokur = "gokur.png"
        self.gokur = pygame.image.load(self.gokur).convert_alpha()
        self.gokur = pygame.transform.scale(self.gokur, (int(juga2.amplada_jugador), int(juga2.alsada_jugador)))        
        """ Goku miran a la dreta i a l'esquerra """
        self.goku7 = "goku7.png"
        self.goku7 = pygame.image.load(self.goku7).convert_alpha()
        self.goku7 = pygame.transform.scale(self.goku7, (int(juga2.amplada_jugador), int(juga2.alsada_jugador)))
        self.goku7r = "goku7r.png"
        self.goku7r = pygame.image.load(self.goku7r).convert_alpha()
        self.goku7r = pygame.transform.scale(self.goku7r, (int(juga2.amplada_jugador), int(juga2.alsada_jugador)))
        """ Goku miran a la dreta i a l'esquerra """
        self.goku4 = "goku4.png"
        self.goku4 = pygame.image.load(self.goku4).convert_alpha()
        self.goku4 = pygame.transform.scale(self.goku4, (int(juga2.amplada_jugador), int(juga2.alsada_jugador)))
        self.goku4r = "goku4r.png"
        self.goku4r = pygame.image.load(self.goku4r).convert_alpha()
        self.goku4r = pygame.transform.scale(self.goku4r, (int(juga2.amplada_jugador), int(juga2.alsada_jugador)))
        """ Goku miran a la dreta i a l'esquerra """
        self.goten = "goten.png"
        self.gotenr = "gotenr.png"
        """ Goten miran a la dreta i a l'esquerra """        
        self.songohan = "songohan.png"
        self.songohan = pygame.image.load(self.songohan).convert_alpha()
        self.songohan = pygame.transform.scale(self.songohan, (int(juga2.amplada_jugador), int(juga2.alsada_jugador)))
        self.songohanr = "songohanr.png"
        self.songohanr = pygame.image.load(self.songohanr).convert_alpha()
        self.songohanr = pygame.transform.scale(self.songohanr, (int(juga2.amplada_jugador), int(juga2.alsada_jugador)))        
        """ Songohan miran a la dreta i a l'esquerra """
        self.goku2 = "goku2.png"
        self.goku2 = pygame.image.load(self.goku2).convert_alpha()
        self.goku2 = pygame.transform.scale(self.goku2, (int(joc.amplada_Pantalla), int(joc.alsada_Pantalla)))
        self.goku8 = "goku8.png"
        self.goku8 = pygame.image.load(self.goku8).convert_alpha()
        self.goku8 = pygame.transform.scale(self.goku8, (int(joc.amplada_Pantalla/2), int(joc.alsada_Pantalla/2)))
        self.Fons_n1 = "nameq.jpg"
        self.Fons_n1 = pygame.image.load(self.Fons_n1).convert_alpha()
        self.Fons_n1 = pygame.transform.scale(self.Fons_n1, (int(joc.amplada_Pantalla), int(joc.alsada_Pantalla)))
        self.Fons_n3 = "Namek1.png"
        self.Fons_n3 = pygame.image.load(self.Fons_n3).convert_alpha()
        self.Fons_n3 = pygame.transform.scale(self.Fons_n3, (int(joc.amplada_Pantalla), int(joc.alsada_Pantalla)))
        self.Fons_n5 = "nameDrag.jpeg"
        self.Fons_n5 = pygame.image.load(self.Fons_n5).convert_alpha()
        self.Fons_n5 = pygame.transform.scale(self.Fons_n5, (int(joc.amplada_Pantalla), int(joc.alsada_Pantalla)))
        self.Fons_n7 = "brolyEsc.jpg"
        self.Fons_n7 = pygame.image.load(self.Fons_n7).convert_alpha()
        self.Fons_n7 = pygame.transform.scale(self.Fons_n7, (int(joc.amplada_Pantalla), int(joc.alsada_Pantalla)))
        self.Fons = self.Fons_n1
        self.juga1dreta = self.a16r
        self.juga1esque = self.a16
        self.juga2dreta = self.goku
        self.juga2esque = self.gokur
        """carregar dels fitxers imatge en variables per el fons de les finestres"""
        self.goku3 = "goku31.png"
        self.goku3 = pygame.image.load(self.goku3)
        pygame.display.set_icon(self.goku3)
        """ icona del joc per la finestre pygame """
        self.atomix = "Atomix1.png"
        self.atomix = pygame.image.load(self.atomix)
        self.atomix = pygame.transform.scale(self.atomix, (int(enem1.amplada_enemic), int(enem1.alsada_enemic)))
        self.buu = "buu1.png"
        self.buu = pygame.image.load(self.buu)
        self.buu = pygame.transform.scale(self.buu, (int(enem1.amplada_enemic), int(enem1.alsada_enemic)))
        """ carregar l'enemic 1 """
        self.kame0 = "kame0.png"
        self.kame0 = pygame.image.load(self.kame0)
        self.kame0 = pygame.transform.scale(self.kame0, (int(pro1.amplada_project), int(pro1.alsada_project))) 
        """ carrega el projectil de l'enemic 1 """
        self.frizer = "frieza.png"
        self.frizer = pygame.image.load(self.frizer)
        self.frizer = pygame.transform.scale(self.frizer, (int(enem2.amplada_enemic), int(enem2.alsada_enemic)))
        self.Artwork = "Artwork.png"
        self.Artwork = pygame.image.load(self.Artwork)
        self.Artwork = pygame.transform.scale(self.Artwork, (int(enem2.amplada_enemic), int(enem2.alsada_enemic)))
        """ carrega de l'enemic 2 """
        self.ball_F = "ball_F.png"
        self.ball_F = pygame.image.load(self.ball_F)
        self.ball_F = pygame.transform.scale(self.ball_F, (int(pro2.amplada_project), int(pro2.alsada_project)))
        """ càrrega del projectil de l'enemic 2 """
    def actualImg (self, joc, juga1, juga2, ball, enem1, pro1, enem2, pro2) :
        """
        creació del mètode per l'actualització del jugador
        """
        self.kame = "KameB.png"
        self.kame = pygame.image.load(self.kame).convert_alpha()
        self.kame1 = pygame.transform.scale(self.kame, (int(juga1.amplada_kame), int(juga1.alsada_kame)))
        self.kame2 = pygame.transform.scale(self.kame, (int(juga2.amplada_kame), int(juga2.alsada_kame)))
        """ kamehame del jugadors """
        self.ballD = "ball_1.png"
        self.ballD = pygame.image.load(self.ballD).convert_alpha()
        self.ballD = pygame.transform.scale(self.ballD, (int(ball.amplada_ball), int(ball.alsada_ball)))
        self.ball4 = "ball_4.png"
        self.ball4 = pygame.image.load(self.ball4).convert_alpha()
        self.ball4 = pygame.transform.scale(self.ball4, (int(ball.amplada_ball), int(ball.alsada_ball)))
        self.ballZ = "z_ball.png"
        self.ballZ = pygame.image.load(self.ballZ).convert_alpha()
        self.ballZ = pygame.transform.scale(self.ballZ, (int(ball.amplada_ball), int(ball.alsada_ball))) 
        self.ball = self.ballD
        """ boles de drac """
        self.a16 = "a-16.png"
        self.a16 = pygame.image.load(self.a16).convert_alpha()
        self.a16 = pygame.transform.scale(self.a16, (int(juga1.amplada_jugador), int(juga1.alsada_jugador)))
        self.a16r = "a-16r.png"
        self.a16r = pygame.image.load(self.a16r).convert_alpha()
        self.a16r = pygame.transform.scale(self.a16r, (int(juga1.amplada_jugador), int(juga1.alsada_jugador)))
        """ A 16 miran a la dreta i a l'esquerra """
        self.Trunks = "Trunks.png"
        self.Trunks = pygame.image.load(self.Trunks).convert_alpha()
        self.Trunks = pygame.transform.scale(self.Trunks, (int(juga1.amplada_jugador), int(juga1.alsada_jugador)))
        self.Trunksr = "Trunksr.png"
        self.Trunksr = pygame.image.load(self.Trunksr).convert_alpha()
        self.Trunksr = pygame.transform.scale(self.Trunksr, (int(juga1.amplada_jugador), int(juga1.alsada_jugador)))
        """ Trunks miran a la dreta i a l'esquerra """
        self.Vegeta = "Vegeta.png"
        self.Vegeta = pygame.image.load(self.Vegeta).convert_alpha()
        self.Vegeta = pygame.transform.scale(self.Vegeta, (int(juga1.amplada_jugador), int(juga1.alsada_jugador)))        
        self.Vegetar = "Vegetar.png"
        self.Vegetar = pygame.image.load(self.Vegetar).convert_alpha()
        self.Vegetar = pygame.transform.scale(self.Vegetar, (int(juga1.amplada_jugador), int(juga1.alsada_jugador)))         
        """ Vegeta miran a la dreta i a l'esquerra """  
        self.Vegeta1 = "vegeta1.png"
        self.Vegeta1 = pygame.image.load(self.Vegeta1).convert_alpha()
        self.Vegeta1 = pygame.transform.scale(self.Vegeta1, (int(juga1.amplada_jugador), int(juga1.alsada_jugador))) 
        self.Vegeta1r = "vegeta1r.png"
        self.Vegeta1r = pygame.image.load(self.Vegeta1r).convert_alpha()
        self.Vegeta1r = pygame.transform.scale(self.Vegeta1r, (int(juga1.amplada_jugador), int(juga1.alsada_jugador)))         
        """ Vegeta miran a la dreta i a l'esquerra """ 
        self.picolo = "piccolo.png"
        self.picolor = "piccolor.png"
        """ piccolo miran a la dreta i a l'esquerra """ 
        self.goku = "goku.png"
        self.goku = pygame.image.load(self.goku).convert_alpha()
        self.goku = pygame.transform.scale(self.goku, (int(juga2.amplada_jugador), int(juga2.alsada_jugador)))
        self.gokur = "gokur.png"
        self.gokur = pygame.image.load(self.gokur).convert_alpha()
        self.gokur = pygame.transform.scale(self.gokur, (int(juga2.amplada_jugador), int(juga2.alsada_jugador)))        
        """ Goku miran a la dreta i a l'esquerra """
        self.goku7 = "goku7.png"
        self.goku7 = pygame.image.load(self.goku7).convert_alpha()
        self.goku7 = pygame.transform.scale(self.goku7, (int(juga2.amplada_jugador), int(juga2.alsada_jugador)))
        self.goku7r = "goku7r.png"
        self.goku7r = pygame.image.load(self.goku7r).convert_alpha()
        self.goku7r = pygame.transform.scale(self.goku7r, (int(juga2.amplada_jugador), int(juga2.alsada_jugador)))
        """ Goku miran a la dreta i a l'esquerra """
        self.goku4 = "goku4.png"
        self.goku4 = pygame.image.load(self.goku4).convert_alpha()
        self.goku4 = pygame.transform.scale(self.goku4, (int(juga2.amplada_jugador), int(juga2.alsada_jugador)))
        self.goku4r = "goku4r.png"
        self.goku4r = pygame.image.load(self.goku4r).convert_alpha()
        self.goku4r = pygame.transform.scale(self.goku4r, (int(juga2.amplada_jugador), int(juga2.alsada_jugador)))
        """ Goku miran a la dreta i a l'esquerra """
        self.goten = "goten.png"
        self.gotenr = "gotenr.png"
        """ Goten miran a la dreta i a l'esquerra """        
        self.songohan = "songohan.png"
        self.songohan = pygame.image.load(self.songohan).convert_alpha()
        self.songohan = pygame.transform.scale(self.songohan, (int(juga2.amplada_jugador), int(juga2.alsada_jugador)))
        self.songohanr = "songohanr.png"
        self.songohanr = pygame.image.load(self.songohanr).convert_alpha()
        self.songohanr = pygame.transform.scale(self.songohanr, (int(juga2.amplada_jugador), int(juga2.alsada_jugador)))        
        """ Songohan miran a la dreta i a l'esquerra """
        self.goku2 = "goku2.png"
        self.goku2 = pygame.image.load(self.goku2).convert_alpha()
        self.goku2 = pygame.transform.scale(self.goku2, (int(joc.amplada_Pantalla), int(joc.alsada_Pantalla)))
        self.goku8 = "goku8.png"
        self.goku8 = pygame.image.load(self.goku8).convert_alpha()
        self.goku8 = pygame.transform.scale(self.goku8, (int(joc.amplada_Pantalla/2), int(joc.alsada_Pantalla/2)))
        self.Fons_n1 = "nameq.jpg"
        self.Fons_n1 = pygame.image.load(self.Fons_n1).convert_alpha()
        self.Fons_n1 = pygame.transform.scale(self.Fons_n1, (int(joc.amplada_Pantalla), int(joc.alsada_Pantalla)))
        self.Fons_n3 = "Namek1.png"
        self.Fons_n3 = pygame.image.load(self.Fons_n3).convert_alpha()
        self.Fons_n3 = pygame.transform.scale(self.Fons_n3, (int(joc.amplada_Pantalla), int(joc.alsada_Pantalla)))
        self.Fons_n5 = "nameDrag.jpeg"
        self.Fons_n5 = pygame.image.load(self.Fons_n5).convert_alpha()
        self.Fons_n5 = pygame.transform.scale(self.Fons_n5, (int(joc.amplada_Pantalla), int(joc.alsada_Pantalla)))
        self.Fons_n7 = "brolyEsc.jpg"
        self.Fons_n7 = pygame.image.load(self.Fons_n7).convert_alpha()
        self.Fons_n7 = pygame.transform.scale(self.Fons_n7, (int(joc.amplada_Pantalla), int(joc.alsada_Pantalla)))
        self.Fons = self.Fons_n1
        self.juga1dreta = self.a16r
        self.juga1esque = self.a16
        self.juga2dreta = self.goku
        self.juga2esque = self.gokur
        """carregar dels fitxers imatge en variables per el fons de les finestres"""
        self.goku3 = "goku31.png"
        self.goku3 = pygame.image.load(self.goku3)
        pygame.display.set_icon(self.goku3)
        """ icona del joc per la finestre pygame """
        self.atomix = "Atomix1.png"
        self.atomix = pygame.image.load(self.atomix)
        self.atomix = pygame.transform.scale(self.atomix, (int(enem1.amplada_enemic), int(enem1.alsada_enemic)))
        self.buu = "buu1.png"
        self.buu = pygame.image.load(self.buu)
        self.buu = pygame.transform.scale(self.buu, (int(enem1.amplada_enemic), int(enem1.alsada_enemic)))
        """ carregar l'enemic 1 """
        self.kame0 = "kame0.png"
        self.kame0 = pygame.image.load(self.kame0)
        self.kame0 = pygame.transform.scale(self.kame0, (int(pro1.amplada_project), int(pro1.alsada_project))) 
        """ carrega el projectil de l'enemic 1 """
        self.frizer = "frieza.png"
        self.frizer = pygame.image.load(self.frizer)
        self.frizer = pygame.transform.scale(self.frizer, (int(enem2.amplada_enemic), int(enem2.alsada_enemic)))
        self.Artwork = "Artwork.png"
        self.Artwork = pygame.image.load(self.Artwork)
        self.Artwork = pygame.transform.scale(self.Artwork, (int(enem2.amplada_enemic), int(enem2.alsada_enemic)))
        """ carrega de l'enemic 2 """
        self.ball_F = "ball_F.png"
        self.ball_F = pygame.image.load(self.ball_F)
        self.ball_F = pygame.transform.scale(self.ball_F, (int(pro2.amplada_project), int(pro2.alsada_project)))
        """ càrrega del projectil de l'enemic 2 """
        
class Enemic1 (object) :
    """
    creació de la classe per el enemic 1, on emprearem els mètodes de posició
    """
    def __init__ (self, joc) :
        """
        creació del constructor de la classe
        """
        self.enemic1 = ""
        self.amplada_enemic = joc.amplada_Pantalla/10
        self.alsada_enemic = joc.alsada_Pantalla/5
        self.e1_x = random.randrange(0, int(joc.amplada_Pantalla - self.amplada_enemic))
        self.e1_y = self.alsada_enemic/2
        self.e1Amagat = False
        """ posició i atributs de l'enemic 1 """
    def actualJuga (self, joc) :
        """
        creació del mètode per l'actualització de l'enemic 1
        """ 
        self.enemic1 = ""
        self.amplada_enemic = joc.amplada_Pantalla/10
        self.alsada_enemic = joc.alsada_Pantalla/5
        self.e1_x = random.randrange(0, int(joc.amplada_Pantalla - self.amplada_enemic))
        self.e1_y = self.alsada_enemic/2
        self.e1Amagat = False
        """ posició i atributs de l'enemic 1 """
class EnemicPro1 (object) :
    """
    creació de la classe del projectil per el enemicPro 1, 
    """
    def __init__ (self, joc, enem1) :
        """
        creació del constructor de la classe
        """
        self.amplada_project = joc.amplada_Pantalla/14
        self.alsada_project = joc.alsada_Pantalla/12
        self.pro1_x = enem1.e1_x
        self.pro1_y = enem1.e1_y
        """ posicions i atributs del projectil de l'enemic 1 """
    def actualProj (self, joc, enem1) :
        """
        creació del mètode per l'actualització de l'enemic 1
        """
        self.amplada_project = joc.amplada_Pantalla/14
        self.alsada_project = joc.alsada_Pantalla/12
        self.pro1_x = enem1.e1_x
        self.pro1_y = enem1.e1_y
        """ posicions i atributs del projectil de l'enemic 1 """
class Enemic2 (object) :
    """
    creació de la classe per el enemic 2, on emprearem els mètodes de posició
    """
    def __init__ (self, joc) :
        """
        creació del constructor de la classe
        """
        self.enemic2 = ""
        self.amplada_enemic = joc.amplada_Pantalla/8
        self.alsada_enemic = joc.alsada_Pantalla/3
        self.e2_x = random.randrange(0, int(joc.amplada_Pantalla - self.amplada_enemic))
        self.e2_y = self.alsada_enemic/2
        self.e2Amagat = False
    def actualJuga (self, joc) :
        """
        creació del mètode per l'actualització de l'enemic 2
        """
        self.enemic2 = ""
        self.amplada_enemic = joc.amplada_Pantalla/12
        self.alsada_enemic = joc.alsada_Pantalla/4
        self.e2_x = random.randrange(0, int(joc.amplada_Pantalla - self.amplada_enemic))
        self.e2_y = self.alsada_enemic/2
        self.e2Amagat = False
class EnemicPro2 (object) :
    """
    creació de la classe del projectil per el enemicPro 2, 
    """
    def __init__ (self, joc, enem2) :
        """
        creació del constructor de la classe
        """
        self.amplada_project = joc.amplada_Pantalla/14
        self.alsada_project = joc.alsada_Pantalla/12
        self.pro2_x = enem2.e2_x
        self.pro2_y = enem2.e2_y
    def actualProj (self, joc, enem2) :
        """
        creació del mètode per l'actualització de l'enemic 2
        """
        self.amplada_project = joc.amplada_Pantalla/14
        self.alsada_project = joc.alsada_Pantalla/12
        self.pro2_x = enem2.e2_x
        self.pro2_y = enem2.e2_y
class Bolesdrac (object) :
    """
    creació de la classe de les boles de drac on ens recuperarem amb increments
    de vida
    """
    def __init__ (self, joc) :
        """
        creació del constructor de la classe
        """
        #self.ballD = ""
        self.boles_speed = 6
        self.alsada_ball = joc.alsada_Pantalla / 12
        self.amplada_ball = joc.amplada_Pantalla / 14
        self.ball_x = random.randrange(0, int(joc.amplada_Pantalla - self.amplada_ball))
        self.ball_y = 0  
    def actualBole (self, joc) :
        """
        creació del mètode per l'actual posició de la bola de drac
        """
        #self.ball = img.ballD
        self.alsada_ball = joc.alsada_Pantalla / 12
        self.amplada_ball = joc.amplada_Pantalla / 14 
""" començament de la classe principal Joc """
class Joc (object) :
    """
    crearem la classe on es desenvoluparà el joc passant com a paràmetre
    un objecte el qual l'encapsulat de la class serà destruit quan sortim d'ella
    """
    def __init__ (self) :
        """
        crearem el constructor de la classe amb la inicialització del seus atributs
        """
        #super().__init__()
        self.amplada_Pantalla = 550
        self.alsada_Pantalla = 400
        """ mides de la pantalla """      
        self.color_scr = (12, 222, 12)
        self.level = 1
        self.entrab1, self.entrab2 = False, False
        self.ent1, self.ent2 = False, False
        """
        inicialització de les variable globals del programa
        """
    def modiMides (self) :
        """
        creació del mètode de modificar les mides
        """
        self.dimensions = [self.amplada_Pantalla, self.alsada_Pantalla]
        self.pantalla = pygame.display.set_mode(self.dimensions)
        """ 
        dimensionar la finestre de pygame 
        """ 
        self.mida_txt = int(self.alsada_Pantalla/10)
        """ mida del text del menú """
        self.marca_txt = int(self.alsada_Pantalla/10)
        """ mida del text del marcador """
        self.amplada_jugador = self.amplada_Pantalla/6
        self.alsada_jugador = self.alsada_Pantalla/3
        """ mides dels jugadors """
        self.amplada_kame = self.amplada_Pantalla/26
        self.alsada_kame = self.alsada_Pantalla/8
        """ mides dels kamehame """ 
    def game_over (self,juga1, juga2, joc, img, txt1) :
        """
        creació del mètode de final de partida
        """
        self.tipografia = pygame.font.SysFont("serif", joc.marca_txt)
        self.marcador2 = self.tipografia.render("Score:{} life:{} ||L.:".format(juga2.score2, juga2.life2),1,(222, 62, 62))
        self.marcador1 = self.tipografia.render("{}|| life:{} Score:{}".format(joc.level, juga1.life1, juga1.score1),1,(62, 62, 222))
        self.txt_final = self.tipografia.render("GAME OVER... return to start",1,(26, 26, 26))
        joc.pantalla.blit(img.Fons, (0, 0))
        joc.pantalla.blit(self.marcador2, (0, 10))
        joc.pantalla.blit(self.marcador1, (joc.amplada_Pantalla/2, 10))
        joc.pantalla.blit(self.txt_final, (20, joc.alsada_Pantalla/2))
        pygame.display.flip()
        juga1.acabat1 = False
        juga2.acabat2 = False
        txt1.color_txt1 = (12, 12, 12)
        juga1.j1_x = joc.amplada_Pantalla*2/3
        juga2.j2_x = joc.amplada_Pantalla/3
        return True
# ------------------------------------------------------------------------------------------------------
#    ----------------------------------- mètodes per el joc del bola de drac Z -------------------------
#   ---------------------------------------------------------------------------------------------------- 
    def procesEvents (self, juga1, juga2, joc, img) :
        """
        crearem el mètode on tenim tots els esdeveniments de la del joc en definions
        de tecles de control
        """
        fer, pause = False, True
        for moment in pygame.event.get() :
            if moment.type == pygame.QUIT :
                fer = True
            elif moment.type == pygame.KEYDOWN :
                if moment.key == juga1.dreta_jug1 :           
                    juga1.jugador1_speed = 10
                    juga1.canvi_pos1 = 50
                    juga1.guerrer1 = img.juga1dreta
                if moment.key == juga1.esque_jug1 :
                    juga1.jugador1_speed = -10
                    juga1.canvi_pos1 = 0
                    juga1.guerrer1 = img.juga1esque
                if moment.key == juga1.tret_jug1 :
                    juga1.tret1_speed = -50    
                if moment.key == juga2.dreta_jug2 :           
                    juga2.jugador2_speed = 10
                    juga2.canvi_pos2 = 60
                    juga2.guerrer2 = img.juga2dreta
                if moment.key == juga2.esque_jug2 :
                    juga2.jugador2_speed = -10
                    juga2.canvi_pos2 = 10
                    juga2.guerrer2 = img.juga2esque
                if moment.key == juga2.tret_jug2 :
                    juga2.tret2_speed = -50   
                if moment.key == pygame.K_ESCAPE :                
                    fer = True
                if moment.key == 112 :
                    pause = False                           
            elif moment.type == pygame.KEYUP :
                if moment.key == juga1.dreta_jug1 or moment.key == juga1.esque_jug1 :
                    juga1.jugador1_speed = 0
                if moment.key == juga2.dreta_jug2 or moment.key == juga2.esque_jug2 :
                    juga2.jugador2_speed = 0
                if moment.key == juga1.tret_jug1 :
                    juga1.tret1_speed = 0
                    juga1.ka1_y = joc.alsada_Pantalla - juga1.alsada_kame
                if moment.key == juga2.tret_jug2 :
                    juga2.tret2_speed = 0
                    juga2.ka2_y = joc.alsada_Pantalla - juga2.alsada_kame
        return fer, pause    
    def paused (self, pause, joc) :
        """
        crearem el mètode per parar el joc 
        """
        for moment in pygame.event.get():
            if moment.type == pygame.QUIT :
                pause = True
            elif moment.type == pygame.KEYDOWN :
                if moment.key == pygame.K_ESCAPE :
                    pause = True
                if moment.key == 112 :
                    pause = True
        tipografia = pygame.font.SysFont("serif", joc.mida_txt)
        texte = tipografia.render("PAUSED", 1, (21, 21, 21))
        joc.pantalla.blit(texte, (joc.amplada_Pantalla/3, joc.alsada_Pantalla/2))
        pygame.mixer.music.pause()
        pygame.display.flip()
        return pause
    def logicaExecutar (self, juga1, juga2, joc, img, bolesD, txt, enem1, pro1, enem2, pro2) :
        """
        crearem el mètode on aniran fer actualitzacions de les noves posicions del objectes 
        """
        final = False
        """ boolean per sortir  del bucle """
        juga1.j1_x += juga1.jugador1_speed
        juga2.j2_x += juga2.jugador2_speed
        bolesD.ball_y += bolesD.boles_speed
        pro1.pro1_y += bolesD.boles_speed
        pro2.pro2_y += bolesD.boles_speed
        juga1.ka1_x = juga1.j1_x + juga1.canvi_pos1
        juga1.ka1_y += juga1.tret1_speed
        juga2.ka2_x = juga2.j2_x + juga2.canvi_pos2
        juga2.ka2_y += juga2.tret2_speed
        """ canvis de posicions del objectes """
        juga1.juga1_rect = juga1.guerrer1.get_rect()
        juga1.juga1_rect.top = juga1.j1_y
        juga1.juga1_rect.left = juga1.j1_x        
        juga1.kame1_rect = img.kame1.get_rect()
        juga1.kame1_rect.top = juga1.ka1_y
        juga1.kame1_rect.left = juga1.ka1_x
        """ conversió a rectangle de l'objecte 1 """
        juga2.juga2_rect = juga2.guerrer2.get_rect()
        juga2.juga2_rect.top = juga2.j2_y
        juga2.juga2_rect.left = juga2.j2_x        
        juga2.kame2_rect = img.kame2.get_rect()
        juga2.kame2_rect.top = juga2.ka2_y
        juga2.kame2_rect.left = juga2.ka2_x
        """ conversió a rectangle de l'objecte 2 """
        bolesD.ballD_rect = img.ball.get_rect()
        bolesD.ballD_rect.top = bolesD.ball_y
        bolesD.ballD_rect.left = bolesD.ball_x 
        """ conversió a rectangle de les boles de drac """
        enem1.enemic1_rect = enem1.enemic1.get_rect()
        enem1.enemic1_rect.top = enem1.e1_y
        enem1.enemic1_rect.left = enem1.e1_x
        """ conversió a rectangle l'enemic 1 """
        pro1.project1_rect = img.kame0.get_rect()
        pro1.project1_rect.top = pro1.pro1_y
        pro1.project1_rect.left = pro1.pro1_x
        """ conversió a rectangle el projectil de l'enemic 1 """
        enem2.enemic2_rect = enem2.enemic2.get_rect()
        enem2.enemic2_rect.top = enem2.e2_y
        enem2.enemic2_rect.left = enem2.e2_x
        """ conversió a rectangle l'enemic 1 """
        pro2.project2_rect = img.ball_F.get_rect()
        pro2.project2_rect.top = pro2.pro2_y
        pro2.project2_rect.left = pro2.pro2_x
        """ conversió a rectangle el projectil de l'enemic 1 """
        if juga1.juga1_rect.colliderect(bolesD.ballD_rect) and (juga1.acabat1 == False) :
            bolesD.ball_y = 0
            bolesD.ball_x = random.randrange(0, int(joc.amplada_Pantalla - bolesD.amplada_ball))
            juga1.score1 += 1
        if juga2.juga2_rect.colliderect(bolesD.ballD_rect) and (juga2.acabat2 == False) :
            bolesD.ball_y = 0
            bolesD.ball_x = random.randrange(0, int(joc.amplada_Pantalla - bolesD.amplada_ball))
            juga2.score2 += 1
        if juga1.kame1_rect.colliderect(bolesD.ballD_rect) and (juga1.acabat1 == False) :
            bolesD.ball_y = 0
            bolesD.ball_x = random.randrange(0, int(joc.amplada_Pantalla - bolesD.amplada_ball))
            #juga1.life1 -= 1
            if juga1.life1 <= 0 :
                juga1.acabat1 = True
                if juga2.life2 <= 0 :
                    final = joc.game_over(juga1, juga2, joc, img, txt)
                    time.sleep(4)
        if juga2.kame2_rect.colliderect(bolesD.ballD_rect) and (juga2.acabat2 == False) :
            bolesD.ball_y = 0
            bolesD.ball_x = random.randrange(0, int(joc.amplada_Pantalla - bolesD.amplada_ball))
            #juga2.life2 -= 1 
            if juga2.life2 <= 0 :
                juga2.acabat2 = True
                if juga1.life1 <= 0 :
                    final = joc.game_over(juga1, juga2, joc, img, txt)
                    time.sleep(4)
        if bolesD.ball_y > (joc.alsada_Pantalla - 2*bolesD.alsada_ball) :
            bolesD.ball_y = 0
            bolesD.ball_x = random.randrange(0, int(joc.amplada_Pantalla - bolesD.amplada_ball))
            juga1.life1 -= 1
            if juga1.life1 <= 0 :
                juga1.acabat1 = True
                if juga2.life2 <= 0 :
                    final = joc.game_over(juga1, juga2, joc, img, txt)
                    time.sleep(4)
            juga2.life2 -= 1
            if juga2.life2 <= 0 :
                juga2.acabat2 = True
                if juga1.life1 <= 0 :
                    final = joc.game_over(juga1, juga2, joc, img, txt)
                    time.sleep(4)
        if juga1.kame1_rect.colliderect(enem1.enemic1_rect) and (juga1.acabat1 == False) :
            enem1.e1_x = random.randrange(0, int(joc.amplada_Pantalla - enem1.amplada_enemic))
            juga1.score1 += 2
        if juga2.kame2_rect.colliderect(enem1.enemic1_rect) and (juga2.acabat2 == False) :
            enem1.e1_x = random.randrange(0, int(joc.amplada_Pantalla - enem1.amplada_enemic))
            juga2.score2 += 2
        if pro1.pro1_y > (joc.alsada_Pantalla - 2*pro1.alsada_project) :
            pro1.pro1_y = enem1.alsada_enemic/2
            pro1.pro1_x = enem1.e1_x 
        if juga1.kame1_rect.colliderect(pro1.project1_rect) :
            pro1.pro1_y = enem1.alsada_enemic/2
            pro1.pro1_x = enem1.e1_x 
        if juga2.kame2_rect.colliderect(pro1.project1_rect) :
            pro1.pro1_y = enem1.alsada_enemic/2
            pro1.pro1_x = enem1.e1_x            
        if pro1.project1_rect.colliderect(juga1.juga1_rect) and (juga1.acabat1 == False) :
            pro1.pro1_y = enem1.alsada_enemic/2
            pro1.pro1_x = enem1.e1_x
            juga1.life1 -= 1
            if juga1.life1 <= 0 :
                juga1.acabat1 = True
                if juga2.life2 <= 0 :
                    final = joc.game_over(juga1, juga2, joc, img, txt)
                    time.sleep(4)
        if pro1.project1_rect.colliderect(juga2.juga2_rect) and (juga2.acabat2 == False) :
            pro1.pro1_y = enem1.alsada_enemic/2
            pro1.pro1_x = enem1.e1_x        
            juga2.life2 -= 1
            if juga2.life2 <= 0 :
                juga2.acabat2 = True
                if juga1.life1 <= 0 :
                    final = joc.game_over(juga1, juga2, joc, img, txt)
                    time.sleep(4)    
        """ càlcul de la coalisió amb l'enemic 1"""
        if juga1.kame1_rect.colliderect(enem2.enemic2_rect) :
            enem2.e2_x = random.randrange(0, int(joc.amplada_Pantalla - enem2.amplada_enemic))
            juga2.score2 += 2
        if juga2.kame2_rect.colliderect(enem2.enemic2_rect) :
            enem2.e2_x = random.randrange(0, int(joc.amplada_Pantalla - enem2.amplada_enemic))
            juga2.score2 += 2
        if pro2.pro2_y > (joc.alsada_Pantalla - 2*pro2.alsada_project) :
            pro2.pro2_y = enem2.alsada_enemic/2
            pro2.pro2_x = enem2.e2_x 
        if juga1.kame1_rect.colliderect(pro2.project2_rect) :
            pro2.pro2_y = enem2.alsada_enemic/2
            pro2.pro2_x = enem2.e2_x 
        if juga2.kame2_rect.colliderect(pro2.project2_rect) :
            pro2.pro2_y = enem2.alsada_enemic/2
            pro2.pro2_x = enem2.e2_x            
        if pro2.project2_rect.colliderect(juga1.juga1_rect) and (juga1.acabat1 == False) :
            pro2.pro2_y = enem2.alsada_enemic/2
            pro2.pro2_x = enem2.e2_x
            juga1.life1 -= 1
            if juga1.life1 <= 0 :
                juga1.acabat1 = True
                if juga2.life2 <= 0 :
                    final = joc.game_over(juga1, juga2, joc, img, txt)
                    time.sleep(4)
        if pro2.project2_rect.colliderect(juga2.juga2_rect) and (juga2.acabat2 == False) :
            pro2.pro2_y = enem2.alsada_enemic/2
            pro2.pro2_x = enem2.e2_x        
            juga2.life2 -= 1
            if juga2.life2 <= 0 :
                juga2.acabat2 = True
                if juga1.life1 <= 0 :
                    final = joc.game_over(juga1, juga2, joc, img, txt)
                    time.sleep(4)        
        """ condicional en augment de puntuació i decrement de vides """
        if (juga1.score1+juga2.score2) > 9 and (juga1.score1+juga2.score2 < 20)  :
            joc.level = 2
            img.juga2dreta = img.songohanr
            img.juga2esque = img.songohan
            img.juga1dreta = img.Trunks
            img.juga1esque = img.Trunksr
            bolesD.boles_speed = 7
        if (juga1.score1+juga2.score2) > 19 and (juga1.score1+juga2.score2 < 40)  :
            joc.level = 3
            img.Fons = img.Fons_n3
            img.ball = img.ball4
        if (juga1.score1+juga2.score2) > 39 and (juga1.score1+juga2.score2 < 60)  :
            joc.level = 4
            img.juga2dreta = img.goku7r
            img.juga2esque = img.goku7
            img.juga1dreta = img.Vegeta
            img.juga1esque = img.Vegetar
            bolesD.boles_speed = 8
            enem1.enemic1 = img.buu
            enem2.enemic2 = img.Artwork
        if (juga1.score1+juga2.score2) > 59 and (juga1.score1+juga2.score2 < 80)  :
            joc.level = 5
            img.Fons = img.Fons_n5
            img.ball = img.ballZ
            bolesD.boles_speed = 9
            enem2.enemic2 = img.frizer
        if (juga1.score1+juga2.score2) > 79 and (juga1.score1+juga2.score2 < 100)  :
            joc.level = 6
            img.juga2dreta = img.goku4r
            img.juga2esque = img.goku4
            img.juga1dreta = img.Vegeta1r
            img.juga1esque = img.Vegeta1
            bolesD.boles_speed = 10
            enem1.enemic1 = img.atomix
        if juga1.score1+juga2.score2 > 99  :
            joc.level = 7
            img.Fons = img.Fons_n7
            enem2.enemic2 = img.Artwork
            bolesD.boles_speed = 11
        """ canvis de personatges i fons de paisstges quan augmentem el nivell """            
        if juga1.j1_x > joc.amplada_Pantalla- joc.amplada_jugador :
            juga1.j1_x = 0
        if juga2.j2_x > joc.amplada_Pantalla- joc.amplada_jugador :
            juga2.j2_x = 0
        if juga1.j1_x < 0 :
            juga1.j1_x = joc.amplada_Pantalla - joc.amplada_jugador
        if juga2.j2_x < 0 :
            juga2.j2_x = joc.amplada_Pantalla - joc.amplada_jugador
        """ condicions de reposicionaments dels jugadors fora de límits """ 
        return final
    """ acabar tot el procés de lògica d'execucions """       
    def visualPantalla (self, juga1, juga2, joc, img, bolesD, enem1, pro1, enem2, pro2) :
        """
        crearem el mètode per la visualtizatció de les continues modificacions dels objectes del joc
        """
        self.tipografia = pygame.font.SysFont("serif", joc.marca_txt)
        self.marcador2 = self.tipografia.render("Score:{} life:{} ||L.:".format(juga2.score2, juga2.life2),1,(222, 62, 62))
        self.marcador1 = self.tipografia.render("{}|| life:{} Score:{}".format(joc.level, juga1.life1, juga1.score1),1,(62, 62, 222))
        joc.pantalla.blit(img.Fons, (0, 0))
        joc.pantalla.blit(self.marcador2, (0, 10))
        joc.pantalla.blit(self.marcador1, (joc.amplada_Pantalla/2, 10))
        if juga1.acabat1 == False :
            joc.pantalla.blit(juga1.guerrer1, (juga1.j1_x, juga1.j1_y))
            joc.pantalla.blit(img.kame1, (juga1.ka1_x, juga1.ka1_y))
        if juga2.acabat2 == False :
            joc.pantalla.blit(juga2.guerrer2, (juga2.j2_x, juga2.j2_y))
            joc.pantalla.blit(img.kame2, (juga2.ka2_x, juga2.ka2_y))
        joc.pantalla.blit(img.ball, (bolesD.ball_x, bolesD.ball_y))
        if (joc.level > 1) and ((juga1.score1+juga2.score2)%3 != 0) :
            if enem1.e1Amagat == False :
                enem1.e1_x = random.randrange(0, int(joc.amplada_Pantalla - enem1.amplada_enemic))
                enem1.e1Amagat = True
            joc.pantalla.blit(enem1.enemic1, (enem1.e1_x, enem1.e1_y))
        else :
            enem1.e1Amagat = False
        if (joc.level > 2) and ((juga1.score1+juga2.score2)%3 != 0) :
            joc.pantalla.blit(img.kame0, (pro1.pro1_x, pro1.pro1_y))
        else :
            pro1.pro1_y = enem1.e1_y
            pro1.pro1_x = enem1.e1_x
        if (joc.level > 3) and ((juga1.score1+juga2.score2+1)%3 != 0) :
            if enem2.e2Amagat == False :
                enem2.e2_x = random.randrange(0, int(joc.amplada_Pantalla - enem2.amplada_enemic))
                enem2.e2Amagat = True
            joc.pantalla.blit(enem2.enemic2, (enem2.e2_x, enem2.e2_y))
            joc.pantalla.blit(img.ball_F, (pro2.pro2_x, pro2.pro2_y))
        else :
            enem2.e2Amagat = False
            pro2.pro2_y = enem2.e2_y
            pro2.pro2_x = enem2.e2_x
            
        pygame.display.flip()
        """ final de la càrrega de la pantalla del joc """
# -----------------------------------------------------------------------------------------------------------------------
#    ------------------------------------------------ mètodes per la llista del millors registres -----------------------
#   --------------------------------------------------------------------------------------------------------------------- 
    def connecSQL (self) :
        """
        crearem una mètode per fer una connexió a una BBDD i poder extreure els
        resultats per pantalla de pygame
        """
        cont = []
        nom = ""
        punt = ""
        naci = ""
        self.connexio = sqlite3.connect("DragonBall.db")
        self.cursor = self.connexio.cursor()
        self.cursor.execute("SELECT id, pseudonim, nivell, email, nacionalitat, puntuacio FROM RegistreDragon ORDER BY puntuacio DESC")
        registres = self.cursor.fetchall()
        for registre in registres :
            nom = registre[1]
            naci = registre[4]
            punt = registre[5]
            cont += " ",nom," ",naci," ",punt          
        self.connexio.close()
        return cont
    def evensRanking (self, reg) :
        """
        crearem una funció per els esdeveniment de la pantalla de rankings
        """
        for esdev in pygame.event.get() :
            if esdev.type == pygame.QUIT :
                reg = True
            elif esdev.type == pygame.KEYDOWN :
                if esdev.key == pygame.K_ESCAPE :
                    reg = True
        return reg
    def visualRank (self, joc, container, img) :
        """
        crearem una funció per visualitzar els millor registres per pantalla
        """
        joc.pantalla.fill(joc.color_scr)
        self.tipografia = pygame.font.SysFont("serif", joc.mida_txt)
        self.tipografia2 = pygame.font.SysFont("serif", int(joc.mida_txt/2))
        self.linia1 = self.tipografia.render("THE BEST SCORE HERE", 1, (21, 21, 212))
        self.linia2 = self.tipografia2.render("1. {} ({}): {}".format(container[1],container[3],container[5]),1,(21, 21, 21))
        self.linia3 = self.tipografia2.render("2. {} ({}): {}".format(container[7],container[9],container[11]),1,(21, 21, 21))
        self.linia4 = self.tipografia2.render("3. {} ({}): {}".format(container[13],container[15],container[17]),1,(21, 21, 21))
        self.linia5 = self.tipografia2.render("4. {} ({}): {}".format(container[19],container[21],container[23]),1,(21, 21, 21))
        self.linia6 = self.tipografia2.render("5. {} ({}): {}".format(container[25],container[27],container[29]),1,(21, 21, 21))
        self.linia7 = self.tipografia2.render("6. {} ({}): {}".format(container[31],container[33],container[35]),1,(21, 21, 21))
        self.linia8 = self.tipografia2.render("7. {} ({}): {}".format(container[37],container[39],container[41]),1,(21, 21, 21))
        self.linia9 = self.tipografia2.render("8. {} ({}): {}".format(container[43],container[45],container[47]),1,(21, 21, 21))
        self.linia10 = self.tipografia2.render("9. {} ({}): {}".format(container[49],container[51],container[53]),1,(21, 21, 21))
        joc.pantalla.blit(img.goku8, (int(joc.amplada_Pantalla/2), int(joc.alsada_Pantalla/2)))
        joc.pantalla.blit(self.linia1, (joc.amplada_Pantalla/10, 10))
        joc.pantalla.blit(self.linia2, (joc.amplada_Pantalla/10, joc.alsada_Pantalla/10))
        joc.pantalla.blit(self.linia3, (joc.amplada_Pantalla/10, joc.alsada_Pantalla*2/10))
        joc.pantalla.blit(self.linia4, (joc.amplada_Pantalla/10, joc.alsada_Pantalla*3/10)) 
        joc.pantalla.blit(self.linia5, (joc.amplada_Pantalla/10, joc.alsada_Pantalla*4/10))
        joc.pantalla.blit(self.linia6, (joc.amplada_Pantalla/10, joc.alsada_Pantalla*5/10))
        joc.pantalla.blit(self.linia7, (joc.amplada_Pantalla/10, joc.alsada_Pantalla*6/10))
        joc.pantalla.blit(self.linia8, (joc.amplada_Pantalla/10, joc.alsada_Pantalla*7/10)) 
        joc.pantalla.blit(self.linia9, (joc.amplada_Pantalla/10, joc.alsada_Pantalla*8/10))
        joc.pantalla.blit(self.linia10, (joc.amplada_Pantalla/10, joc.alsada_Pantalla*9/10))
        pygame.display.flip()
# -----------------------------------------------------------------------------------------------------------------------
#    ------------------------------------------- mètodes per la portada iteractiva --------------------------------------
#   --------------------------------------------------------------------------------------------------------------------- 
    def evensMenu (self, reg, fer, sortir, inserir, txt, joc, juga1, juga2, img, bolesD, enem1, pro1, enem2, pro2) :
        """
        crearem els esdeveniments per la portada iteractiva
        """
        container = []
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                fer = True 
                """ en cas de sortir del programa """
            elif event.type == pygame.KEYDOWN :
                if event.key == pygame.K_ESCAPE :
                    fer = True 
                    """ sortida del programa en la tecla abortar """
                if event.key == 112 :
                    juga1.acabat1 = not juga1.acabat1
                    if juga1.acabat1 == True :
                        txt.color_txt1 = (212, 12, 12)
                    else:
                        txt.color_txt1 = (12, 12, 12)
                """ elecció d'un o dos jugadors en la partida """
                if event.key == 107 :
                    txt.color_txt2 = (212, 12, 12)
                    inserir = False
                if event.key == 103 :
                    juga1.score1, juga2.score2, juga1.life1, juga2.life2, joc.level = 0, 0, 3, 3, 1
                    juga1.guerrer1, juga2.guerrer2, img.ball, img.Fons, enem1.enemic1 = img.a16, img.goku, img.ballD, img.Fons_n1, img.atomix
                    img.juga1dreta, img.juga1esque, img.juga2dreta, img.juga2esque = img.a16r, img.a16, img.goku, img.gokur
                    juga1.j1_x = joc.amplada_Pantalla*2/3
                    juga2.j2_x = joc.amplada_Pantalla/3
                    pygame.mixer.music.load("BolaDracZ.mp3")
                    pygame.mixer.music.set_volume(1)
                    pygame.mixer.music.play (-1)
                    """ cançó de bola de drac Z"""
                    sortir = False                    
                if event.key == 282 :
                    joc.amplada_Pantalla = 950
                    joc.alsada_Pantalla = 690
                    joc.modiMides()
                    juga1.actualJuga(joc)
                    juga2.actualJuga(joc)
                    bolesD.actualBole(joc)
                    enem1.actualJuga(joc)
                    pro1.actualProj(joc, enem1)
                    enem2.actualJuga(joc)
                    pro2.actualProj(joc, enem2)
                    img.actualImg(joc, juga1, juga2, bolesD, enem1, pro1, enem2, pro2)
                if event.key == 283 :
                    joc.amplada_Pantalla = 730
                    joc.alsada_Pantalla = 530
                    joc.modiMides()
                    juga1.actualJuga(joc)
                    juga2.actualJuga(joc)
                    bolesD.actualBole(joc)
                    enem1.actualJuga(joc)
                    pro1.actualProj(joc, enem1)
                    enem2.actualJuga(joc)
                    pro2.actualProj(joc, enem2)
                    img.actualImg(joc, juga1, juga2, bolesD, enem1, pro1, enem2, pro2)
                if event.key == 284 :
                    joc.amplada_Pantalla = 550
                    joc.alsada_Pantalla = 400
                    joc.modiMides()
                    juga1.actualJuga(joc)
                    juga2.actualJuga(joc)
                    bolesD.actualBole(joc)
                    enem1.actualJuga(joc)
                    pro1.actualProj(joc, enem1)
                    enem2.actualJuga(joc)
                    pro2.actualProj(joc, enem2)
                    img.actualImg(joc, juga1, juga2, bolesD, enem1, pro1, enem2, pro2)
                if event.key == 114 :
                    txt.color_txt4 = (212, 12, 12)
                    container = joc.connecSQL() 
                    reg = False
                    time.sleep(0.5)                     
        if (joc.amplada_Pantalla/2 + joc.amplada_Pantalla/10 > mouse[0] > joc.amplada_Pantalla/10) and (joc.alsada_Pantalla*8/10 + joc.mida_txt > mouse[1] > joc.alsada_Pantalla*8/10) :
            txt.color_txt5 = (212, 12, 12)
            if click[0] == 1 :                    
                juga1.score1, juga2.score2, juga1.life1, juga2.life2, joc.level = 0, 0, 3, 3, 1
                juga1.guerrer1, juga2.guerrer2, img.ball, img.Fons, enem1.enemic1, enem2.enemic2 = img.a16, img.goku, img.ballD, img.Fons_n1, img.atomix, img.frizer
                img.juga1dreta, img.juga1esque, img.juga2dreta, img.juga2esque = img.a16r, img.a16, img.goku, img.gokur
                juga1.j1_x = joc.amplada_Pantalla*2/3
                juga2.j2_x = joc.amplada_Pantalla/3
                pygame.mixer.music.load("BolaDracZ.mp3")
                pygame.mixer.music.set_volume(1)
                pygame.mixer.music.play (-1)
                """ cançó de bola de drac Z"""
                sortir = False
        elif (joc.amplada_Pantalla/2 + joc.amplada_Pantalla/10 > mouse[0] > joc.amplada_Pantalla/10) and (joc.alsada_Pantalla*6/10 + joc.mida_txt > mouse[1] > joc.alsada_Pantalla*6/10) :
            txt.color_txt4 = (212, 12, 12)
            if click[0] == 1 :
                container = joc.connecSQL()
                reg = False
        elif (joc.amplada_Pantalla/2 + joc.amplada_Pantalla/10 > mouse[0] > joc.amplada_Pantalla/10) and (joc.alsada_Pantalla*4/10 + joc.mida_txt > mouse[1] > joc.alsada_Pantalla*4/10) :
            txt.color_txt3 = (212, 12, 12)
            
        elif (joc.amplada_Pantalla/2 + joc.amplada_Pantalla/10 > mouse[0] > joc.amplada_Pantalla/10) and (joc.alsada_Pantalla*2/10 + joc.mida_txt > mouse[1] > joc.alsada_Pantalla*2/10) :
            txt.color_txt2 = (212, 12, 12)
            if click[0] == 1 :
                inserir = False
        elif (joc.amplada_Pantalla/2 + joc.amplada_Pantalla/10 > mouse[0] > joc.amplada_Pantalla/10) and (10 + joc.mida_txt > mouse[1] > 10) :
            if click[0] == 1 :
                juga1.acabat1 = not juga1.acabat1
                if juga1.acabat1 == True :
                    txt.color_txt1 = (212, 12, 12)
                else:
                    txt.color_txt1 = (12, 12, 12)  
        else :
            txt.color_txt5, txt.color_txt4, txt.color_txt3, txt.color_txt2 = (12, 12, 12), (12, 12, 12), (12, 12, 12), (12, 12, 12)
            """ en cas d'entrar en la primera fase del joc """
        return reg, fer, sortir,inserir, container        
    def visualMenu (self, txt, joc, img) :
        """
        crearem el mètode de visualització de la portada interactiva
        """
        joc.pantalla.fill(joc.color_scr)
        self.tipografia = pygame.font.SysFont("serif", joc.mida_txt)
        self.opcio1 = self.tipografia.render("PLAYERS:[1 only]", 1, txt.color_txt1)
        self.opcio2 = self.tipografia.render("KEY NEW REGISTRE", 1, txt.color_txt2)
        self.opcio3 = self.tipografia.render("OPTIONS CONFING", 1, txt.color_txt3)
        self.opcio4 = self.tipografia.render("RANKING PLAYERS", 1, txt.color_txt4)
        self.opcio5 = self.tipografia.render("GAMMING...", 1, txt.color_txt5)
        """
        crearem tots els objectes de la portada interectiva incloent el fons de pantalla
        """
        joc.pantalla.blit(img.goku2, (0,0))
        joc.pantalla.blit(self.opcio1, (joc.amplada_Pantalla/10, 10))      
        joc.pantalla.blit(self.opcio2, (joc.amplada_Pantalla/10, joc.alsada_Pantalla*2/10))
        joc.pantalla.blit(self.opcio3, (joc.amplada_Pantalla/10, joc.alsada_Pantalla*4/10))
        joc.pantalla.blit(self.opcio4, (joc.amplada_Pantalla/10, joc.alsada_Pantalla*6/10))
        joc.pantalla.blit(self.opcio5, (joc.amplada_Pantalla/10, joc.alsada_Pantalla*8/10))
        pygame.display.flip()
        """
        sortida de tots els objectes per la finestre pygame "portada iteractiva
        """
#    -----------------------------------------------------------------------------------------------------------
#    ------------------------------------------- mètodes per la inserció d'un registe --------------------------
#   ------------------------------------------------------------------------------------------------------------         
    def evensRegister (self, inserir, text1) :
        """ crearem un mètode d'esdeveniment per la pantalla d'inserció de registres a la BBDD """
        for esdev in pygame.event.get() :
            if esdev.type == pygame.QUIT :
                inserir = True
                text1.color_txt2 = (12, 12, 12)
            elif esdev.type == pygame.KEYDOWN :
                if esdev.key == pygame.K_ESCAPE :
                    inserir = True
                    text1.color_txt2 = (12, 12, 12)
        return inserir
    def visualRegister (self, txt, joc, img, jugador2) :
        """ crearem el mètode per visualitzar el camps del nostre nou registre """
        #joc.pantalla.fill(joc.color_scr)
        formAuxiliar(joc, jugador2)
        return True
        #pygame.display.flip()
"""-------------------------------------------------------------------------------------------------------------------
   ------------------------------------------------------ Funcions principal main ------------------------------------
   -------------------------------------------------------------------------------------------------------------------
"""
def main():
    """
    Funció principal del programa.
    """
    pygame.init() 
    """ inicialització de la pantalla del joc """
    pygame.display.set_caption("Bola de Drac Z")
    """ rètol de la finestra """
    container = []
    acabar, sortir, rank, inserir, pause = False, True, True, True, True
    segons = pygame.time.Clock()
    joc = Joc()
    joc.modiMides()
    """ Crearem una instància de la classe Joc """ 
    text1 = Text1 ()
    jugador1 = Jugador1 (joc)
    jugador2 = Jugador2 (joc)
    bolesD = Bolesdrac (joc)
    enemic1 = Enemic1 (joc)
    projectil1 = EnemicPro1(joc, enemic1)
    enemic2 = Enemic2 (joc)
    projectil2 = EnemicPro2(joc, enemic2)
    img = carregaImg (joc, jugador1, jugador2, bolesD, enemic1, projectil1, enemic2, projectil2)
    """
    crearem una instància per cada classe
    """
    while not acabar: 
        """ Bucle principal metres el boolean sigui False sortirà portada iteractiva"""               
        while not sortir: 
            """ Bucle aniuat mentres sortir sigui False sortirà video joc"""             
            sortir, pause = joc.procesEvents(jugador1, jugador2, joc, img)
            """ crida del mètode d'entrada d'esdeveniment per entrades """
            if sortir == True :
                continue
            while not pause :
                pause = joc.paused(pause, joc)
                """ crida el mèdode paused per parar el joc """
                if pause == True :
                    pygame.mixer.music.unpause()
                pygame.display.update()
                segons.tick(60)
                """ farem 60 cops en un segon el bucle d'esdeveniments """
            sortir = joc.logicaExecutar(jugador1, jugador2, joc, img, bolesD, text1, enemic1, projectil1, enemic2, projectil2)
            """ crida del mètode per les noves posiciones dels objets i
             ens comprobarà les coal·lissions """
            joc.visualPantalla(jugador1, jugador2, joc, img, bolesD, enemic1, projectil1, enemic2, projectil2)
            """ Dibuixar el moment actual per observar tots els canvis """
            pygame.display.update()
            segons.tick(60) 
            """ farem 60 cop en un segon el bucle d'esdeveniments """
        while not rank:
            """ bucle on visualitzem els registres de la basse de dades"""
            rank = joc.evensRanking(rank)
            """ crida el mètode d'esdeveniment per la pantalla ranking"""
            joc.visualRank(joc, container, img)
            """ funció per visualitzar el ranking de registres per pantalla"""
            pygame.display.update()
            segons.tick(60)
            """ farem 60 cops en un segon el bucle d'esdeveniments """
        while not inserir :
            """bucle on innsertirem els camps del nou registre """
            inserir = joc.evensRegister(inserir, text1)
            """ mètode per controlar les entrades de caràcters d'entrada """
            inserir = joc.visualRegister(text1, joc, img, jugador2)
            """ mètode on serà visibilitats els textes en la pantalla creada """
            pygame.display.update()
            segons.tick(60)
            """ farem 60 cops en un segon el bucle d'esdeveniments """
        text1.color_txt2, text1.color_txt4, text1.color_txt5 = (12, 12, 12), (12, 12, 12), (12, 12, 12)
        """ color negre per el botó Gamming """
        rank, acabar, sortir, inserir, container = joc.evensMenu(rank, acabar, sortir, inserir, text1, joc, jugador1, jugador2, img, bolesD, enemic1, projectil1, enemic2, projectil2)
        """crida de la funció d'esdeveniments per la portada iteractiva """
        joc.visualMenu(text1, joc, img)           
        """  visualització del menú amb totes les seves opcions """
        time.sleep(0.5)
        """ temps d'espera mig segon """
        pygame.display.update() 
        segons.tick(60)
        """ farem 60 cop en un segon els bucle de la pantalla """
    """
    carregarem el menu principal del joc per escollir opcions d'una nova partida
    """          
    pygame.quit() 
    """ tancarem i sortirem de la finestre pygame """
    quit() 
    """ sortirem de python 3.7 """ 
"""--------------------------------------------------------------------------------------------------------------------
   ------------------------------------------- Funcions de formularis per pantalla ------------------------------------
   --------------------------------------------------------------------------------------------------------------------
"""
#-------------------------------------------- connexió amb SQL i insertem un nou registre
def connecSQLIn(pseudonim, nivell, email, nacionalitat, puntuacio) :
    connexio = sqlite3.connect("DragonBall.db")
    cursor = connexio.cursor()
    arxiu = [(pseudonim, nivell, email, nacionalitat, puntuacio)]
    #print ("arx:", arxiu)
    cursor.executemany("INSERT INTO RegistreDragon VALUES (NULL,?,?,?,?,?)",arxiu)
    connexio.commit()
    connexio.close()
#----------------------------  funció d'extreure el formulari per pantalla
def formAuxiliar (joc, jugador2) :
#------------------- MULTIUSER BOX
    title = "Introduir nou registre"
    fieldNames = ["Nom","Pais", "Mail"]
    fieldValues = [""] * len(fieldNames)
    #print (len(fieldValues), type(fieldValues))
    surtok = fes_bucle(joc, jugador2, fieldNames, fieldValues, title, "Introdueixi les dades")
    if surtok == True:
        print ("grava dades", fieldValues)
#---------------------- BUCLE D'ACEPTACIO DE DADES FINS QUE ESTIGUIN OK
def fes_bucle (joc, jugador2, fieldNames, fieldValues, title, errores_msg):   
    
    validOK = False
    
    while validOK == False :
        #---------------------- Abre ventana
        fieldValues = multenterbox(errores_msg,title, fieldNames, fieldValues)
    
        #---------------------- Han cancelado
        if fieldValues == None:
            return False
        else :
            errores_msg = ""
            #---------------------- Hace validaciones para cada campo
            for i in range(len(fieldNames)):
              if fieldValues[i].strip() == "":
                 errores_msg += ('"%s" camp obligatori\n\n' % fieldNames[i])
            
            #-----------------------------end for
            if errores_msg == "": 
                validOK = True
    #------------------------------------------- end while
    nivell = joc.level
    puntuacio = jugador2.score2
    #print ("Dades entrades:", fieldValues)
    connecSQLIn(fieldValues[0], nivell, fieldValues[2], fieldValues[1], puntuacio)
    return True


"""----------------------------------------------------------------------------------------------------------------------
    ------------------------------------------------------------ inci de l'execució -------------------------------------
    ---------------------------------------------------------------------------------------------------------------------
"""
if __name__ == "__main__":
    """ 
    Crida de la funció principal i començarem el joc 
    """     
    main() 
    """ funció principal main() """