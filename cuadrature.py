#!/usr/bin/env python3

"""
Cálculo de integrales mediante cuadratura Gaussiana.

Aqui se implementa el método de cuadratura Gaussiana con polinomios de Legendre para aproximar integrales definidas
"""

import numpy as np
import matplotlib.pyplot as plt

def gaussxw(N):
    """Calcula los puntos y pesos para la cuadratura de Gauss-Legendre.

    Utiliza numpy para calcular los polinomios de legendre

    Args:
        N (int): Número de subregiones

    Returns:
        tuple: (x, w) donde:
            x : ndarray
                Puntos de muestreo en [-1, 1]
            w : ndarray 
                Pesos correspondientes a los puntos
    """
    x,w= np.polynomial.legendre.leggauss(N)

    return x,w

def gaussxwab(a, b, x, w):
    """Escala puntos de muestreo y pesos al intervalo [a, b].

    Transforma los puntos del intervalo [-1, 1]
    al intervalo de integración deseado [a, b].

    Args:
        a (float): Límite inferior de la integral
        b (float): Límite superior de la integral
        x (ndarray): los puntos de muestreo sin escalar
        w (ndarray): Pesos correspondientes sin escalar

    Returns:
        tuple (x_k, w_k): los valores escalados a nuestro intervalo de integracion
    """
    return 0.5*(b-a)*x + 0.5*(b+a), 0.5*(b-a)*w

def func(x):
    """Función a integrar: sin(x²).

    Args:
        x (ndarray o float): Punto(s) donde evaluar la función

    Returns:
        (ndarray o float): Valores de la función evaluada en ese punto

    Nota:
        Esta función puede modificarse para implementar otros integrandos.
    """
    return np.sin(x**2)

def sumatoria(x_k, w_k, func):
    """Calcula la aproximación de la integral mediante sumatoria ponderada.

    Args:
        x_k (ndarray): Puntos de muestreo escalados
        w_k (ndarray): Pesos escalados
        func (callable): Función a integrar

    Returns:
        (float): Aproximación numérica de la integral

    """
    return np.sum(w_k * func(x_k))

# =============================================================================
# Configuración principal
# =============================================================================
a, b = 0, np.pi  # Límites de integración
N_values = range(1, 21)  # Rango de puntos a evaluar
results = []  # Almacenará resultados para cada N

# =============================================================================
# Cálculo de la integral para diferentes N
# =============================================================================
for n in N_values:
    x, w = gaussxw(n)
    x_k, w_k = gaussxwab(a, b, x, w)
    results.append(sumatoria(x_k, w_k, func))

# Resultados destacados
print(f"Resultado con N=5: {results[4]:.8f}")
print(f"Resultado con N=20: {results[-1]:.8f}")

# =============================================================================
# Visualización de resultados
# =============================================================================
plt.figure(figsize=(10, 6), dpi=100)
plt.plot(N_values, results, 'o-', color='#1f77b4', markersize=8, linewidth=2)
plt.xlabel("Número de puntos (N)", fontsize=12, labelpad=10)
plt.ylabel("Valor de la integral", fontsize=12, labelpad=10)
plt.title(r"Convergencia de $\int_0^\pi \sin(x^2)\,dx$", 
         fontsize=14, pad=20)

# Línea de referencia para el valor más preciso
plt.axhline(y=results[-1], color='red', linestyle='--', alpha=0.7,
           label=f'N=20: {results[-1]:.8f}')

# Configuración estética
plt.grid(True, linestyle=':', alpha=0.7)
plt.legend(fontsize=10, framealpha=0.9)
plt.tight_layout()

# Guardar y mostrar
plt.savefig('convergencia_gaussiana.png', bbox_inches='tight')
plt.show()
