import os
import types
import functools

from unittest.mock import Mock
from django.test import TestCase
from ddt import ddt, file_data, unpack

from app import rest
from app.providers import imgur, tumblr, deviantart, gfycat

def testProvider(
        self, provider, submission, api_params, api_result, expected):
    api = Mock(spec_set=types.FunctionType, return_value=api_result)
    if isinstance(api_params, list):
        # json cannot store tuples
        api_params = tuple(api_params)
    actual = provider.embed(submission, api)
    api.assert_called_once_with(api_params)
    self.assertEqual(actual, expected)

def testUrlBasedProvider(
        self, provider, url, api_params, api_result, expected):
    submission = Mock(spec_set=["url"])
    submission.url = url
    testProvider(self, provider, submission, api_params, api_result, expected)

def addUrlProviderTestCase(cls, provider):
    name = provider.__name__
    dataFile = os.path.join("test_data", "{0}.json".format(name))
    funcName = "test{0}".format(name.title())
    # I would like to use functools.partial like this
    # func = functools.partial(testUrlBasedProvider, provider=provider)
    # but unfortunately functools.partial is rather dumb and wouldn't
    # remove the provider argument from the function call :/
    def func(self, url, api_params, api_result, expected):
        return testUrlBasedProvider(
                self, provider, url, api_params, api_result, expected)
    setattr(cls, funcName, file_data(dataFile)(func))

def addUrlProviderTests(*providers):
    def decorator(cls):
        for provider in providers:
            addUrlProviderTestCase(cls, provider)
        return cls
    return decorator

# Create your tests here.
@ddt
@addUrlProviderTests(imgur, tumblr, gfycat, deviantart)
class TestProviders(TestCase):
    pass
