# Rúbricas del proyecto MATE-2105

La especificación de fechas y formatos está en <https://cesarneyit-code.github.io/mate2105/proyecto.html>.

## Hitos y checkpoints: 100 puntos, equivalentes al 15% del curso

### P01 Lista corta de datos: 5 puntos

| Criterio | Puntos |
|---|---:|
| 2 o 3 fuentes verificables con licencia y acceso | 2 |
| Unidad, tamaño, objetivo y variables descritos | 1 |
| Riesgo de cada opción identificado | 1 |
| Opción preferida y comparación razonada | 1 |

### P02 Prepropuesta: 10 puntos

| Criterio | Puntos |
|---|---:|
| Pregunta, usuario y alcance | 2 |
| Población, muestra y unidad | 2 |
| Estimando y métrica tentativa | 2 |
| Baseline y protocolo inicial | 2 |
| Riesgo, incertidumbre y siguiente paso | 2 |

### P03 Propuesta aprobable: 20 puntos

| Criterio | Puntos |
|---|---:|
| Datos viables, legales y documentados | 4 |
| Pregunta, población, muestra y estimando coherentes | 4 |
| Partición y prevención de leakage | 4 |
| Métrica, baseline y modelos comparables | 4 |
| Incertidumbre, riesgos y plan de trabajo | 4 |

### P04 Baseline: 20 puntos

| Criterio | Puntos |
|---|---:|
| Notebook ejecutable y estructura solicitada | 5 |
| Partición reproducible sin leakage evidente | 4 |
| Baseline correcto y pertinente | 4 |
| Métrica calculada e interpretada | 4 |
| Limitación y siguiente experimento | 3 |

### P05 Checkpoint técnico: 20 puntos

| Criterio | Puntos |
|---|---:|
| Comparación justa con el baseline | 4 |
| Protocolo y partición reproducibles | 4 |
| Variación entre folds, muestras o repeticiones | 4 |
| Análisis de errores o slices | 4 |
| Siguiente experimento priorizado y límites | 4 |

### P06 Análisis estructural: 10 puntos

| Criterio | Puntos |
|---|---:|
| Pregunta y método pertinentes | 2 |
| Preprocesamiento correcto | 2 |
| Resultado cuantitativo y soporte visual | 2 |
| Estabilidad o sensibilidad | 2 |
| Interpretación y límite | 2 |

### P07 Reproducibilidad: 15 puntos

| Criterio | Puntos |
|---|---:|
| `README.md` y orden de ejecución suficientes | 3 |
| Entorno y dependencias declarados | 3 |
| Datos documentados y versionados | 3 |
| Manifest, métricas y semilla coherentes | 3 |
| Ejecución limpia reconstruye el resultado principal | 3 |

En cada criterio, evidencia completa recibe el puntaje total; evidencia parcial recibe aproximadamente la mitad; evidencia ausente, contradictoria o imposible de abrir recibe cero.

## Reporte y repositorio final: 100 puntos, equivalentes al 15% del curso

| Criterio | Completo | Parcial | Insuficiente | Máximo |
|---|---|---|---|---:|
| Problema, datos y alcance | pregunta, uso, población, muestra, fuente y cobertura son coherentes | falta precisión en uno o dos elementos | pregunta o datos no permiten evaluar el alcance | 15 |
| Matemática y algoritmo | estimando, estimador, objetivo y algoritmo se definen con la notación del proyecto | formulación correcta pero incompleta o poco conectada | descripción de biblioteca sin fundamento o con errores | 20 |
| Validación, incertidumbre y errores | comparación justa, test reservado, variación cuantificada y fallos analizados | resultados útiles con una debilidad metodológica | leakage, comparación inválida o ausencia de diagnóstico | 25 |
| Reproducibilidad | otra persona reconstruye el resultado siguiendo el README | requiere una corrección menor documentable | faltan archivos, dependencias o rutas funcionales | 15 |
| Comunicación | tesis, tablas, figuras y escritura sostienen una lectura clara | mensaje comprensible con ruido o soportes incompletos | resultados desconectados o difíciles de interpretar | 15 |
| Limitaciones y ética | límites concretos y recomendación proporcional | límites genéricos o recomendación demasiado amplia | omite riesgos relevantes o afirma más de lo observado | 10 |

## Defensa individual: 10 puntos, equivalentes al 10% del curso

| Criterio | 0 | 1 | 2 |
|---|---|---|---|
| Autoría | no identifica una contribución | contribución vaga | contribución concreta y archivo verificable |
| Matemática | error conceptual | explicación parcial | fórmula o algoritmo correcto conectado al proyecto |
| Validación | no justifica métricas o partición | justificación incompleta | conecta baseline, partición, métrica e incertidumbre |
| Reproducibilidad | no sabe reconstruir el resultado | localiza archivos aislados | explica entorno, orden, manifest y artefacto |
| Limitaciones | no reconoce límites | límite genérico | límite específico y efecto sobre la conclusión |
