# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 08:23:31 2016

@author: bill
"""

#Módulos utilizados
from numpy import *
from scipy import signal


#define ft

a = array([1])  #numerador
b = array([1, 60, 500]) #denominador

#define tempo de amostragem

Ts = 1

#multiplica por 1/s

sizeb = size(b)
b = insert(b, sizeb, 0)

#faz frações parciais

r,p,k = signal.residue(a,b)
# r = coeficientes
# p = polos
# k = Coefficients of the direct polynomial term.?????

#extrai coeficiente de steady state
#extrai coeficiente de dinâmica
#extrai polos

d_s = array([])
d_d = array([])
d_i = array([])
polos = array([])
integrador = 0

for i in range(size(p)):
    if (p[i]==0):
        if (integrador):
            d_i = insert(d_i,size(d_i), r[i])        
        else:
            d_s = insert(d_s, size(d_s), r[i])
            integrador += 1
    else:
        d_d = insert(d_d, size(d_d), r[i])
        polos = insert(polos, size(polos), p[i])

if (size(d_i)==0):
    d_i = insert(d_i,size(d_i), 0) 


#monta matriz A
A_1 = hstack((array([[1]]),zeros((1,2)),array([[Ts]])))  #primeira linha
z_1 = zeros((size(d_d),size(d_s)))
z_2 = zeros((size(d_d),size(d_i)))
A_2 = hstack((z_1,diag(polos,0),z_2)) #segunda linha
A_3 = hstack((zeros((1,size(d_s))), zeros((1,size(d_d))), array([[1]]))) #terceira linha


A = vstack((A_1,A_2,A_3))


#monta matriz B

B_1 = d_s+d_i
B_2 = 


B_3 = d_i
#monta matriz C

#monta sistema ss