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

## Mise

Use [mise](https://mise.jdx.dev/) for managing programming language versions

```bash
brew install mise
```

Then activate it:

```bash
# ~/.zshrc

# Enable Mise
eval "$(mise activate zsh)"
```

Install runtimes:

```bash
mise use node@latest
```

## Agents

Install OpenAi codex

```bash
brew install codex
```

Useful list of MCP servers:

- [chrome-devtools](https://github.com/ChromeDevTools/chrome-devtools-mcp)
- [context7](https://github.com/upstash/context7)
- [next-devtools](https://github.com/vercel/next-devtools-mcp)
- [playwright](https://github.com/microsoft/playwright-mcp)
- [mapbox](https://github.com/mapbox/mcp-server)
- [vercel](https://vercel.com/docs/mcp/vercel-mcp)

## Apps

### Development

```bash
brew install --cask \
  visual-studio-code \
  github \
  gh \
  dash
```

- [Visual Studio Code](https://code.visualstudio.com/)
- [Github Desktop](https://desktop.github.com/)
- [gh](https://cli.github.com/)
- [Dash](https://kapeli.com/dash)

### Database

- [Supabase](https://supabase.com/)
- [Postgres.app](https://postgresapp.com/) PostgreSQL database
- [Sequel](https://www.sequelpro.com/) MySQL GUI
- [Postico](https://eggerapps.at/postico/) PostgreSQL GUI
- [Base](https://menial.co.uk/base/) SQLite3 GUI

```bash
brew install --cask \
  supabase \
  postgres-unofficial \
  sequel-pro \
  postico \
  base
```

See:

- https://postgresapp.com/documentation/install.html

### Other

```bash
brew install --cask \
  appcleaner \
  bitwarden \
  google-chrome \
  slack \
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
