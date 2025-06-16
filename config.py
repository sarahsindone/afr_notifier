# config.py
from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    # AFR RSS feed URL
    afr_rss_url: str = Field(..., env="AFR_RSS_URL")
    # Comma-separated list of keywords in your .env
    keywords: list[str] = Field(..., env="KEYWORDS")

    # — New email settings —
    smtp_server: str = Field(..., env="SMTP_SERVER")
    smtp_port:   int = Field(..., env="SMTP_PORT")
    smtp_user:   str = Field(..., env="SMTP_USER")
    smtp_pass:   str = Field(..., env="SMTP_PASS")
    email_to:    str = Field(..., env="EMAIL_TO")

    class Config:
        env_file = ".env"
        case_sensitive = False

# instantiate a single settings object for import elsewhere
settings = Settings()
