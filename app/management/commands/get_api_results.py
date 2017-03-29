import functools
import importlib
import json
import os
from unittest.mock import Mock

from django.core.management.base import BaseCommand, CommandError

import app

class Command(BaseCommand):
    args = '<provider provider ...>'
    help = 'Extends the test data with the current api results. Useful when creating or extending providers'

    def getCurrentTestData(self, provider, item):
        original_api = provider.embed.__defaults__[0]
        api = Mock(wraps=original_api)
        sub = Mock()
        sub.url = item['url']
        result = provider.embed(sub, api)
        call, *others = api.mock_calls
        assert not others
        name, args, kwargs = call
        assert name == ''
        assert not kwargs
        assert len(args) == 1
        api_params = args[0]
        # I don't know how to get the result from a wrapped mock call :/
        api_result = original_api(api_params)
        return {
            'url' : item['url'],
            'api_params' : api_params,
            'api_result' : api_result,
            'expected' : result
        }

    def overwriteTestData(self, provider):
        name = provider.__name__
        app_path = os.path.dirname(os.path.abspath(app.__file__))
        data_file = os.path.join("test_data", "{0}.json".format(name))
        data_path = os.path.join(app_path, data_file)
        with open(data_path, "r+") as f:
            data = json.load(f)
            f.seek(0)
            new_data = list(map(functools.partial(
                    self.getCurrentTestData, provider), data))
            json.dump(new_data, f, sort_keys=True, indent=2)
            f.truncate()

    def add_arguments(self, parser):
        parser.add_argument('provider_module', nargs='+', type=str)

    def handle(self, *args, **options):
        for provider_name in options['provider_module']:
            provider = importlib.import_module(provider_name)
            self.overwriteTestData(provider)
