## Getting started

```bash
cd & git clone https://github.com/phildionne/dotfiles
```

## Brew

Install [brew](https://brew.sh/)

## Terminal

### Iterm2

Use Iterm2

```bash
brew install --cask iterm2
```

### Zsh

While latest macOS versions have Zsh already installed, it's best to install it with brew to get the latest and keep it updated.

```bash
brew install zsh
```

### Pure

Use the [Pure](https://github.com/sindresorhus/pure) prompt

```bash
brew install pure
```

- Use the [snazzy theme](https://github.com/sindresorhus/iterm2-snazzy) with iTerm2
- Use [zsh-syntax-highlighting](https://github.com/zsh-users/zsh-syntax-highlighting)

## ASDF

Use [asdf](https://github.com/asdf-vm/asdf) for managing programming language versions

```bash
brew install asdf
```

Then add asdf to your path:

```bash
# ~/.zshrc

# Enable ASDF
export PATH="${ASD_DATA_DIR:-$HOME/.asdf}/shims:$PATH"%
```

Install some plugins:

```bash
asdf plugin add ruby
asdf plugin add nodejs

asdf install ruby latest
asdf install nodejs latest
```

## GitHub CLI

Use [gh](https://cli.github.com/) for interacting with the GitHub API

```bash
brew install gh
```

## Apps

Use [brew cask](https://github.com/caskroom/homebrew-cask):

### Development

```bash
brew install --cask \
  visual-studio-code \
  github \
  dash
```

- [Visual Studio Code](https://code.visualstudio.com/)
- [Github Desktop](https://desktop.github.com/)
- [Dash](https://kapeli.com/dash)

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

### Orbstack

Install orbstack:

```bash
brew install --cask orbstack
```

### Everything else

- `.git_config`
- `.global_ignore`

Create symlinks to your dotfiles in `~`.

```bash
cd ~/dotfiles
rake install
```

## OSX

### Quick Look

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

### Security

Make you mac secure; taken from [this guide](https://github.com/drduh/macOS-Security-and-Privacy-Guide). These are the absolute basics:

1. Enable [firewall](https://github.com/drduh/macOS-Security-and-Privacy-Guide?tab=readme-ov-file#firewall)
2. Enable [FileVault](https://github.com/drduh/macOS-Security-and-Privacy-Guide?tab=readme-ov-file#filevault)
3. Use [NextDNS](https://nextdns.io)
