# Rúbrica Lab 5: Aprendizaje no supervisado

Puntaje total: 100 puntos.

## Autograder: 85 puntos

| Componente | Puntos | Criterio |
|---|---:|---|
| Centrado | 10 | Calcula medias por columna, conserva forma y deja columnas centradas. |
| PCA con SVD | 20 | Devuelve componentes, scores, varianza explicada y media con dimensiones correctas y valores coherentes. |
| Reconstrucción | 10 | Reconstruye en el espacio original y reduce error al aumentar componentes. |
| K-Means | 15 | Entrena con `n_init=10`, produce etiquetas, inertia y silhouette válidos. |
| Selección de k | 10 | Evalúa varios valores de k y selecciona por mayor silhouette. |
| Similitud coseno | 10 | Produce matriz simétrica, diagonal correcta y valores numéricos estables. |
| Recomendación | 10 | Ordena por similitud y excluye item consultado e items ya vistos. |

## Revisión manual: 15 puntos

| Nivel | Puntos | Descriptor |
|---|---:|---|
| Excelente | 13-15 | Interpreta evidencia cuantitativa, reconoce límites de PCA/K-Means/recomendación y propone una validación adicional concreta. |
| Adecuado | 9-12 | Usa evidencia relevante, pero la interpretación es parcial o la validación queda poco específica. |
| Insuficiente | 4-8 | Describe resultados sin justificar decisiones o ignora limitaciones importantes. |
| No evaluable | 0-3 | Respuesta ausente, genérica o incompatible con el notebook. |

## Carga manual esperada

Tiempo objetivo por estudiante: 2 minutos.

El profesor solo debe leer la pregunta manual y marcar casos donde:

- la explicación contradice los resultados numéricos;
- hay uso de test o validación de forma indebida;
- se hacen afirmaciones fuertes sin evidencia;
- la recomendación tiene riesgo ético o técnico no reconocido.

