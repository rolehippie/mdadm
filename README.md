# mdadm

[![Build Status](https://cloud.drone.io/api/badges/rolehippie/mdadm/status.svg)](https://cloud.drone.io/rolehippie/mdadm)

Ansible role to configure mdadm

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

- None

## License

Apache-2.0

## Author

[Thomas Boerger](https://github.com/tboerger)
