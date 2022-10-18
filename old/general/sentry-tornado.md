<!-- Space: RD -->
<!-- Title: How to send errors from python tornado to sentry? -->

### How to send errors from python tornado to sentry?
1. Install sentry-sdk from PyPI:
```commandline
pip install --upgrade sentry-sdk
```
2. If you're on Python 3.6, you also need the aiocontextvars package:
```commandline
pip install --upgrade aiocontextvars
```
3. Initialize the SDK before starting the server:
```python
import sentry_sdk
from sentry_sdk.integrations.tornado import TornadoIntegration

sentry_sdk.init(
   dsn="https://da8486c0814546f68c60ddc6479ab5e5@o1116961.ingest.sentry.io/6150815",
   integrations=[TornadoIntegration()]
)

# Your app code here, without changes

class MyHandler(...):
```



#### Refrences:
- [Using Sentry With Flask to Log Errors](https://www.youtube.com/watch?v=zVW83QUSDdQ)
- [Prepare the Tornado SDK](https://sentry.io/onboarding/no-org-0u/get-started/)
