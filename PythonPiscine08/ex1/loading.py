import importlib


# Checkear si un paquete existe
def check_package(name: str):
    spec = importlib.util.find_spec(name)
    if spec is None:
        print(f"[MISSING] {name}")
        return False
    else:
        module = importlib.import_module(name)
        version = getattr(module, "__version__", "unknown")
        print(f"[OK] {name} ({version}) - ready")
        return True

def check_all_packs() -> bool:
    packages = ["pandas", "numpy", "matplotlib"]

    all_ok = True

    for pkg in packages:
        if not check_package(pkg):
            all_ok = False
    if not all_ok:
        print("\nMissing dependencies!")
        print("Install with pip:")
        print("pip install -r requirements.txt")
        print("\nOr with Poetry:")
        print("poetry install")
        # Cuando faltan paquetes
        print("\n--- Dependency Management ---")
        print("pip uses requirements.txt")
        print("Poetry uses pyproject.toml and virtual environments")
        
    return all_ok

if __name__ == "__main__":
    print("LOADING STATUS: Loading programs...")
    print("Checking dependencies:")

    if not check_all_packs():
        exit()

    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt

    print("\nAnalyzing Matrix data...")
    #  Generar datos con numpy
    data = np.random.randn(1000)
    # Usar pandas para convertir los datos
    df = pd.DataFrame(data, columns=["values"])
    print("Processing 1000 data points...")
    print("Generating visualization...")
    # Crear un gáfico fácil un histograma
    plt.hist(df["values"])
    plt.savefig("matrix_analysis.png")
    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")
