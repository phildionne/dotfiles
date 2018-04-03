## Getting started
```bash
cd & git clone https://github.com/phildionne/dotfiles
```

### Bash
Install [bash-it](https://github.com/revans/bash-it) and pick useful completions and plugins. Mines are:

#### Aliases
- General

#### Plugins
none

#### Completions
- Defaults

### Apps

Use [brew cask](https://github.com/caskroom/homebrew-cask):

```bash
brew cask install appcleaner \
atom \
dash \
dropbox \
evernote \
github \
google-chrome \
gpg \
harvest \
iterm2 \
keybase \
postgres \
postico \
postman \
sketch \
skype \
slack \
spectacle \
spotify
```

### Utilities

Use [brew](https://brew.sh/):

```bash
brew install curl hub
```

### Package managers

```bash
brew install pyenv rbenv jenv
brew install yarn --without-node
```

Install [nvm](https://github.com/creationix/nvm) for managing Node versions.

### Docker

Install docker with Virtual Box:

```bash
brew cask install virtualbox
brew install docker docker-machine

docker-machine create default
```

### Atom

Overwrite Atom preferences with your own:

```bash
ln -s $HOME/dotfiles/atom/* $HOME/.atom/
```

### Erlang & Elixir

Install [erlang-history](https://github.com/ferd/erlang-history) to enable history in the elixir & erlang interactive consoles.


### Everything else

- `.bash_profile`
- `.git_config`
- `.global_ignore`
- `.gemrc`
- `.irbrc`
- `.pryrc`
- `.rspec`

Create symlinks to your dotfiles in `~`. This will overwrite `~/.bash_profile` created by bash-it.

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

Allow to [write](http://apple.stackexchange.com/questions/152661/write-to-ntfs-formated-drives-on-yosemite) to ntfs formated drives:

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
