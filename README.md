Ansible Lookup Plug-in for Libsecret
=========

A module that allows Ansible to lookup secrets using the Libsecret API.

Requirements
------------

In order to use this role you'll need.

* Libsecret and its python bindings installed.
* A provider (like GNOME Keyring) for the Libsecret service.

Role Variables
--------------

This plug-in does not depend on any external variables.

Deficiencies
------------

* Can only use the default `Secret.Service` proxy. [Ref](https://lazka.github.io/pgi-docs/Secret-1/classes/Service.html#Secret.Service.get_sync)

Examples
--------

Create a secret for use with this plug-in.

    secret-tool store --label "Example" key1 value1 key2 value2

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - ansible-plugin-libsecret
      tasks:
         - debug:
	     msg: "{{ lookup('libsecret', { 'key1': 'value1', 'key2': 'value2' }) }}"

Here's an example of the return value.

    {
      'label': 'Example',
      'created': 1552586144,
      'modified': 1552586144,
      'schema': 'org.freedesktop.Secret.Generic',
      'is_locked': False,
      'attrs': {
        'xdg:schema': 'org.freedesktop.Secret.Generic',
        'key1': 'value1',
        'key2': 'value2'
      },
      'secret': {
        'content_type': 'text/plain',
        'data': b'Ex@mp1e',
	'text': 'Ex@mp1e'
      }
    }

License
-------

GPLv3+

References and Thanks
---------------------

I would have had no idea how to write this thing without:

* The [source](https://gitlab.gnome.org/GNOME/libsecret/) for Libsecret.
* The [source](https://gitlab.gnome.org/GNOME/libsecret/tree/master/tool) for `secret-tool`.
* The [API reference](https://developer.gnome.org/libsecret/unstable/complete.html) for Libsecret.
* The [API reference](https://lazka.github.io/pgi-docs/#Secret-1) for the Python bindings.
* The [`dict` lookup plug-in](https://github.com/ansible/ansible/blob/devel/lib/ansible/plugins/lookup/dict.py).
* The [Ansible docs](https://docs.ansible.com/ansible/latest/user_guide/playbooks_reuse_roles.html#embedding-modules-and-plugins-in-roles) for embedding plug-ins in roles.
* The [Ansible docs](https://docs.ansible.com/ansible/latest/dev_guide/developing_plugins.html#lookup-plugins) for lookup plug-ins.

Author Information
------------------

* Estelle Poulin <dev@inspiredby.es>
