"""
Cached REST requests for json data basically
"""

import functools

import requests
from django.core.cache import cache

# a week
DEFAULT_TIMEOUT = 7 * 24 * 60 * 60

class Rest():
    def __init__(self, endpoint, timeout=DEFAULT_TIMEOUT, **kwargs):
        """
        Creates a new REST API endpoint.

        endpoint is a url with optional printf style placeholders. those will be
        replaced when the api is queried with the get method.

        timeout specifies how long successful results should be cached in
        seconds.

        any additional key word arguments are passed donw to the requests
        library in each request. This allows for the easy specification of
        autzorization tokens (Rest(..., headers={'authorization':'...'}))
        """
        self.endpoint = endpoint
        self.timeout = timeout
        self.kwargs = kwargs

    def get(self, identifier, **kwargs):
        """
        Makes a request for the object identified by identifier.

        identifier can also be a tuple if the endpoint contains more than one
        placeholder.

        additional key word arguments override the generic arguments specified
        in the constructor.

        Returns the (possibly cached) result of the query on success and throws
        an exception in case of a connection error.
        """
        url = self.endpoint % identifier
        return cache.get_or_set(url, functools.partial(self._req, url, kwargs),
                self.timeout)

    def _req(self, url, kwargs):
        # update default kwargs with request specific kwargs
        kwargs = dict(self.kwargs, **kwargs)
        r = requests.get(url, **kwargs)
        # make sure that we don't cache failures
        r.raise_for_status()
        return r.json()
