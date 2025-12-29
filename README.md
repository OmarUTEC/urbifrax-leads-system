```markdown
# urbifrax-leads-system

Sistema simple de gestión de leads inmobiliarios por consola.

Archivos principales:

- `main.py`: Interfaz de consola (registro, listado, búsqueda).
- `leads.py`: Lógica de leads (añadir, listar, filtrar, buscar).
- `storage.py`: Persistencia en `data/leads.json`.
- `utils.py`: Validaciones y helpers de entrada.

Uso rápido:

1. Ejecuta:

```bash
python -m urbifrax-leads-system.main
```

o desde el directorio del proyecto:

```bash
python main.py
```

2. Sigue el menú para registrar, listar o buscar leads.

Los leads se guardan en `data/leads.json` como una lista de objetos JSON.
```
# urbifrax-leads-system

