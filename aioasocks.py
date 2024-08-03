from typing import Literal
from aiohttp import ClientSession, ClientResponse


class HTTPClient:
    REQUEST_TYPE = Literal["GET", "POST", "DELETE", "PUT", "HEAD", "OPTIONS", "PATCH"]
    __instance = None
    
    def __new__(cls):
        if cls.__instance is None and cls.base_url:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        self.session = ClientSession(
            headers=dict(ContentType='application/json'))

    async def _request(self, 
                      req_type: REQUEST_TYPE,
                      **kwargs):
        try:
            request = getattr(self.session, req_type.lower()) 
            async with request(**kwargs) as resp: 
                resp: ClientResponse
            await self.session.close()
            if resp.status == 200:
                return await resp.json()
            else:
                return False
        except Exception as e:
            print(e)


class AsocksDir(HTTPClient):
    def __init__(self, api_key: str):
        self.base_url = "https://api.asocks.com"
        self.api_str = f"?apiKey={api_key}"
        super().__init__()

    # dir
    async def dir_countries(self):
        return await self._request(
            req_type="GET",
            url=self.base_url + '/v2/dir/countries/' + self.api_str
            )

    async def dir_states(self, params: dict):
        return await self._request(
            req_type="GET",
            url=self.base_url + '/v2/dir/states/' + self.api_str,
            params=params
            )

    async def dir_cities(self, params: dict):
        return await self._request(
            req_type="GET",
            url=self.base_url + '/v2/dir/cities/' + self.api_str,
            params=params
            )

    async def dir_asns(self, params: dict):
        return await self._request(
            req_type="GET",
            url=self.base_url + '/v2/dir/asns/' + self.api_str,
            params=params
            )


class AsocksProxy(HTTPClient):
    def __init__(self, api_key: str):
        self.base_url = "https://api.asocks.com"
        self.api_str = f"?apiKey={api_key}"
        super().__init__()

    # plan
    async def plan_info(self):
        return await self._request(
            req_type="GET",
            url=self.base_url + '/v2/plan/info/' + self.api_str
            )

    # user
    async def user_balance(self):
        return await self._request(
            req_type="GET",
            url=self.base_url + '/v2/user/balance/' + self.api_str
            )

    #proxy
    async def search(self, params: dict):
        return await self._request(
            req_type="GET",
            url=self.base_url + '/v2/proxy/search/' + self.api_str,
            params=params
            )
    
    async def ports(self, params: dict):
        return await self._request(
            req_type="GET",
            url=self.base_url + '/v2/proxy/ports/' + self.api_str,
            params=params
            )

    async def create_port(self, data: dict):
        return await self._request(
            req_type="POST",
            url=self.base_url + '/v2/proxy/create-port/' + self.api_str,
            data=data
            )

    async def delete_port(self, params: dict):
        return await self._request(
            req_type="DELETE",
            url=self.base_url + '/v2/proxy/delete-port/' + self.api_str,
            params=params
            )

    async def archive_port(self, params: dict):
            return await self._request(
                req_type="PATCH",
                url=self.base_url + '/v2/proxy/archive-port/' + self.api_str,
                params=params
                )

    async def refresh(self, params: dict):
            return await self._request(
                req_type="GET",
                url=self.base_url + '/v2/proxy/refresh/' + self.api_str,
                params=params
                )
    async def port_info(self, params: dict):
        return await self._request(
            req_type="GET",
            url=self.base_url + '/v2/proxy/port-info/' + self.api_str,
            params=params
            )

    async def change_name(self, params: dict, data: dict):
        return await self._request(
            req_type="PATCH",
            url=self.base_url + '/v2/proxy/change-name/' + self.api_str,
            params=params,
            data=data
            )

    async def total_spent_traffic(self):
        return await self._request(
            req_type="GET",
            url=self.base_url + '/v2/proxy/total-spent-traffic/' + self.api_str
            )


class AsocksTemplates(HTTPClient):
    def __init__(self, api_key: str):
        self.base_url = "https://api.asocks.com"
        self.api_str = f"?apiKey={api_key}"
        super().__init__()

    # template
    async def proxy_template(self, params: dict):
        return await self._request(
            req_type="GET",
            url=self.base_url + '/v2/proxy-template/' + self.api_str,
            params=params
            )

    async def create_template(self, data: dict):
        return await self._request(
            req_type="POST",
            url=self.base_url + '/v2/proxy-template/create-template' + self.api_str,
            data=data
            )

    async def update_template(self, params: dict):
        return await self._request(
            req_type="PATCH",
            url=self.base_url + '/v2/proxy-template/update-template' + self.api_str,
            params=params
            )

    async def delete_template(self, params: dict):
        return await self._request(
            req_type="DELETE",
            url=self.base_url + '/v2/proxy-template/delete-template' + self.api_str,
            params=params
            )


class AsocksWhitelist(HTTPClient):
    def __init__(self, api_key: str):
        self.base_url = "https://api.asocks.com"
        self.api_str = f"?apiKey={api_key}"
        super().__init__()

    # whitelist
    async def add(self, data: dict):
        return await self._request(
            req_type="POST",
            url=self.base_url + '/v2/whitelist/add/' + self.api_str,
            data=data
            )
    
    async def delete(self, params: dict):
        return await self._request(
            req_type="DELETE",
            url=self.base_url + '/v2/whitelist/delete/' + self.api_str,
            params=params
            )


class AsocksClient:
    def __init__(self, api_key: str):
        self.dir = AsocksDir(api_key=api_key)
        self.proxy = AsocksProxy(api_key=api_key)
        self.templates = AsocksTemplates(api_key=api_key)
        self.whitelist = AsocksWhitelist(api_key=api_key)
