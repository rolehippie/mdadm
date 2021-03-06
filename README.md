# mdadm

[![Source Code](https://img.shields.io/badge/github-source%20code-blue?logo=github&logoColor=white)](https://github.com/rolehippie/mdadm) [![Build Status](https://img.shields.io/drone/build/rolehippie/mdadm/master?logo=drone)](https://cloud.drone.io/rolehippie/mdadm) [![License: Apache-2.0](https://img.shields.io/github/license/rolehippie/mdadm)](https://github.com/rolehippie/mdadm/blob/master/LICENSE) 

Ansible role to install and configure mdadm RAID manager. 

## Sponsor 

[![Proact Deutschland GmbH](https://proact.eu/wp-content/uploads/2020/03/proact-logo.png)](https://proact.eu) 

Building and improving this Ansible role have been sponsored by my employer **Proact Deutschland GmbH**.

## Table of content

* [Default Variables](#default-variables)
  * [mdadm_arrays](#mdadm_arrays)
  * [mdadm_homehost](#mdadm_homehost)
  * [mdadm_mailaddr](#mdadm_mailaddr)
* [Dependencies](#dependencies)
* [License](#license)
* [Author](#author)

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

## Dependencies

* None

## License

Apache-2.0

## Author

[Thomas Boerger](https://github.com/tboerger)
