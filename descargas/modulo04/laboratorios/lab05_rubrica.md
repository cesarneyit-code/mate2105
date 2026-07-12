# Rúbrica Lab 5: Aprendizaje no supervisado

Puntaje total: 100 puntos.

## Autograder: 85 puntos

| Componente | Puntos | Criterio |
|---|---:|---|
| Centrado | 10 | Calcula medias por columna, conserva forma y deja columnas centradas. |
| PCA con SVD | 15 | Devuelve componentes, scores, varianza explicada y media con dimensiones correctas y valores coherentes. |
| Reconstrucción | 10 | Reconstruye en el espacio original y reduce error al aumentar componentes. |
| K-Means | 15 | Entrena con `n_init=10`, produce etiquetas, inertia y silhouette válidos. |
| Selección de k | 10 | Evalúa varios valores de k y selecciona por mayor silhouette. |
| Similitud coseno | 10 | Produce matriz simétrica, diagonal correcta y valores numéricos estables. |
| Recomendación | 5 | Ordena por similitud y excluye item consultado e items ya vistos. |
| Contrato probabilístico | 10 | Distingue covarianza poblacional/muestral, fuentes de inestabilidad y mecanismo de exposición. |

## Revisión manual: 15 puntos

| Nivel | Puntos | Descriptor |
|---:|---:|---|
| 2 | 15 | Interpreta un resultado, separa variación muestral y algorítmica, reconoce exposición y propone validación concreta. |
| 1 | 7.5 | Usa un resultado relevante, pero la interpretación o la validación queda incompleta. |
| 0 | 0 | Respuesta ausente, genérica, contradictoria o incompatible con el notebook. |

## Carga manual esperada

Tiempo objetivo por estudiante: 2 minutos.

El profesor solo debe leer la pregunta manual y marcar casos donde:

- la explicación contradice los resultados numéricos;
- hay uso de test o validación de forma indebida;
- se hacen afirmaciones fuertes sin un resultado que las sostenga;
- la recomendación tiene riesgo ético o técnico no reconocido.
