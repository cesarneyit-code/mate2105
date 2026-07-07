# Rubrica Lab 2

## Distribucion

| Componente | Puntos | Calificacion |
|---|---:|---|
| Particiones y escalamiento | 1.5 | Autograded |
| Ridge/Lasso y validacion | 3.0 | Autograded |
| Regresion logistica | 2.0 | Autograded |
| Metricas y umbral | 2.0 | Autograded |
| Recomendacion tecnica | 1.5 | Manual |

## Revision manual

Pregunta:

> Que modelo o umbral recomendarias y que limitacion comunicarias antes de usarlo?

| Puntaje manual | Criterio |
|---:|---|
| 0.0 | No hay decision tecnica clara |
| 0.75 | Hay decision, pero la evidencia es incompleta o no menciona limitaciones |
| 1.5 | La decision usa metrica adecuada, comparacion/baseline y una limitacion concreta |

## Senales de alerta

- Escalamiento ajustado con todo el dataset.
- Hiperparametro escogido por prueba o entrenamiento solamente.
- Umbral elegido sin relacion con precision/recall.
- Recomendacion sin contexto de decision.
- Metricas reportadas sin declarar clase positiva.

La revision manual se centra en decision, evidencia y limitacion.
