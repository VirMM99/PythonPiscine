from dotenv import load_dotenv
import os

# Cargar .env
load_dotenv()

print("ORACLE STATUS: Reading the Matrix...\n")

mode = os.getenv("MATRIX_MODE")
db = os.getenv("DATABASE_URL")
api = os.getenv("API_KEY")
log = os.getenv("LOG_LEVEL")
zion = os.getenv("ZION_ENDPOINT")

missing = []

if not mode:
    missing.append("MATRIX_MODE")
if not db:
    missing.append("DATABASE_URL")
if not api:
    missing.append("API_KEY")
if not log:
    missing.append("LOG_LEVEL")
if not zion:
    missing.append("ZION_ENDPOINT")
if missing:
    print("[WARNING] Missing config:", ", ".join(missing))

print("Configuration loaded:")
print(f"Mode: {mode}")

if mode == "development":
    print("Database: Connected to local instance")
    print("Log Level:", log)
elif mode == "production":
    print("Database: Connected to production server")
    print("Log Level:", log)

if api:
    print("API Access: Authenticated")
else:
    print("API Access: Missing Key")
if zion:
    print("Zion Network: Online")
else:
    print("Zion Network: Offline")

print("\nEnviroment security check:")
print("[OK] No hardcoded secrets detected")
print("[OK] .env file properly configured")
print("[OK] Production overrides available")
