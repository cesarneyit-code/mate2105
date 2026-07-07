# Rúbrica: laboratorio diagnóstico 1

Este laboratorio es diagnóstico y de bajo riesgo. Su función principal es identificar el nivel inicial del grupo, problemas de entorno y necesidades de apoyo.

Escala sugerida: 10 puntos formativos. Si el curso decide no asignar nota numérica a la Semana 1, esta misma rúbrica puede usarse como lista de chequeo.

| Criterio | Puntos | Excelente | Adecuado | Requiere revisión |
|---|---:|---|---|---|
| Ejecucion del entorno | 1.5 | Ejecuta todo el notebook sin errores y selecciona un kernel adecuado | Ejecuta la mayor parte o documenta con precision un error técnico | No ejecuta y no documenta el bloqueo |
| Inspeccion de datos | 1.5 | Identifica filas, variables, clases, dimensiones y balance con valores correctos | Identifica la mayoría de elementos con errores menores | Confunde `X`, `y`, clases, filas o columnas |
| Particion train/test | 1.0 | Explica el propósito de separar datos y por qué `stratify=y` preserva proporciones | Explica parcialmente la partición | No justifica la partición o cree que es solo una formalidad |
| Baseline | 1.5 | Calcula e interpreta el baseline como comparación mínima necesaria | Calcula baseline pero lo interpreta de forma superficial | No calcula baseline o no entiende su función |
| Modelo y métrica | 1.5 | Compara modelo y baseline usando accuracy, sin exagerar el resultado | Reporta numeros correctos con interpretación limitada | Presenta métricas aisladas sin comparación |
| Diagnóstico de errores | 1.0 | Usa matriz de confusion o reporte para hablar de errores por clase y limitaciones | Menciona errores, pero sin conectar con limitaciones | No analiza errores |
| Conclusion técnica | 1.0 | Menciona métrica, baseline, partición/datos y limitacion principal | Menciona algunos elementos, pero falta precision | Concluye de forma exagerada, vaga o no técnica |
| Ideas de proyecto | 1.0 | Propone dos ideas con unidad de observación, pregunta, decisión y riesgo | Propone ideas incompletas pero rescatables | Las ideas no son modelables, no tienen datos claros o son solo herramientas |

## Manejo de bloqueos técnicos

Un estudiante con bloqueo técnico puede recibir credito razonable si:

1. entrega el notebook o documento con el error completo;
2. identifica en que paso fallo;
3. responde las preguntas conceptuales que no dependen de ejecutar código;
4. propone un plan concreto para resolverlo antes de la Semana 2.

No debe recibir el mismo tratamiento un bloqueo documentado que una entrega vacia.

## Retroalimentacion sugerida

El asistente no debe corregir cada línea de código manualmente. Debe concentrarse en:

- problemas de entorno;
- confusion entre datos, modelo y métrica;
- interpretaciones exageradas;
- ideas de proyecto no modelables;
- estudiantes que requieren apoyo temprano.

Comentarios utiles:

- "Tu resultado numérico esta bien, pero falta compararlo contra el baseline."
- "La conclusión promete más de lo que permite un dataset pequeño."
- "La idea de proyecto necesita unidad de observación y decisión."
- "El error técnico esta bien documentado; falta intentar el chequeo de entorno."

## Criterio de logro

El estudiante está listo para avanzar a la Semana 2 si puede:

- ejecutar un notebook básico;
- distinguir `X`, `y`, baseline y modelo;
- explicar por qué se separan entrenamiento y prueba;
- escribir una conclusión que no se limite a reportar un número.
