"""
The default provider which will *always* return an embeddable sorry post
"""

from urllib.parse import urlparse
import operator

SORRY_TEMPLATE = """
There currently isn't a way to embed this link from the domain <a href="%s">%s</a>.
Maybe someone will send the developer a pull request to fix this ;)
"""
# contains a mapping of domains to a set of urls (belonging to this domain)
# we can later count the urls and so compute the number of unresolved requests
# to this domain
unembedded_domains = {}

def embed(submission):
    domain = ".".join(urlparse(submission.url).netloc.split(".")[-2:])

    # default value will be the empty set.
    unembedded_domains[domain] = unembedded_domains.get(domain, set())
    unembedded_domains[domain].add(submission.url)

    return {
        'kind' : 'SORRY',
        'sorrytext' : SORRY_TEMPLATE % (submission.url, domain)
    }

# sort the dict by values and returns it
def get_unsupported_domains():
    counted_domains = {}
    for domain, links in unembedded_domains.items():
        counted_domains[domain] = len(links)
    return reversed(sorted(counted_domains.items(),
                           key=operator.itemgetter(1)))
