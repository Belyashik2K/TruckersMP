import ssl
import certifi

from typing import Optional
from aiohttp import ClientSession, TCPConnector

from .exceptions.HTTPError import HTTPError
from .exceptions.TruckersMPError import TruckersMPError

class HTTPClient:
    """Represents an HTTP client sending HTTP requests to the API."""

    def __init__(self) -> None:
        """Initialize the HTTPClient."""
        self._method = 'GET'

    async def __aenter__(self, *args, **kwargs) -> None:
        """Create a new session."""
        ssl_context = ssl.create_default_context(cafile=certifi.where())
        connector = TCPConnector(ssl=ssl_context)
        self._session = ClientSession(connector=connector)

    async def __aexit__(self, *args, **kwargs) -> None:
        """Close the session."""
        await self._session.close()

    async def _request(self, url: str, **kwargs) -> Optional[dict]:
        """Make a request to the API."""
        async with self:
            response = await self._session.request(self._method, url, **kwargs)
            """Check if the response is 200, if not, raise an exception."""
            if response.status == 200:
                """Check if the response contains an error."""
                return self.__check_exception(await response.json())
            else:
                """If the response code is not 200, then raise an exception."""
                raise HTTPError("An error with code " + response.status + " occurred while fetching data from " + url)

    def __check_exception(self, response: dict) -> None:
        """Check if the response contains an error."""
        try:
            """If the response contains an error, then raise an exception."""
            if response['error']:
                raise TruckersMPError(response['descriptor'])
        except KeyError:
            """If the response doesn't contain an error, then site is up."""
            pass

        try:
            """If the response contains a response key, then return it."""
            return response['response']
        except KeyError:
            """If the response doesn't contain a response, then return all response."""
            return response