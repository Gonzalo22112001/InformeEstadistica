import json

input_file = "informe.ipynb"
output_file = "informe_reparado.ipynb"

try:
    with open(input_file, "r", encoding="utf-8") as f:
        notebook = json.load(f)

    # Verifica cada celda y elimina las dañadas
    valid_cells = []
    for cell in notebook.get("cells", []):
        if "cell_type" in cell and "source" in cell:
            valid_cells.append(cell)

    # Reescribe el archivo con las celdas válidas
    notebook["cells"] = valid_cells
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(notebook, f, indent=4)

    print(f"Archivo reparado guardado como: {output_file}")

except Exception as e:
    print(f"Error: {e}")

