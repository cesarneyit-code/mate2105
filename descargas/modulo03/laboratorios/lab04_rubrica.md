# Rúbrica Lab 4: Diagnóstico de modelos

## Distribución

| Componente | Peso |
|---|---:|
| Autograder: particiones, métricas, CV, curvas, slices y contrato probabilístico | 85% |
| Interpretación manual | 15% |

## Revisión manual

Tiempo esperado por estudiante: 2-3 minutos.

La IA funciona como segundo lector: propone un nivel y señala contradicciones,
pero el profesor conserva la decisión final. No recibe nombres ni el notebook
completo y no sustituye el autograder. La meta es 30-45 segundos en casos
normales y 2-3 minutos en casos marcados.

| Puntaje | Criterio |
|---:|---|
| 0 | No hay diagnóstico o no usa resultados del notebook |
| 1 | Menciona un resultado, pero no conecta con baseline, validación o errores |
| 2 | Justifica selección con estimando, métrica, incertidumbre, baseline, slices y siguiente experimento |

El nivel manual se escala al 15% del laboratorio:

\[
\text{puntaje manual}=15\frac{\text{nivel}}{2}.
\]

## Señales de alerta

- Test usado antes de cerrar decisiones.
- Transformaciones hechas antes de partir datos.
- Métrica principal no corresponde al costo del problema.
- Cross-validation sin pipeline.
- Presentar `media - desviación` como intervalo de confianza.
- Recomendación genérica sin acción técnica.
- Tratar scores de folds dependientes como observaciones iid.

## Comentarios rápidos sugeridos

- "La comparación contra baseline está bien; falta analizar errores."
- "La métrica elegida necesita justificación por costo de error."
- "No uses test para decidir hiperparámetros."
- "La recomendación debe nombrar resultado, diagnóstico y siguiente experimento."
