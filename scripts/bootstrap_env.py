from base64 import urlsafe_b64encode
from os import urandom
from pathlib import Path
from secrets import token_urlsafe

TARGET = Path(".env")


def fernet_key() -> str:
    return urlsafe_b64encode(urandom(32)).decode()


def content() -> str:
    postgres_password = token_urlsafe(32)
    values = (
        ("JWT_SECRET", token_urlsafe(48)),
        ("MFA_ENCRYPTION_KEY", fernet_key()),
        ("APP_ENVIRONMENT", "development"),
        ("POSTGRES_USER", "lambdaflux"),
        ("POSTGRES_PASSWORD", postgres_password),
        ("POSTGRES_DB", "lambdaflux"),
        (
            "DATABASE_URL",
            f"postgresql+psycopg://lambdaflux:{postgres_password}@postgres:5432/lambdaflux",
        ),
        ("COURSE_DIR", "/course"),
        ("API_PORT", "8000"),
        ("JWT_ISSUER", "lambdaflux.local"),
        ("JWT_AUDIENCE", "lambdaflux-api"),
        ("JWT_ACCESS_MINUTES", "15"),
        ("JWT_REFRESH_MINUTES", "1440"),
        ("JWT_CHALLENGE_MINUTES", "5"),
        ("AUTH_MAX_FAILURES", "5"),
        ("AUTH_FAILURE_WINDOW_MINUTES", "10"),
        ("MFA_ISSUER", "LambdaFlux"),
        ("MFA_VALID_WINDOW", "1"),
        ("OLLAMA_BASE_URL", "http://ollama:11434"),
        ("OLLAMA_MODEL", "qwen3:4b"),
        ("OLLAMA_TIMEOUT_SECONDS", "90"),
    )
    return "\n".join(map(lambda item: f"{item[0]}={item[1]}", values)) + "\n"


def main() -> None:
    if TARGET.exists():
        raise SystemExit(".env already exists; refusing to overwrite secrets")
    TARGET.write_text(content(), encoding="utf-8")
    TARGET.chmod(0o600)
    print("Created .env with unique local secrets")


if __name__ == "__main__":
    main()
