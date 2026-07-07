# Rubrica Lab 4: Diagnóstico de modelos

## Distribución

| Componente | Peso |
|---|---:|
| Autograder: particiones, métricas, CV, curvas y slices | 85% |
| Interpretación manual | 15% |

## Revisión manual

Tiempo esperado por estudiante: 2-3 minutos.

| Puntaje | Criterio |
|---:|---|
| 0 | No hay diagnóstico o no usa evidencia del notebook |
| 1 | Menciona un resultado, pero no conecta con baseline, validación o errores |
| 2 | Justifica selección con métrica, baseline, validación, slices y siguiente experimento |

## Señales de alerta

- Test usado antes de cerrar decisiones.
- Transformaciones hechas antes de partir datos.
- Métrica principal no corresponde al costo del problema.
- Cross-validation sin pipeline.
- Recomendación genérica sin acción técnica.

## Comentarios rápidos sugeridos

- "La comparación contra baseline está bien; falta analizar errores."
- "La métrica elegida necesita justificación por costo de error."
- "No uses test para decidir hiperparámetros."
- "La recomendación debe tener forma evidencia-diagnóstico-acción."
