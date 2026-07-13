# Rúbrica Lab 2

## Distribución

| Componente | Puntos | Calificacion |
|---|---:|---|
| Particiones y escalamiento | 1.5 | Autograded |
| Ridge/Lasso y validación | 3.0 | Autograded |
| Modelo Bernoulli y regresión logística | 2.0 | Autograded |
| Métricas, error estándar, umbral y protocolo | 2.0 | Autograded |
| Recomendación técnica | 1.5 | Manual |

## Revisión manual

Pregunta:

> ¿Qué modelo o umbral recomendarías, qué cantidad poblacional intenta estimar la métrica y qué incertidumbre comunicarías antes de usarlo?

| Puntaje manual | Criterio |
|---:|---|
| 0.0 | No hay una recomendación técnica clara |
| 0.75 | Hay una recomendación, pero los resultados citados son incompletos o no menciona limitaciones |
| 1.5 | La recomendación usa métrica y comparación, distingue probabilidad estimada de verdadera y comunica incertidumbre y alcance |

## Señales de alerta

- Escalamiento ajustado con todo el dataset.
- Hiperparámetro escogido con prueba o solo con entrenamiento.
- Umbral elegido sin relación con precision/recall.
- Recomendación sin contexto de uso.
- Métricas reportadas sin declarar la clase positiva.

La revisión asistida por IA se concentra en la recomendación, sus resultados y
sus límites. El profesor aprueba cada nivel; la IA no vuelve a calificar las
pruebas de código. Tiempo objetivo: 30-45 segundos en casos normales y hasta dos
minutos en casos marcados.
