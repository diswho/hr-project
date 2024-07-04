# Start Service

```bash
sudo service docker start
```

# Unprivileged namespaces

`sudo sysctl -w kernel.apparmor_restrict_unprivileged_unconfined=0`

`sudo sysctl -w kernel.apparmor_restrict_unprivileged_userns=0`

## Launch Docker Desktop

```
systemctl --user start docker-desktop
```

## To stop Docker Desktop

```
systemctl --user stop docker-desktop
```

### To enable Docker Desktop to start on sign in

`systemctl --user enable docker-desktop`

## Upgrade Docker Desktop

```
sudo apt-get install ./docker-desktop-<version>-<arch>.deb
```
## Local Development

* Start the stack with Docker Compose:

```bash
docker compose up -d
```