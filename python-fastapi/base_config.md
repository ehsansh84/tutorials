# How to use BaseConfig
If you create a model that inherits from BaseSettings, the model initialiser will attempt to determine the values of any fields not passed as keyword arguments by reading from the environment. (Default values will still be used if the matching environment variable is not set.)

This makes it easy to:
- Create a clearly-defined, type-hinted application configuration class
- Automatically read modifications to the configuration from environment variables
- Manually override specific settings in the initialiser where desired (e.g. in unit tests)

A simple way to load configs from `.env` file:
`.env` inside project root:
```
EMAIL="ehsan.shirzadi[at]gmail.com"
APP_NAME="MyApp"
```
`settings.py`
```python
from pydantic import BaseSettings
class Settings(BaseSettings):
    app_name: str
    email: str

    class Config:
        env_file = ".env"
```
`boot.py`
```python
from settings import Settings

app = FastAPI()


setting = Settings()
print(setting)
```

### References:
- [Settings management](https://docs.pydantic.dev/usage/settings/)
- []()
- []()
- []()