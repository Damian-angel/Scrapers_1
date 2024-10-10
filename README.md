# Selenium Web Scraper para Extracción de Atributos de Producto

Este script utiliza `Selenium` para automatizar la descarga de un archivo JSON desde una URL, extrae datos específicos sobre los atributos del producto y los guarda en un archivo CSV. El código está pensado para ejecutarse en un entorno sin interfaz gráfica, usando un navegador Chrome en modo headless (sin ventana).

## Requisitos

Antes de ejecutar el script, asegúrate de tener instalados los siguientes requisitos:

1. Python 3.6 o superior 
2. Las siguientes bibliotecas de Python:
   - `selenium`
   - `json`
   - `csv`
   - `time`

Puedes instalar `Selenium` utilizando `pip`:

```bash
pip install selenium
```

ChromeDriver
El script requiere que el archivo chromedriver.exe esté localizado en una ruta específica

`
  chrome_driver_path = "C:\\Users\\lch_a\\OneDrive\\Documentos\\GitHub\\code_challenge_v1\\chromedriver.exe"
`

## Flujo del Script

Inicialización del Navegador:

1. Se utiliza Selenium para lanzar el navegador Chrome en modo headless, lo que significa que el navegador funciona en segundo plano sin mostrar ventanas.
Descarga del JSON:

2. El navegador visita la URL proporcionada y descarga el contenido JSON.
Extracción de Datos:

3. Se extraen varias propiedades relacionadas con los productos, como alérgenos, si es vegano, kosher, orgánico, etc., del contenido JSON.
Generación del Archivo CSV:

4. La información extraída se guarda en un archivo CSV llamado output-product.csv.
