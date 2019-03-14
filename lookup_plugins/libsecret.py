#! /usr/bin/env python
"""Ansible lookup plug-in for libsecret."""

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
from ansible.plugins.lookup import LookupBase

from gi.repository import Secret

DOCUMENTATION = """
      lookup: libsecret
        author: Estelle Poulin <dev@inspiredby.es>
        version_added: "2.8"
        short_description: Lookup passwords in libsecret.
        description:
            - Lookup returns the password from a libsecret entry.
        options:
          _terms:
            description: A list of dicts where each dict represents the 
            attributes to search on.
            required: True
"""


class LookupModule(LookupBase):
    """Lookup Plugin for libsecret."""

    def run(self, terms, variables=None, **kwargs):
        """Entrypoint for a lookup plugin."""
        ret = []
        service = Secret.Service.get_sync(
            Secret.ServiceFlags.OPEN_SESSION |    
            Secret.ServiceFlags.LOAD_COLLECTIONS, None)

        for term in terms:
            ret_item = {}
            results = service.search_sync(
                None,
                term,
                Secret.SearchFlags.ALL |
                Secret.SearchFlags.UNLOCK |
                Secret.SearchFlags.LOAD_SECRETS,
                None)

            for result in results:

                ret_item = {
                    'label': result.get_label(),
                    'created': result.get_created(),
                    'modified': result.get_modified(),
                    'schema': result.get_schema_name(),
                    'is_locked': result.get_locked(),
                    'attrs': result.get_attributes(),
                }

                secret = result.get_secret()
                if secret:
                    ret_item['secret'] = {
                        'content_type': secret.get_content_type(),
                        'data': secret.get(),
                        'text': secret.get_text(),
                    }
                else:
                    ret_item['secret'] = None

                ret.append(ret_item)

        return ret
