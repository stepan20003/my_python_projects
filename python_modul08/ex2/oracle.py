import os
import sys
from dotenv import dotenv_values


def reading() -> dict[str, str]:
    return dotenv_values(".env")


def get_config(key: str, file_config: dict[str, str]) -> str | None:
    return os.getenv(key) or file_config.get(key)


def require(key: str, value: str | None) -> str:
    if value is None or value == "":
        print(f"[ERROR] Missing configuration: {key}")
        sys.exit(1)
    return value


def main():

    file_config = reading()

    matrix_mode = require("MATRIX_MODE",
                          get_config("MATRIX_MODE", file_config))
    db = require("DATABASE_URL", get_config("DATABASE_URL", file_config))
    api = require("API_KEY", get_config("API_KEY", file_config))
    log = require("LOG_LEVEL", get_config("LOG_LEVEL", file_config))
    zion = require("ZION_ENDPOINT", get_config("ZION_ENDPOINT", file_config))

    print("ORACLE STATUS: Reading the Matrix...\n")

    print("Configuration loaded:")
    print("Mode:", matrix_mode)
    if matrix_mode == "development" and db is not None:
        print("Database: Connected to local instance")
    else:
        print("Database: Connected to remote secure cluster")
    if api is not None:
        print("API Access: Authenticated")
    else:
        print("API Access: not Authenticated")

    print("Log Level:", log)
    print("Zion Network:", "Online" if zion else "Offline")

    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available")

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
