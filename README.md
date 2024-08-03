# aioasocks
aioasocks it's simple asynchronous Python SDK for [asocks.com](https://asocks.com/) public API
## Quickstart

```python
from aioasocks import AsocksClient

async def main():
    asocks = AsocksClient(api_key="<YOUR_API_KEY>")
    resp = asocks.proxy.create_port(
        params=dict(country_code="RU",
                    type_id=1,
                    proxy_type_id=2,
                    name="proxy_name"
    ))
```
## Contacts
**Telegram:** [@TheDinAlt](t.me/TheDinAlt)
