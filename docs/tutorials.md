## Ejemplo

Pongamos una integral simple por ejemplo 
\begin{equation}
\int_0^1 x^2 dx
\end{equation}

Se prueba con N=5 en la funcion gaussxw. 
\begin{align}
x, w = gaussxw(5)
\end{align}

Esa funcion devuelve valores de x,w no ajustados por lo tanto enviamos esos valores obtenidos a la funcion gaussxwab para ajustarlos

def gaussxwab(a, b, x, w):
    return 0.5 * (b - a) * x + 0.5 * (b + a), 0.5 * (b - a) * w

Finalmente calculamos el resultado de la aproximacion de la siguiente forma 

def gaussxwab(x_k, w_k, func):
    resultado=wk*func(x_k)
return resultado

Donde func es la funcion escrita en el cuerpo del codigo , a la hora de imprimir el resultado obtendriamos 0.333 para un N=5


