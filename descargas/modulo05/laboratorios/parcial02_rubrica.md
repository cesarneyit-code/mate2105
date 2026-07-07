# Rúbrica Parcial 2

Puntaje sugerido: 100 puntos.

## Notebook autograded: 70 puntos

| Componente | Puntos | Criterio |
|---|---:|---|
| Softmax estable y cross-entropy | 10 | Probabilidades válidas, estabilidad ante shifts y pérdida correcta. |
| Particiones estratificadas | 10 | Train/dev/test cubren datos, no se solapan y preservan proporciones. |
| Resumen CV y selección | 10 | Media, desviación y selección por desempeño con desempate prudente. |
| PCA desde SVD | 15 | Centrado, varianza explicada, reconstrucción y error coherente. |
| K-Means y silhouette | 10 | Evalúa varios k y selecciona por mayor silhouette. |
| Manifest reproducible | 15 | Hash SHA-256, parámetros, métricas y artefactos estructurados. |

## Preguntas estructuradas: 20 puntos

Pueden calificarse en Gradescope como selección, respuesta numérica o fórmula:

- dimensiones en forward propagation;
- rol del test set;
- efecto de regularización;
- lectura de learning curve;
- interpretación de silhouette;
- riesgo de persistencia de modelos no confiables.

## Explicación breve: 10 puntos

| Nivel | Puntos | Descriptor |
|---|---:|---|
| Excelente | 9-10 | Integra métrica, variabilidad, slices, reproducibilidad y decisión proporcional. |
| Adecuado | 6-8 | Identifica evidencia principal, pero falta precisión o manifest. |
| Insuficiente | 2-5 | Respuesta genérica o sin conexión con validación. |
| No evaluable | 0-1 | Ausente o incompatible con el caso. |

## Carga manual esperada

Tiempo objetivo por estudiante: 3 a 5 minutos.

El profesor revisa solo:

- preguntas estructuradas no automatizadas;
- explicación breve;
- casos donde el autograder marque ejecución fallida o resultados sospechosos.

