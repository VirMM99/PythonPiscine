

def secure_archive(filename, mode="r", content=None):
    try:
        if mode == "r":
            with open(filename, "r") as f:
                data = f.read()
                return (True, data)
        elif mode == "w":
            if content is None:
                return (False, "No content to write")
            with open(filename, "w") as f:
                f.write(content)
                return (True, "Content successfully written to file")
        else:
            return (False, "Invalid mode")
    except Exception as e:
        return (False, str(e))


print("=== Cyber Archives Security ===")
print()
print("Using 'secure archive' to read from a nonexistent file:")
print(secure_archive("/not/existing/file"))
print()
print("Using 'secure archive' to read from a nonexistent file:")
print(secure_archive("/etc/shadow"))
print()
print("Using 'secure archive' to read from a regular file:")
success, data = secure_archive("ancient_fragment.txt")
print((success, data))
print()
print("Using 'secure archive' to write previous content to a new file:")
print(secure_archive("new_file.txt", "w", data))


# Con el with statement ensures que el file se cierra automáticamente
# Aunq la excepcion ocurra, previniendo resource leaks
# haciendo el código mas safer
# Se ha puesto etc/shadow por que la otra no existe en mi ordena
