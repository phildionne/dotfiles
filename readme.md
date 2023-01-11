## Getting started

```bash
cd & git clone https://github.com/phildionne/dotfiles
```

## Brew

Install [brew](https://brew.sh/)

```bash
# Upgrade outdated casks and outdated, unpinned formulae
brew upgrade

# Remove stale lock files and outdated downloads for all formulae and casks, and remove old versions of installed formulae
# -s Scrub the cache, including downloads for even the latest versions.
brew cleanup -s

# Uninstall formulae that were only installed as a dependency of another formula and are now no longer needed
brew autoremove

# Upgrade outdated casks
brew upgrade $(brew outdated --cask --greedy --quiet)
```

## Terminal

### Zsh

While latest macOS versions have Zsh already installed, it's best to install it with brew to get the latest and keep it updated.

```bash
brew install zsh
```

### Warp

Then install [Warp](https://warp.dev).

```bash
brew install warp
```

## Utilities

```bash
brew install \
  asdf \
  doctl \
  yarn \
  tmux \
  overmind \
  redis
```

- [asdf](https://github.com/asdf-vm/asdf) for managing programming language versions
- [yarn](https://yarnpkg.com/) for managing JavaScript packages
- [doctl](https://github.com/digitalocean/doctl) for interacting with the Digital Ocean API
- [overmind](https://github.com/DarthSim/overmind) for managing Procfile-based applications
- [tmux](https://tmux.github.io/) for saving project state and switching between projects
- [redis](http://redis.io/) for storing key-value data

## Git

- [hub](https://github.com/github/hub) for interacting with the GitHub API
- [Git Credentials Manager](https://docs.github.com/en/get-started/getting-started-with-git/caching-your-github-credentials-in-git#git-credential-manager-core)

```bash
brew install hub

brew tap microsoft/git
brew install --cask git-credential-manager-core
```

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
brew install --cask \
  visual-studio-code \
  github \
  dash \
  ngrok \
  postman
```

- [Visual Studio Code](https://code.visualstudio.com/)
- [Github Desktop](https://desktop.github.com/)
- [Dash](https://kapeli.com/dash)
- [ngrok](https://ngrok.com/)
- [Postman](https://www.postman.com/)

### Database

- [Postgres.app](https://postgresapp.com/) PostgreSQL database
- [Sequel](https://www.sequelpro.com/) MySQL GUI
- [Postico](https://eggerapps.at/postico/) PostgreSQL GUI
- [Base](https://menial.co.uk/base/) SQLite3 GUI

```bash
brew install --cask \
  postgres-unofficial \
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
brew install --cask \
  appcleaner \
  bitwarden \
  dropbox \
  google-chrome \
  messenger \
  slack \
  raycast \
  spotify \
  the-unarchiver \
  vlc \
  webtorrent
```

### Docker

Install docker:

```bash
brew install --cask docker
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

#### Quick Look

Adds support for:

- Preview source code files with syntax highlighting
- Preview plain text files without or with unknown file extension
- Preview Markdown files
- Preview JSON files

```bash
brew install \
  qlcolorcode \
  qlstephen \
  qlmarkdown \
  quicklook-json
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
2. Enable [FileVault](https://github.com/drduh/macOS-Security-and-Privacy-Guide#full-disk-encryption)
3. Disable [spotlight suggestions](https://github.com/drduh/OS-X-Yosemite-Security-and-Privacy-Guide#spotlight-suggestions)
4. Configure [PGP/GPG](https://github.com/drduh/macOS-Security-and-Privacy-Guide#pgpgpg)
5. Use latest OpenSSL: `brew install openssl`
6. Use curl with openssl: `brew install curl --with-openssl && brew link --force curl`
7. Use [NextDNS](https://nextdns.io)
