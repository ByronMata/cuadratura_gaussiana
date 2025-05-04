## Fundamentos Matemáticos

Para aproximar las integrales por medio de polinomios de legendre se utiliza fundamentalmente la siguiente formula:

\begin{equation}
\int_a^b {\rm{d}}x f(x) \approx \sum_{k=1}^{N} w_k*f(x_k).
\end{equation}

Donde x_k son los puntos de muestreo y w_k los pesos en esos puntos ademas de usar N segmentos de la integral.

En nuestro proceso primero utilizamos una funcion llamada gaussxw que usando la biblioteca de Numpy calcula los puntos de muestreo y pesos en el intervalo [-1,1] en cierta cantidad de N segmentos de la integral.
Como queremos aproximar la integral en un intervalo indiferente tenemos que ajustar esos puntos a nuestros valores para eso se realiza este tipo de ajuste.
Para ajustar los puntos de muestreo se aplica la siguiente formula donde a es el limite inferior de nuestra integral y b el limite superior.
\begin{equation}
x_k=0.5 * (b - a) * x + 0.5 * (b + a)
\end{equation}

Para los pesos ajustados:
\begin{equation}
w_k=0.5 * (b - a) * w
\end{equation}

Ya con los valores ajustados podemos sustituir en la primer formula y obtener una aproximacion de la integral, se puede variar el numero de N segmentos para encontrar una mejor aproximacion.
