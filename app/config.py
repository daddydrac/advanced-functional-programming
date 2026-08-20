"""Provided environment schema for the Docker Compose workshop."""

from functools import lru_cache
from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Immutable environment configuration; secrets are required, never embedded."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
        frozen=True,
    )

    app_name: str = "LambdaFlux Functional Python Workshop"
    app_environment: str = "development"
    database_url: str = Field(min_length=1)
    course_dir: Path = Path("/course")
    jwt_secret: str = Field(min_length=43)
    jwt_issuer: str = "lambdaflux.local"
    jwt_audience: str = "lambdaflux-api"
    jwt_access_minutes: int = Field(default=15, ge=1, le=60)
    jwt_refresh_minutes: int = Field(default=1_440, ge=15, le=10_080)
    jwt_challenge_minutes: int = Field(default=5, ge=1, le=15)
    auth_max_failures: int = Field(default=5, ge=3, le=20)
    auth_failure_window_minutes: int = Field(default=10, ge=1, le=60)
    mfa_encryption_key: str = Field(min_length=43, max_length=44)
    mfa_issuer: str = "LambdaFlux"
    mfa_valid_window: int = Field(default=1, ge=0, le=1)
    ollama_base_url: str = "http://ollama:11434"
    ollama_model: str = "qwen3:4b"
    ollama_timeout_seconds: float = Field(default=90.0, ge=1.0, le=600.0)


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    """Load and cache configuration.

    Provided course infrastructure. Configuration concepts are explained in
    chapter 44, item 44.3:
    ``tutorials/part-3-application/44-docker-compose-full-stack.md``.
    """
    return Settings()
