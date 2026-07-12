# Rúbrica: laboratorio diagnóstico 1

Este laboratorio es diagnóstico y de bajo riesgo. Su función principal es identificar el nivel inicial del grupo, problemas de entorno y necesidades de apoyo.

Escala sugerida: 10 puntos formativos. Si el curso decide no asignar nota numérica a la Semana 1, esta misma rúbrica puede usarse como lista de chequeo.

| Criterio | Puntos | Excelente | Adecuado | Requiere revisión |
|---|---:|---|---|---|
| Ejecución del entorno | 1.0 | Ejecuta todo el notebook sin errores y selecciona un kernel adecuado | Ejecuta la mayor parte o documenta con precisión un error técnico | No ejecuta y no documenta el bloqueo |
| Población, muestra y estimación | 2.0 | Distingue población, muestra aleatoria, realización, estimador y estimación con notación y ejemplo correctos | Distingue la mayoría, pero mezcla un nivel o usa notación imprecisa | Trata el archivo como población o confunde estimador con valor calculado |
| Riesgo e incertidumbre | 1.5 | Compara riesgo esperado y empírico, verifica la distribución muestral y explica la variación | Ejecuta la simulación y reconoce variación, pero no conecta con el objeto poblacional | Exige igualdad exacta o interpreta la variación como error de código |
| Inspección y partición de datos | 1.0 | Identifica filas, variables, clases y justifica separación y estratificación | Identifica la mayoría con errores menores | Confunde `X`, `y`, clases o propósito de test |
| Baseline, modelo y métrica | 1.5 | Compara modelo y baseline usando accuracy y error estándar sin exagerar | Reporta números correctos con interpretación parcial | Presenta métricas aisladas o como propiedades exactas |
| Diagnóstico de errores | 1.0 | Usa matriz de confusión o reporte para hablar de errores por clase y limitaciones | Menciona errores sin conectarlos con limitaciones | No analiza errores |
| Conclusión técnica | 1.0 | Reporta estimación, incertidumbre, baseline, alcance poblacional y limitación | Menciona algunos elementos, pero falta precisión | Concluye de forma exagerada, vaga o no técnica |
| Ideas de proyecto | 1.0 | Propone dos ideas con población, muestreo, unidad, pregunta, estimando y limitación | Propone ideas incompletas pero recuperables | Las ideas no definen datos, población o pregunta modelable |

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
- distinguir población, muestra, estimador y estimación;
- explicar por qué el riesgo empírico varía entre muestras;
- distinguir `X`, `y`, baseline y modelo;
- explicar por qué se separan entrenamiento y prueba;
- escribir una conclusión que reporte estimación, incertidumbre y alcance.
