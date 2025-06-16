from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    # AFR RSS feed URL
    afr_rss_url: str = Field(..., env="AFR_RSS_URL")
    # keep the raw comma-separated keywords string
    keywords: str = Field(..., env="KEYWORDS")

    # — Email settings —
    smtp_server: str = Field(..., env="SMTP_SERVER")
    smtp_port:   int = Field(..., env="SMTP_PORT")
    smtp_user:   str = Field(..., env="SMTP_USER")
    smtp_pass:   str = Field(..., env="SMTP_PASS")
    email_to:    str = Field(..., env="EMAIL_TO")

    class Config:
        env_file = ".env"
        case_sensitive = False

    @property
    def keywords_list(self) -> list[str]:
        # split the comma-list into a clean, lowercase list
        return [k.strip().lower() for k in self.keywords.split(",") if k.strip()]

# instantiate once, reuse everywhere
settings = Settings()
