# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 21:51:53 2019
@file : setup.py
@description: conversió codi python en un fitxer executable
@author: Gilbert Viader
"""
import cx_Freeze

executables = [cx_Freeze.Executable("DragonBall.py")]

cx_Freeze.setup(
    name="Bola de Drac Z",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":["KameB.png", "ball_1.png", "ball_4.png", "z_ball.png"
    , "a-16.png", "a-16r.png", "Trunks.png", "Trunksr.png","Vegeta.png","Vegetar.png","vegeta1.png","vegeta1r.png"
    ,"piccolo.png","piccolor.png","goku.png","gokur.png","goku7.png","goku7r.png","goku4.png","goku4r.png"
    ,"goten.png","gotenr.png","songohan.png","songohanr.png","goku2.png","goku8.png","nameq.jpg","Namek1.png"
    ,"nameDrag.jpeg","brolyEsc.jpg","goku31.png","Atomix1.png","buu1.png","kame0.png","frieza.png"
    ,"Artwork.png","ball_F.png"]}},
    executables = executables)

