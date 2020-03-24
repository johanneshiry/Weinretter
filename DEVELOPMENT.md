# Weinretter Development Environment

## Start VM

```
vagrant up
```

## Deploy code changes to VM

```
vagrant provision
```

This rebuilds the containers inside VM and starts the frontend container on port 443 HTTPS of VM IP address using a snakeoil certificate.

Use `vagrant ssh-config` to show the IP address of VM or `vagrant ssh` to connect via SSH.


## Use libvirt instead of VirtualBox

```
cp dev/config.yml dev/config.local.yml
```

change provider to libvirt in `dev/config.local.yml`