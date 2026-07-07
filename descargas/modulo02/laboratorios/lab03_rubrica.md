# Rubrica Lab 3: Red neuronal desde cero

## Distribucion

| Componente | Peso |
|---|---:|
| Autograder: funciones matematicas y algoritmicas | 85% |
| Interpretacion manual | 15% |

## Revisión manual

Tiempo esperado por estudiante: 2-3 minutos.

| Puntaje | Criterio |
|---:|---|
| 0 | No hay interpretación, no usa evidencia o contradice los resultados |
| 1 | Menciona una métrica o curva, pero no diagnostica entrenamiento ni limitación |
| 2 | Usa pérdida, validación/comparación y limitación concreta para justificar aprendizaje |

## Señales de alerta

- Accuracy perfecta sin curva ni partición clara.
- Funciones hardcodeadas para casos de prueba.
- Uso del conjunto de test para seleccionar hiperparámetros.
- Notebook que depende de ejecutar celdas fuera de orden.
- Comparación con PyTorch/sklearn sin misma partición.

## Comentarios rápidos sugeridos

- "La evidencia numérica es correcta, pero falta conectar con una limitación."
- "La curva de pérdida se interpreta bien; falta separar validación de test."
- "La comparación profesional es útil, pero debe usar la misma partición."
- "La implementación parece funcionar, pero la explicación no defiende una decisión técnica."
