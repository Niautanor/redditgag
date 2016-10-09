"""
The default provider which will *always* return an embeddable sorry post
"""

from urllib.parse import urlparse
import operator

SORRY_TEMPLATE = """
There currently isn't a way to embed this link from the domain %s.
Maybe someone will send the developer a pull request to fix this ;)
"""
# contains a mapping of domains to a set of urls (belonging to this domain)
# we can later count the urls and so compute the number of unresolved requests
# to this domain
unembedded_domains = dict()

def embed(submission):
    domain = urlparse(submission.url).netloc

    # default value will be the empty set. 
    unembedded_domains[domain] = unembedded_domains.get(domain, set())
    unembedded_domains[domain].add(submission.url)

    return {
        'kind' : 'SORRY',
        'sorrytext' : SORRY_TEMPLATE % domain
    }

# sort the dict by values and returns it
def get_unsupported_domains():
	counted_domains = dict()
	for domain in unembedded_domains.keys():
		counted_domains[domain] = len(unembedded_domains[domain])
	return reversed(sorted(counted_domains.items(), key=operator.itemgetter(1)))
