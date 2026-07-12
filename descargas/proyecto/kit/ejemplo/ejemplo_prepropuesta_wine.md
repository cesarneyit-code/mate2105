# Ejemplo resuelto de prepropuesta

Este documento muestra el nivel de precisión esperado. `load_wine` viaja con `scikit-learn` y permite reproducir el ejemplo sin internet, pero su documentación no describe por completo un proceso operativo contemporáneo. Por eso sirve como modelo de formato, no como tema ideal para el proyecto final.

## Identificación

- Grupo: ejemplo.
- Integrantes: estudiante A, estudiante B.
- Hito: P02 Prepropuesta.
- Fecha: 2026-08-20.

## Pregunta y uso

**Pregunta.** Entre las tres clases de cultivar representadas en la muestra, ¿con qué precisión puede una regresión logística clasificar una observación usando las 13 mediciones químicas disponibles y cómo se compara con predecir siempre la clase más frecuente?

**Usuario hipotético.** Un laboratorio que necesita una referencia reproducible para revisar consistencia de etiquetas históricas.

**Uso.** Marcar observaciones discordantes para revisión humana. No se propone autenticar origen geográfico ni reemplazar una prueba de laboratorio.

## Datos

- Fuente: `sklearn.datasets.load_wine`, derivado del conjunto Wine de UCI.
- Unidad de observación: un análisis químico de una muestra de vino.
- Tamaño: 178 observaciones, 13 variables y 3 clases; conteos 59, 71 y 48.
- Objetivo: clase de cultivar codificada como 0, 1 o 2.
- Acceso: incluido en `scikit-learn`; no requiere descarga externa.

## Población y muestra

La documentación disponible describe 178 análisis, pero no establece un mecanismo de muestreo probabilístico ni una población contemporánea claramente delimitada. La conclusión se restringirá a observaciones comparables con esta colección. No se afirmará desempeño para vinos comerciales actuales ni para otros laboratorios.

## Objeto matemático

Para un par aleatorio \((X,Y)\) con la distribución de uso restringida, el objetivo es estimar las probabilidades condicionales \(P(Y=k\mid X=x)\). El clasificador usa la clase de mayor probabilidad estimada. La métrica principal será F1 macro porque da el mismo peso a las tres clases; accuracy será secundaria.

El estimador será regresión logística multinomial con escalamiento ajustado únicamente con entrenamiento. La variación se estudiará inicialmente con validación cruzada estratificada; el test permanecerá reservado para la comparación final.

## Protocolo inicial

- Partición de desarrollo: entrenamiento y validación estratificados, semilla 2105.
- Baseline: clase más frecuente.
- Modelo: `StandardScaler` seguido de `LogisticRegression`.
- Regla de selección: F1 macro promedio en validación.
- Comprobación final: una sola evaluación en test después de cerrar decisiones.

Como verificación de código, el ejemplo ejecutable usa un test de 25%. Con esa partición, el baseline obtiene accuracy 0.4000 y F1 macro 0.1905; el pipeline logístico obtiene accuracy 0.9778 y F1 macro 0.9771. Estos valores comprueban la implementación, pero todavía no estiman desempeño fuera de la colección documentada.

## Riesgo y siguiente paso

El riesgo principal no es algorítmico: la población y el proceso de observación están insuficientemente documentados. El siguiente paso es localizar la ficha original, verificar significado y unidades de las variables y decidir si existe un contexto de uso que justifique continuar. Si no se puede documentar, el equipo debe escoger otro dataset.
