# mdadm

[![Source Code](https://img.shields.io/badge/github-source%20code-blue?logo=github&logoColor=white)](https://github.com/rolehippie/mdadm) [![General Workflow](https://github.com/rolehippie/mdadm/actions/workflows/general.yml/badge.svg)](https://github.com/rolehippie/mdadm/actions/workflows/general.yml) [![Readme Workflow](https://github.com/rolehippie/mdadm/actions/workflows/readme.yml/badge.svg)](https://github.com/rolehippie/mdadm/actions/workflows/readme.yml) [![Galaxy Workflow](https://github.com/rolehippie/mdadm/actions/workflows/galaxy.yml/badge.svg)](https://github.com/rolehippie/mdadm/actions/workflows/galaxy.yml) [![License: Apache-2.0](https://img.shields.io/github/license/rolehippie/mdadm)](https://github.com/rolehippie/mdadm/blob/master/LICENSE) [![Ansible Role](https://img.shields.io/ansible/role/51431)](https://galaxy.ansible.com/rolehippie/mdadm)

Ansible role to install and configure mdadm RAID manager.

## Sponsor

Building and improving this Ansible role have been sponsored by my current and previous employers like **[Cloudpunks GmbH](https://cloudpunks.de)** and **[Proact Deutschland GmbH](https://www.proact.eu)**.

## Table of content

- [Default Variables](#default-variables)
  - [mdadm_arrays](#mdadm_arrays)
  - [mdadm_homehost](#mdadm_homehost)
  - [mdadm_mailaddr](#mdadm_mailaddr)
- [Discovered Tags](#discovered-tags)
- [Dependencies](#dependencies)
- [License](#license)
- [Author](#author)

---

## Default Variables

### mdadm_arrays

List of docker registries to auto login

#### Default value

```YAML
mdadm_arrays: []
```

#### Example usage

```YAML
mdadm_arrays:
  - number: 0
    level: 1
    filesystem: ext4
    mountpoint: /var/lib/foo
    devices:
      - /dev/sdb
      - /dev/sdc
```

### mdadm_homehost

Hostname for the mdadm config

#### Default value

```YAML
mdadm_homehost: '{{ inventory_hostname }}'
```

### mdadm_mailaddr

#### Default value

```YAML
mdadm_mailaddr: root
```

## Discovered Tags

**_mdadm_**

**_skip_ansible_later_**


## Dependencies

- None

## License

Apache-2.0

## Author

[Thomas Boerger](https://github.com/tboerger)
