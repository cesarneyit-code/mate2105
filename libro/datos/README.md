# Paquete de datasets públicos MATE-2105

Estos archivos CSV son pequeños, generados artificialmente y reproducibles. Sirven para
práctica de lectura, modelación, validación y diagnóstico sin depender de
internet ni de librerías externas durante la descarga del libro.

## Archivos

| Archivo | Uso principal |
|---|---|
| `regresion_lineal_sintetica.csv` | regresión lineal, descenso del gradiente y regularización |
| `clasificacion_binaria_sintetica.csv` | regresión logística, umbrales, métricas y slices |
| `clusters_sinteticos.csv` | K-Means, centroides, inercia y silueta |
| `pca_sintetico.csv` | PCA, SVD, varianza explicada y reconstrucción |
| `recomendacion_interacciones.csv` | recomendación item-item y evaluación offline pequeña |

## Trazabilidad

El archivo `manifest_datos.json` registra columnas, número de filas, tamaño,
hash SHA-256, semilla y uso pedagógico de cada CSV.

Para regenerar y auditar:

```bash
python3 scripts/generar_datasets_libro.py
python3 scripts/auditar_datasets_libro.py
```

## Límite de uso

Estos datasets no representan poblaciones reales. No deben usarse para tomar
decisiones clínicas, financieras, operativas o institucionales. Su función es
didáctica.
