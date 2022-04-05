# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 17:36:31 2022

@author: Asus
"""

import Algoritmosnumericos as Alg
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('dark_background')
datos1=pd.read_csv('datos refraccion angulo incidencia.txt')
datos2=pd.read_csv('datos refraccion angulo reflexion.txt')
datos1=datos1[(datos1['t'] >5.60597 )]
datos2=datos2[(datos2['t'] >5.60597 )]

print('Angúlo incidencia')
print(datos1.to_markdown())
print(' ')
print('Angúlo reflexión')
print(datos2.to_markdown())

fig,ax = plt.subplots(2,1,figsize=(10,10))
ax[0].scatter(datos1['t'],datos1['θ'],label='angulo incidencia')
ax[0].scatter(datos2['t'],datos2['θ'],label='angulo reflexion')
ax[0].set_ylabel('θ')
ax[0].set_xlabel('t')
ax[0].set_title('θ vs t')
y=np.sin(datos2['θ']*(3.14/180)).tolist()
x=np.sin(datos1['θ']*(3.14/180)).tolist()
ajuste=Alg.regresionlineal(x,y)
Alg.dibujo_reglineal(x,y,1,0, 'sin(θ) refl vs sin(θ) inc','sin(θ) inc','sin(θ) refl', ax,'ajuste para la ley de snell')



