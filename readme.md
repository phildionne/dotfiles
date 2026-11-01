# Dotfiles

macOS development configuration for Apple Silicon Macs.

## Setup

Run these steps in order in Terminal. Complete each installer, editor, and browser prompt before continuing.

### 1. Install Homebrew

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
eval "$(/opt/homebrew/bin/brew shellenv zsh)"
```

Homebrew runs at `/opt/homebrew/bin/brew`. The `shellenv` command adds it to the current shell's PATH.

### 2. Clone the repository

```bash
cd ~
git clone https://github.com/phildionne/dotfiles
cd dotfiles
```

### 3. Install mise and trust the package sources

```bash
brew install mise
brew trust --formula \
  dotenvx/brew/dotenvx \
  getsentry/tools/sentry \
  hashicorp/tap/terraform \
  heroku/brew/heroku \
  hudochenkov/sshpass/sshpass \
  libsql/sqld/sqld \
  tursodatabase/tap/turso
brew trust --tap abue-ammar/tinycast
```

### 4. Apply the configuration

Trust the checkout and preview the changes:

```bash
mise trust
mise bootstrap --dry-run
```

The preview prints hooks without executing them. It does not check package installation state.

Run bootstrap in an interactive terminal:

```bash
mise bootstrap --raw
```

Bootstrap applies the configuration in this order:

1. Install Homebrew packages.
2. Register and install global mise tools.
3. Link managed files.
4. Apply macOS preferences and the Dock layout.

The Google Drive installer requires a macOS administrator password.

Back up conflicting destination files before rerunning bootstrap. Do not use `--force-dotfiles`.

### 5. Configure SSH signing

Open a new Ghostty window to load the managed shell configuration.

Git signs commits with `~/.ssh/id_ed25519_signing.pub`. GitHub verifies pushed commits against the registered public key.

Sign in to Bitwarden. Restore the private and public signing keys into the files opened below. Save and close each file before continuing:

```bash
mkdir -p ~/.ssh
chmod 700 ~/.ssh
touch ~/.ssh/id_ed25519_signing ~/.ssh/id_ed25519_signing.pub
chmod 600 ~/.ssh/id_ed25519_signing
chmod 644 ~/.ssh/id_ed25519_signing.pub
nano ~/.ssh/id_ed25519_signing
nano ~/.ssh/id_ed25519_signing.pub
```

Sign in to GitHub and list its registered signing keys:

```bash
gh auth login
gh auth refresh -h github.com -s admin:ssh_signing_key
gh ssh-key list --type signing
```

Confirm that the restored public key is listed. If it is absent, register it with `gh ssh-key add ~/.ssh/id_ed25519_signing.pub --type signing --title "$(hostname)-signing"`.

### 6. Authenticate Codex

```bash
codex login
```

### 7. Verify the setup

```bash
cd ~/dotfiles
rake doctor
```

## Packages and runtimes

| Scope | Manager | Source of truth |
| --- | --- | --- |
| Applications and CLI packages | Homebrew | `osx/Brewfile` |
| Node, Vercel CLI, and Neon CLI | mise | `mise.toml` package hooks |
| Project runtime versions | mise | Each project's mise configuration |

The Homebrew hook runs `brew bundle install --file=osx/Brewfile --no-upgrade --verbose`. It installs missing packages. Homebrew upgrades dependencies when required by a new installation.

The mise hook runs `mise use --global node npm:vercel npm:neonctl`. It reuses installed versions and selects the latest version for missing tools. The npm backend gives each CLI a separate installation directory.

## Managed files

The `[dotfiles]` section in `mise.toml` defines these symlinks:

| Repository source | Destination |
| --- | --- |
| `git/gitattributes.symlink` | `~/.gitattributes` |
| `git/gitconfig.symlink` | `~/.gitconfig` |
| `ghostty/config.ghostty.symlink` | `~/.config/ghostty/config.ghostty` |
| `codex/agents.symlink` | `~/.codex/agents` |
| `osx/hushlogin.symlink` | `~/.hushlogin` |
| `zsh/zprofile.symlink` | `~/.zprofile` |
| `zsh/zshrc.symlink` | `~/.zshrc` |

Edit the repository sources to update the linked configuration.

## Terminal and shell

### Ghostty

Ghostty is the supported terminal. Its executable is `/Applications/Ghostty.app/Contents/MacOS/ghostty`.

| Setting | Value |
| --- | --- |
| Theme | Snazzy Soft |
| Font and shell integration | Ghostty defaults |
| `Cmd+R` | Clear the screen |
| New window directory | Home directory |
| New tab directory | Current working directory |

`~/.config/ghostty/config.ghostty` is the sole configuration source. Bootstrap removes an empty secondary macOS config and rejects one containing settings.

### zsh

| File | Responsibility |
| --- | --- |
| `zsh/zprofile.symlink` | Homebrew environment, OrbStack integration, and mise shims for login shells |
| `zsh/zshrc.symlink` | Pure prompt, syntax highlighting, aliases, completions, pnpm, Turso, mise activation, and direnv |

Login shells expose mise shims. Interactive shells activate project runtime versions as directories change.

Apple Terminal uses macOS defaults.

## macOS preferences

`mise.toml` defines the preferences and Dock layout.

| Area | Configuration |
| --- | --- |
| Finder windows | Hidden files visible; column view; sidebar visible |
| Finder desktop | External drives and removable media visible; internal drives hidden |
| Finder sidebar | Favorites and Locations expanded; Tags collapsed |
| Dock | Auto-hide enabled; 64-point icons |
| Pinned applications | Google Chrome, ChatGPT, Ghostty, System Settings, in that order |
| Dock folders | Existing folder-side items preserved |
| Spotlight | Menu bar icon hidden |
| Keyboard repeat | Key repeat `1`; initial delay `10` |
| Keyboard navigation | Disabled |
| Text entry | Automatic capitalization and period substitution enabled |

All pinned applications must exist before preferences are applied. Bootstrap restarts Dock and SystemUIServer. Sign out and back in to activate keyboard changes.

## Codex

Homebrew installs Codex CLI (`codex`) and ChatGPT (`chatgpt`).

| Configuration | Owner |
| --- | --- |
| Custom agent definitions | `codex/agents.symlink` |
| User-managed skills | `agent-skills` repository |
| `~/.codex/config.toml` | Desktop app; machine-local |
| `~/.codex/auth.json` | Local authentication |
| Sessions, logs, caches, and plugins | Local Codex home |

Keep `~/.codex/config.toml` as a local file. Store secrets in local authentication, environment variables, or service login flows.

## Verification

| Check | Command |
| --- | --- |
| Machine configuration | `rake doctor` |
| Homebrew package presence | `brew bundle check --no-upgrade --file=osx/Brewfile` |
| Codex configuration | `codex --strict-config doctor --summary --ascii` |
| Bootstrap behavior in a temporary home | `python3 tests/bootstrap.py` |

Apply individual configuration sections with:

```bash
mise bootstrap --only packages --raw
mise bootstrap --only dotfiles
mise bootstrap --only macos-defaults --raw
```
