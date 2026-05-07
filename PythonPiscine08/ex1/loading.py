

# Checkear si un paquete existe
def check_package() -> bool:
    try:
        import pandas as pd
        print(f"[OK] pandas ({pd.__version__}) - Data manipulation ready")
        pd_ok = True
    except ModuleNotFoundError:
        print("[MISSING] pandas")
        pd_ok = False
    try:
        import numpy as np
        print(f"[OK] numpy ({np.__version__}) - Numerical computation ready")
        np_ok = True
    except ModuleNotFoundError:
        print("[MISSING] numpy")
        np_ok = False
    try:
        import matplotlib as plt
        print(f"[OK] matplotlib ({plt.__version__}) - Visualization ready")
        plt_ok = True
    except ModuleNotFoundError:
        print("[MISSING] matplotlib")
        plt_ok = False
    if not np_ok or not pd_ok or not plt_ok:
        all_ok = False
    else:
        all_ok = True
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
    print()
    print("LOADING STATUS: Loading programs...")
    print("\nChecking dependencies:")

    if not check_package():
        exit()

    import numpy as np
    import pandas as pd
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
    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")
