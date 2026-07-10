# Paquete de datasets públicos MATE-2105

Estos archivos CSV son pequeños y reproducibles. Cinco fueron generados para el
curso y uno es una adaptación congelada de un conjunto oficial de Datos Abiertos
Bogotá. Sirven para practicar lectura, modelación, validación y diagnóstico sin
depender de internet durante la clase.

## Archivos

| Archivo | Uso principal |
|---|---|
| `regresion_lineal_sintetica.csv` | regresión lineal, descenso del gradiente y regularización |
| `clasificacion_binaria_sintetica.csv` | regresión logística, umbrales, métricas y slices |
| `clusters_sinteticos.csv` | K-Means, centroides, inercia y silueta |
| `pca_sintetico.csv` | PCA, SVD, varianza explicada y reconstrucción |
| `recomendacion_interacciones.csv` | recomendación item-item y evaluación offline pequeña |
| `vivienda_nueva_bogota_subzonas.csv` | unidad de observación, documentación y regresión con datos agregados reales |

## Trazabilidad

El archivo `manifest_datos.json` registra columnas, número de filas, tamaño,
hash SHA-256, semilla y uso pedagógico de cada CSV.

Para regenerar y auditar:

```bash
python3 scripts/generar_datasets_libro.py
python3 scripts/auditar_datasets_libro.py
```

## Límite de uso

Los datasets sintéticos no representan poblaciones reales. El archivo de vivienda
resume 32 subzonas y no representa inmuebles individuales; además, el recurso
original no declara explícitamente la unidad del campo `precios`. Ningún archivo
de este paquete debe usarse para tomar decisiones clínicas, financieras,
operativas o institucionales.

## Fuente externa

`vivienda_nueva_bogota_subzonas.csv` adapta siete columnas del conjunto
[Caracterización precios vivienda nueva](https://datosabiertos.bogota.gov.co/dataset/caracterizacion),
publicado por la Secretaría Distrital del Hábitat con licencia CC BY 4.0. La
adaptación selecciona columnas, normaliza encabezados, recorta espacios y redondea
valores numéricos a seis decimales. Fecha de consulta: 2026-07-10.
