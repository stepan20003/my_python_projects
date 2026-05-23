import sys
import importlib


req = {
    "pandas": "Data manipulation",
    "numpy": "Numerical computation",
    "matplotlib": "Visualization",
    "requests": "Network access (optional)"
    }


def check_dependencies():
    loaded = {}
    missing = []

    print("LOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")
    for package, descriptions in req.items():
        try:
            module = importlib.import_module(package)
            version = getattr(module, "__version__", "unknown")
            print(f"[OK] {package} ({version}) - {descriptions} ready")
            loaded[package] = module
        except ImportError:
            print(f"[MISSING] {package} - {descriptions} unavailable")
            missing.append(package)
    return loaded, missing


def show_installation_help(missing_packages):
    """Display installation instructions."""

    if not missing_packages:
        return

    print("\nMissing dependencies detected.\n")

    print("Install with pip:")
    print("pip install -r requirements.txt\n")

    print("Install with Poetry:")
    print("poetry install\n")

    print("Missing packages:")
    for package in missing_packages:
        print(f"- {package}")


def compare_package_management():
    """Show pip vs Poetry differences."""

    print("\nPACKAGE MANAGEMENT COMPARISON")
    print("-" * 40)

    print("pip:")
    print("  - Uses requirements.txt")
    print("  - Global or virtual environment installs")
    print("  - Simple dependency management")

    print("\nPoetry:")
    print("  - Uses pyproject.toml")
    print("  - Automatic virtual environments")
    print("  - Dependency resolution and locking")
    print("  - Better project management")


def analyze_matrix_data(np, pd, plt):
    print("\nAnalyzing Matrix data...")
    matrix_data = np.random.randint(0, 2, size=(1000, 5))
    df = pd.DataFrame(
        matrix_data,
        columns=[
            "Reality",
            "Choice",
            "Freedom",
            "Resistance",
            "Awakening"
        ]
    )
    print(f"Processing {len(df)} data points...")
    means = df.mean()
    print("\nMatrix Signal Strength:")
    print(means)
    print("\nGenerating visualization...")
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar(means.index, means.values)
    ax.set_title("Matrix Data Analysis")
    ax.set_ylabel("Average Signal")
    plt.tight_layout()
    filename = "matrix_analysis.png"
    plt.savefig(filename)
    print("Analysis complete!")
    print(f"Results saved to: {filename}")


def main():
    loaded, missing = check_dependencies()
    compare_package_management()
    required_core = ["pandas", "numpy", "matplotlib"]

    if any(pkg not in loaded for pkg in required_core):
        show_installation_help(missing)
        sys.exit(1)
    pd = importlib.import_module("pandas")
    np = importlib.import_module("numpy")
    plt = importlib.import_module("matplotlib.pyplot")
    pd = loaded["pandas"]
    np = loaded["numpy"]
    analyze_matrix_data(np, pd, plt)


if __name__ == "__main__":
    main()
