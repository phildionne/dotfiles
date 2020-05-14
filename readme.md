## Getting started
```bash
cd & git clone https://github.com/phildionne/dotfiles
```

## Shell

### Zsh

Install [ohmyzsh](https://github.com/ohmyzsh/ohmyzsh) and pick useful plugins. Mines are:

- [bundler](https://github.com/ohmyzsh/ohmyzsh/tree/master/plugins/bundler)

### Theme

Use [Pure](https://github.com/sindresorhus/pure)

```bash
yarn global add pure-prompt
```

## Utilities

Use [brew](https://brew.sh/):

```bash
brew install \
  hub \
  asdf \
  doctl \
  yarn \
  tmux \
  overmind \
  redis
```

* [hub](https://github.com/github/hub) for interacting with the GitHub API
* [asdf](https://github.com/asdf-vm/asdf) for managing programming language versions
* [yarn](https://yarnpkg.com/) for managing JavaScript packages
* [doctl](https://github.com/digitalocean/doctl) for interacting with the Digital Ocean API
* [overmind](https://github.com/DarthSim/overmind) for managing Procfile-based applications
* [tmux](https://tmux.github.io/) for saving project state and switching between projects
* [redis](http://redis.io/) for storing key-value data

## Apps

Use [brew cask](https://github.com/caskroom/homebrew-cask):

### Development

```bash
brew cask install \
  github \
  dash \
  iterm2 \
  ngrok \
  postman

brew cask install visual-studio-code # or
brew cask install atom
```

* [Github Desktop](https://desktop.github.com/)
* [Dash](https://kapeli.com/dash)
* [iterm2](https://www.iterm2.com/)
* [ngrok](https://ngrok.com/)
* [Postman](https://www.postman.com/)

### Database

* [Postgres.app](https://postgresapp.com/) PostgreSQL database
* [Sequel](https://www.sequelpro.com/) MySQL GUI
* [Postico](https://eggerapps.at/postico/) PostgreSQL GUI
* [Base](https://menial.co.uk/base/) SQLite3 GUI

```bash
brew cask install \
  postgres \
  sequel-pro \
  postico \
  base
```

### Other

```bash
brew cask install \
  appcleaner \
  bitwarden \
  dropbox \
  google-backup-and-sync \
  google-chrome \
  sketch \
  slack      \
  rectangle \
  spotify \
  the-unarchiver
```

### Docker

Install docker:

```bash
brew cask install docker
```

### Atom

Overwrite Atom preferences with your own:

```bash
ln -s $HOME/dotfiles/atom/* $HOME/.atom/
```

### Erlang & Elixir

Install [erlang-history](https://github.com/ferd/erlang-history) to enable history in the elixir & erlang interactive consoles.

### Everything else

- `.git_config`
- `.global_ignore`
- `.gemrc`
- `.irbrc`
- `.pryrc`
- `.rspec`

Create symlinks to your dotfiles in `~`.

```bash
cd ~/dotfiles
rake install
```

### OSX

#### Defaults

Set OSX defaults:

```bash
source $HOME/dotfiles/osx/set-defaults.sh
```

*optional* - Allow to [write](http://apple.stackexchange.com/questions/152661/write-to-ntfs-formated-drives-on-yosemite) to ntfs formated drives:

```bash
brew install homebrew/fuse/ntfs-3g
sudo mv /sbin/mount_ntfs /sbin/mount_ntfs.original
sudo ln -s /usr/local/sbin/mount_ntfs /sbin/mount_ntfs
```

#### Security

Make you mac secure; mostly taken from [this guide](https://github.com/drduh/OS-X-Yosemite-Security-and-Privacy-Guide).

1. Enable [firewall](https://github.com/drduh/OS-X-Yosemite-Security-and-Privacy-Guide#firewall)
2. Disable [spotlight suggestions](https://github.com/drduh/OS-X-Yosemite-Security-and-Privacy-Guide#spotlight-suggestions)
3. Configure [hosts file](https://github.com/drduh/OS-X-Yosemite-Security-and-Privacy-Guide#hosts-file); I use [this one](http://someonewhocares.org/hosts/zero/hosts).
4. Use latest OpenSSL: `brew install openssl`
5. Use curl with openssl: `brew install curl --with-openssl && brew link --force curl`
6. Deactivate Chrome's Flash plugin by visiting `chrome://plugins/`
7. Use CloudFlare's DNS [1.1.1.1](https://1.1.1.1/)
