import sys
import os
import site

# If in terminal sys.prefix = sys.base_prefix
# then we are not in a venv, we are in global
in_venv = sys.prefix != sys.base_prefix


def check_matrix() -> None:
    print("MATRIX STATUS: ", end="")
    if in_venv:
        print("Welcome to the construct")
    else:
        print("You're still plugged in")


# Para ver the name of the venv
env_path = sys.prefix
env_name = os.path.basename(env_path)
packages_path = site.getsitepackages()[0]


def check_env() -> None:
    if in_venv:
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Enviroment: {env_name}")
        print(f"Enviroment Path: {env_path}")
        print("\nSUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.")
        print("\nPackage installation path:")
        print(packages_path)
    else:
        print(f"Current Python: {sys.executable}")
        print("Virtual Enviroment: None detected")
        print("\nWARNING: You're in the global environment!")
        print("The machines can see everything you install.")
        print("\nTo enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env\\Scripts\\activate # On Windows")
        print("\nThen run this program again.")


if __name__ == "__main__":
    check_matrix()
    print()
    check_env()
