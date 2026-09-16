#!/usr/bin/env python3
"""Verifica que los archivos de sistema sigan la plantilla estandar."""

import sys
from pathlib import Path

REQUIRED_SECTIONS = ["## Descripción", "## Estado", "## Función"]

errors = []
for f in list(Path("docs/systems").glob("S*.md")) + list(Path("docs/systems").glob("s*.md")):
    content = f.read_text(encoding="utf-8")
    for section in REQUIRED_SECTIONS:
        if section not in content:
            errors.append(f"{f.name}: falta '{section}'")

if errors:
    print("Sistemas con estructura invalida:")
    for e in errors:
        print(f"  - {e}")
    sys.exit(1)

print("Todos los sistemas siguen la plantilla")
