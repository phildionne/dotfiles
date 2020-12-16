## Getting started

```bash
cd & git clone https://github.com/phildionne/dotfiles
```

## Shell

### Zsh

Install [ohmyzsh](https://github.com/ohmyzsh/ohmyzsh) and pick useful plugins. Mines are:

- [bundler](https://github.com/ohmyzsh/ohmyzsh/tree/master/plugins/bundler)
- [zsh-interactive-cd](https://github.com/ohmyzsh/ohmyzsh/tree/master/plugins/zsh-interactive-cd)

### Theme

Use [Pure](https://github.com/sindresorhus/pure) with the [snazzy](https://github.com/sindresorhus/iterm2-snazzy) theme.

```bash
yarn global add pure-prompt
```

Install [snazzy](https://github.com/sindresorhus/iterm2-snazzy#install) for iterm2.

### Dependencies

- [ohmyzsh](https://github.com/ohmyzsh/ohmyzsh)
- [fzf](https://github.com/junegunn/fzf#using-homebrew-or-linuxbrew) required by `zsh-interactive-cd`

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

## Languages

```bash
asdf plugin add ruby
asdf plugin add nodejs

asdf install ruby latest
asdf install nodejs latest
```

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

#### Postgres.app

Configure your `$PATH` to use the included command line tools:

```bash
sudo mkdir -p /etc/paths.d &&
echo /Applications/Postgres.app/Contents/Versions/latest/bin | sudo tee /etc/paths.d/postgresapp
```

See:
- https://postgresapp.com/documentation/install.html

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

#### Quick Look

Adds support for:

- Preview source code files with syntax highlighting
- Preview plain text files without or with unknown file extension
- Preview Markdown files
- Preview JSON files

```bash
brew install qlcolorcode qlstephen qlmarkdown quicklook-json
```

See: https://github.com/sindresorhus/quick-look-plugins

#### Other

_optional_ - Allow to [write](http://apple.stackexchange.com/questions/152661/write-to-ntfs-formated-drives-on-yosemite) to ntfs formated drives:

```bash
brew install homebrew/fuse/ntfs-3g
sudo mv /sbin/mount_ntfs /sbin/mount_ntfs.original
sudo ln -s /usr/local/sbin/mount_ntfs /sbin/mount_ntfs
```

#### Security

Make you mac secure; mostly taken from [this guide](https://github.com/drduh/OS-X-Yosemite-Security-and-Privacy-Guide).

1. Enable [firewall](https://github.com/drduh/OS-X-Yosemite-Security-and-Privacy-Guide#firewall)
3. Enable [FileVault](https://github.com/drduh/macOS-Security-and-Privacy-Guide#full-disk-encryption)
3. Disable [spotlight suggestions](https://github.com/drduh/OS-X-Yosemite-Security-and-Privacy-Guide#spotlight-suggestions)
4. Configure [PGP/GPG](https://github.com/drduh/macOS-Security-and-Privacy-Guide#pgpgpg)
5. Use latest OpenSSL: `brew install openssl`
6. Use curl with openssl: `brew install curl --with-openssl && brew link --force curl`
7. Use [NextDNS](https://nextdns.io)
