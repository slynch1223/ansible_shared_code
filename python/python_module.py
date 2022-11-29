#!/user/bin/python
DOCUMENTATION = r"""
---
module: 'python_module'

author: 'slynch1223@gmail.com'

description: 'This is an example template for python based Ansible modules'

version_added: '2.9'

options:
    bool_var:
        description: 'This is a boolean parameter'
        required: false
        default: true
        type: bool

    string_var:
        description: 'This is a string parameter'
        required: true
        type: str

    password_var:
        description: 'This is a password parameter'
        required: true
        type: str
"""

RETURN = r"""
out_var:
    description: 'This returns some output for later use'
    type: str
"""

EXAMPLES = r"""
---
- name: 'Sample Python Module'
  python_module:
    bool_var: true
    string_var: 'This is a sample message'
    password_var: '{{ some_password }}'
"""

from ansible.module_utils.basic import AnsibleModule

module = AnsibleModule(
    argument_spec=dict(
        bool_var=dict(type="bool", default=True),
        string_var=dict(type="str", required=True),
        username=dict(type="str", required=True),
        password=dict(type="str", required=True, no_log=True),
    ),
    supports_check_mode=False,
)

bool_var = module.params["bool_var"]
string_var = module.params["string_var"]
username = module.params["username"]
password = module.params["password"]

result = dict(changed=False, msg="")

import requests

#################################################################################


def http_basic_auth_get(url):
    try:
        req = requests.get(url=url, auth=(username, password))

        if not req.ok:
            result["json"] = str(req.json())
            result["msg"] = req.reason
            module.fail_json(**result)
        return req.json()
    except Exception as err:
        result["msg"] = str(err)
        module.fail_json(**result)


def http_basic_auth_post(url, body):
    try:
        req = requests.post(url=url, auth=(username, password), verify=False, json=body)

        if not req.ok:
            print(str(req.json()))
            print(req.reason)
        return req.json()
    except Exception as err:
        print(str(err))
        print(req.reason)


#################################################################################


def main():
    global result

    # Perform a search query against a Web API
    search = http_basic_auth_get("https://someurl/api?query=" + "some query string")

    # Check results
    if "results" in search.keys() and type(search["results"]) is list and len(search["results"]) > 0:
        for x in search["results"]:
            result["search"] = x
            result["changed"] = True
            result["msg"] = "Found something"
            http_basic_auth_post("https://someurl/api/insertUpdate", {"key1": "value1", "key2": True})
            break

    module.exit_json(**result)


if __name__ == "__main__":
    main()
