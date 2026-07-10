# Rúbrica Lab 3: Red neuronal desde cero

## Distribución

| Componente | Peso |
|---|---:|
| Autograder: funciones matemáticas y algorítmicas | 85% |
| Interpretación manual | 15% |

## Revisión manual

Tiempo esperado por estudiante: 2-3 minutos.

| Puntaje | Criterio |
|---:|---|
| 0 | No hay interpretación, no usa resultados o los contradice |
| 1 | Menciona una métrica o curva, pero no diagnostica entrenamiento ni limitación |
| 2 | Usa pérdida, validación/comparación y limitación concreta para justificar aprendizaje |

El nivel manual se escala al 15% del laboratorio:

\[
\text{puntaje manual}=15\frac{\text{nivel}}{2}.
\]

## Señales de alerta

- Accuracy perfecta sin curva ni partición clara.
- Funciones hardcodeadas para casos de prueba.
- Uso del conjunto de test para seleccionar hiperparámetros.
- Notebook que depende de ejecutar celdas fuera de orden.
- Comparación con PyTorch/sklearn sin misma partición.

## Comentarios rápidos sugeridos

- "El resultado numérico es correcto, pero falta conectarlo con una limitación."
- "La curva de pérdida se interpreta bien; falta separar validación de test."
- "La comparación con la referencia es útil, pero debe usar la misma partición."
- "La implementación parece funcionar, pero la explicación no acota la conclusión."
