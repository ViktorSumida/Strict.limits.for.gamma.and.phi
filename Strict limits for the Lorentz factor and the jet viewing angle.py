#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 12:50:34 2021

@author: Viktor Sumida
"""

#import scipy.integrate as integrate
#import scipy.special as special
import numpy as np
#import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as patches
#import math


##############################################################################################################
################################## Desenhando retângulo  #####################################################
##############################################################################################################

fig = plt.figure()
visivel = fig.add_subplot(111)
rect1 = patches.Rectangle((5, 3), 30, 10, alpha=0.8, color='xkcd:gray')
rect2 = patches.Rectangle((5, 3), 30, 10, color='xkcd:black', fill=0, linewidth=2)
visivel.add_patch(rect1)
visivel.add_patch(rect2)


##############################################################################################################
#################################### Desenhando círculo  #####################################################
##############################################################################################################

def create_circle():
	circle= plt.Circle((5,0), radius= 5, color='black', zorder=10)
	return circle
def show_shape(patch):
	ax=plt.gca()
	ax.add_patch(patch)
	plt.axis('scaled')
if __name__== '__main__':
	c= create_circle()
	show_shape(c)



# Função para cálculo do beta
def beta(lorentz):
    beta_v_c = ((((lorentz**2)-1)/(lorentz**2))**0.5)
    return beta_v_c


##############################################################################################################
###################  Valores para theta fixo  #################################################################
##############################################################################################################

lorentz = np.arange(1, 2500, 0.1)

# para teta = 0.5° = 0.00872665 rad
doppler_teta_ponto_cinco = 1/(lorentz*(1-(beta(lorentz)*np.cos(0.00872665))))
beta_app_teta_ponto_cinco = beta(lorentz) * lorentz * doppler_teta_ponto_cinco * np.sin(0.00872665)

# para teta = 1° = 0.0174533 rad
doppler_teta_um = 1/(lorentz*(1-(beta(lorentz)*np.cos(0.0174533))))
beta_app_teta_um = beta(lorentz) * lorentz * doppler_teta_um * np.sin(0.0174533)

# para teta = 2° = 0.0349066 rad
doppler_teta_dois = 1/(lorentz*(1-(beta(lorentz)*np.cos(0.0349066))))
beta_app_teta_dois = beta(lorentz) * lorentz * doppler_teta_dois * np.sin(0.0349066)

# para teta = 3° = 0.0523599 rad
doppler_teta_tres = 1/(lorentz*(1-(beta(lorentz)*np.cos(0.0523599))))
beta_app_teta_tres = beta(lorentz) * lorentz * doppler_teta_tres * np.sin(0.0523599)

# para teta = 4° = 0.0698132 rad
doppler_teta_quatro = 1/(lorentz*(1-(beta(lorentz)*np.cos(0.0698132))))
beta_app_teta_quatro = beta(lorentz) * lorentz * doppler_teta_quatro * np.sin(0.0698132)

# para teta = 5° = 0.0872665 rad
doppler_teta_cinco = 1/(lorentz*(1-(beta(lorentz)*np.cos(0.0872665))))
beta_app_teta_cinco = beta(lorentz) * lorentz * doppler_teta_cinco * np.sin(0.0872665)

# para teta = 6° = 0.10472 rad
doppler_teta_seis = 1/(lorentz*(1-(beta(lorentz)*np.cos(0.10472))))
beta_app_teta_seis = beta(lorentz) * lorentz * doppler_teta_seis * np.sin(0.10472)

# para teta = 8° = 0.139626 rad
doppler_teta_oito = 1/(lorentz*(1-(beta(lorentz)*np.cos(0.139626))))
beta_app_teta_oito = beta(lorentz) * lorentz * doppler_teta_oito * np.sin(0.139626)

# para teta = 10° = 0.174533 rad
doppler_teta_dez = 1/(lorentz*(1-(beta(lorentz)*np.cos(0.174533))))
beta_app_teta_dez = beta(lorentz) * lorentz * doppler_teta_dez * np.sin(0.174533)

# para teta = 15° = 0.261799 rad
doppler_teta_quinze = 1/(lorentz*(1-(beta(lorentz)*np.cos(0.261799))))
beta_app_teta_quinze = beta(lorentz) * lorentz * doppler_teta_quinze * np.sin(0.261799)

plt.plot(doppler_teta_ponto_cinco, beta_app_teta_ponto_cinco, 'b-', linewidth=0.8)
plt.plot(doppler_teta_um, beta_app_teta_um, 'b-', linewidth=0.8)
plt.plot(doppler_teta_dois, beta_app_teta_dois, 'b-', linewidth=0.8)
plt.text(19, 9.5, '$\u03B8=2°$', fontsize=12)
plt.plot(doppler_teta_tres, beta_app_teta_tres, 'b-', linewidth=0.8)
plt.plot(doppler_teta_quatro, beta_app_teta_quatro, 'b-', linewidth=0.8)
plt.plot(doppler_teta_cinco, beta_app_teta_cinco, 'b-', linewidth=0.8)
plt.plot(doppler_teta_seis, beta_app_teta_seis, 'b-', linewidth=0.8)
plt.plot(doppler_teta_oito, beta_app_teta_oito, 'b-', linewidth=0.8)
plt.plot(doppler_teta_dez, beta_app_teta_dez, 'b-', linewidth=0.8)
plt.plot(doppler_teta_quinze, beta_app_teta_quinze, 'b-', linewidth=0.8)

##############################################################################################################
###################  Valores para fator de lorentz fixo  #####################################################
##############################################################################################################

ang_teta = np.arange(0.0, 3, 0.001)

# para lorentz = 2
doppler_lorentz_dois = 1/(2*(1-(beta(2)*np.cos(ang_teta))))
beta_app_lorentz_dois = beta(2) * 2 * doppler_lorentz_dois * np.sin(ang_teta)

# para lorentz = 4
doppler_lorentz_quatro = 1/(4*(1-(beta(4)*np.cos(ang_teta))))
beta_app_lorentz_quatro = beta(4) * 4 * doppler_lorentz_quatro * np.sin(ang_teta)

# para lorentz = 6
doppler_lorentz_seis = 1/(6*(1-(beta(6)*np.cos(ang_teta))))
beta_app_lorentz_seis = beta(6) * 6 * doppler_lorentz_seis * np.sin(ang_teta)

# para lorentz = 8
doppler_lorentz_oito = 1/(8*(1-(beta(8)*np.cos(ang_teta))))
beta_app_lorentz_oito = beta(8) * 8 * doppler_lorentz_oito * np.sin(ang_teta)

# para lorentz = 10
doppler_lorentz_dez = 1/(10*(1-(beta(10)*np.cos(ang_teta))))
beta_app_lorentz_dez = beta(10) * 10 * doppler_lorentz_dez * np.sin(ang_teta)

# para lorentz = 15
doppler_lorentz_quinze = 1/(15*(1-(beta(15)*np.cos(ang_teta))))
beta_app_lorentz_quinze = beta(15) * 15 * doppler_lorentz_quinze * np.sin(ang_teta)

# para lorentz = 20
doppler_lorentz_vinte = 1/(20*(1-(beta(20)*np.cos(ang_teta))))
beta_app_lorentz_vinte = beta(20) * 20 * doppler_lorentz_vinte * np.sin(ang_teta)

# para lorentz = 30
doppler_lorentz_trinta = 1/(30*(1-(beta(30)*np.cos(ang_teta))))
beta_app_lorentz_trinta = beta(30) * 30 * doppler_lorentz_trinta * np.sin(ang_teta)

# para lorentz = 50
doppler_lorentz_cinq = 1/(50*(1-(beta(50)*np.cos(ang_teta))))
beta_app_lorentz_cinq = beta(50) * 50 * doppler_lorentz_cinq * np.sin(ang_teta)

# para lorentz = 100
doppler_lorentz_cem = 1/(100*(1-(beta(100)*np.cos(ang_teta))))
beta_app_lorentz_cem = beta(100) * 100 * doppler_lorentz_cem * np.sin(ang_teta)


plt.plot(doppler_lorentz_dois, beta_app_lorentz_dois, 'r-', linewidth=0.8)
plt.plot(doppler_lorentz_quatro, beta_app_lorentz_quatro, 'r-', linewidth=0.8)
plt.plot(doppler_lorentz_seis, beta_app_lorentz_seis, 'r-', linewidth=0.8)
plt.plot(doppler_lorentz_oito, beta_app_lorentz_oito, 'r-', linewidth=0.8)
plt.text(7.7, 8.5, '$\u03B3=8$', fontsize=12)
plt.plot(doppler_lorentz_dez, beta_app_lorentz_dez, 'r-', linewidth=0.8)
plt.text(7.5, 10.2, '$10$', fontsize=12)
plt.plot(doppler_lorentz_quinze, beta_app_lorentz_quinze, 'r-', linewidth=0.8)
plt.plot(doppler_lorentz_vinte, beta_app_lorentz_vinte, 'r-', linewidth=0.8)
plt.plot(doppler_lorentz_trinta, beta_app_lorentz_trinta, 'r-', linewidth=0.8)
plt.plot(doppler_lorentz_cinq, beta_app_lorentz_cinq, 'r-', linewidth=0.8)
plt.plot(doppler_lorentz_cem, beta_app_lorentz_cem, 'r-', linewidth=0.8)

plt.ylabel('Apparent speed', fontsize=20)
plt.xlabel('Doppler boosting factor', fontsize=20)
plt.xlim(0, 50)
plt.ylim(0, 25)



plt.show()
