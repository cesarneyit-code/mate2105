# Rúbrica Parcial 2

Puntaje sugerido: 100 puntos.

## Notebook autograded: 70 puntos

| Componente | Puntos | Criterio |
|---|---:|---|
| Softmax estable y cross-entropy | 10 | Probabilidades válidas, estabilidad ante shifts y pérdida correcta. |
| Particiones estratificadas | 10 | Train/dev/test cubren datos, no se solapan y preservan proporciones. |
| Resumen CV y selección | 10 | Media, desviación y selección por el puntaje heurístico `media - desviación`. |
| PCA desde SVD | 15 | Centrado, varianza explicada, reconstrucción y error coherente. |
| K-Means y silhouette | 10 | Evalúa varios k y selecciona por mayor silhouette. |
| Manifest reproducible | 15 | Entorno, semilla, partición, parámetros, métricas y hashes SHA-256. |

## Preguntas estructuradas: 20 puntos

Pueden calificarse en Gradescope como selección, respuesta numérica o fórmula:

- dimensiones en forward propagation;
- rol del test set;
- efecto de regularización;
- lectura de learning curve;
- interpretación de silhouette;
- riesgo de persistencia de modelos no confiables.

## Explicación breve: 10 puntos

La revisión usa tres niveles y después escala el resultado a diez puntos.

| Nivel | Puntos | Descriptor |
|---:|---:|---|
| 2 | 10 | Nombra una métrica y su variabilidad, localiza el slice, propone una comprobación y especifica cómo registrarla. |
| 1 | 5 | Identifica parte del problema, pero omite la comprobación o el registro reproducible. |
| 0 | 0 | Ausente, incompatible con el caso o sin referencia a resultados del examen. |

## Carga manual esperada

Tiempo objetivo por estudiante: 3 a 5 minutos.

El profesor revisa solo:

- preguntas estructuradas no automatizadas;
- explicación breve;
- casos donde el autograder marque ejecución fallida o resultados sospechosos.
