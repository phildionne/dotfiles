## Dotfiles

This is my personal macOS development baseline for Apple Silicon Macs: shell, Git, Homebrew apps, and editor tooling.

## New Mac Setup

1. Install Homebrew:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

This repo assumes Apple Silicon Homebrew at `/opt/homebrew/bin/brew`.

2. Clone the repo:

```bash
cd ~
git clone https://github.com/phildionne/dotfiles
cd dotfiles
```

3. Install the baseline tools and apps:

```bash
brew bundle install --file=osx/Brewfile
```

4. Link the managed dotfiles:

```bash
rake install
```

5. Configure the iTerm2 profile manually:

- Use iTerm2 as the supported terminal. Apple Terminal is not managed by this repo.
- Set the profile font to `Fira Code Nerd Font`.
- Use the Snazzy color theme, or the current manually configured equivalent.

6. Open a new iTerm2 window and verify the setup:

```bash
cd ~/dotfiles
rake doctor
```

If `rake doctor` reports incomplete SSH signing, restore the signing key from Bitwarden using the SSH signing setup below and run it again.

## Managed Files

`rake install` links the explicit inventory in the `Rakefile`:

- `git/gitattributes.symlink` -> `~/.gitattributes`
- `git/gitconfig.symlink` -> `~/.gitconfig`
- `osx/hushlogin.symlink` -> `~/.hushlogin`
- `zsh/zprofile.symlink` -> `~/.zprofile`
- `zsh/zshrc.symlink` -> `~/.zshrc`

The installer is intentionally symlink-based so edits in `~/dotfiles` are reflected immediately in the active shell and Git configuration.

## Baseline Tools And Apps

The exact install list lives in `osx/Brewfile`.

### Terminal And Shell

- iTerm2 with zsh.
- Pure prompt with zsh syntax highlighting.
- `mise` for runtime management.
- `eza` and `bat` as nicer defaults for `ls` and `cat`.

### Development Tools

- GitHub CLI, Git LFS, ripgrep, dotenvx, sshpass, Terraform, and OpenSSL.
- SSH commit signing with key material stored in Bitwarden and GitHub CLI key upload.
- Heroku, Railway, Vercel, Sentry, Supabase, Neon, Turso, and Google Cloud CLIs.
- OrbStack, ngrok, Postico, Cyberduck, and Dash.
- VS Code, GitHub Desktop, and the Fira Code Nerd Font.

## SSH Signing

Git is configured to sign commits with `~/.ssh/id_ed25519_signing.pub`. Bitwarden stores the key material, but it is not used as an SSH agent.

On a new Mac, copy the private key and public key from Bitwarden into local files:

```bash
mkdir -p ~/.ssh
chmod 700 ~/.ssh
$EDITOR ~/.ssh/id_ed25519_signing
$EDITOR ~/.ssh/id_ed25519_signing.pub
chmod 600 ~/.ssh/id_ed25519_signing
chmod 644 ~/.ssh/id_ed25519_signing.pub
```

Add the public key to GitHub as a signing key:

```bash
gh auth refresh -h github.com -s admin:ssh_signing_key
gh ssh-key add ~/.ssh/id_ed25519_signing.pub --type signing --title "$(hostname)-signing"
```

Verify signing:

```bash
git commit -S --allow-empty -m "Verify signed commit"
git cat-file -p HEAD | grep -A5 '^gpgsig'
```

After pushing a signed commit, GitHub should show it as verified.

### Desktop Apps

- AppCleaner, Bitwarden, Google Chrome, Google Drive, Raycast, Slack, Spotify, Superwhisper, The Unarchiver, VLC, WebTorrent, and Zoom.
- Codex and ChatGPT Atlas for agent-assisted development.

### VS Code Extensions

- Core editing: EditorConfig, ESLint, Prettier, Stylelint, Sort Lines, Change Case, Pretty TypeScript Errors.
- Git and GitHub: GitLens, GitHub theme, GitHub Pull Requests.
- Languages and data: Python, Pylance, Black, isort, Pylint, GraphQL, Tailwind CSS, TOML, dotenv, Jinja, djLint, XML, CSV, SVG preview, SQL formatter.
- Containers and collaboration: Docker, Dev Containers, Live Share.
- AI/editor tools: Copilot Chat, ChatGPT, OXC.

### Agent And MCP Notes

Codex is installed as part of the Brewfile, while user-specific agent auth, logs, memories, and plugins live outside this repo. Useful MCP servers to keep in mind when rebuilding or extending the agent setup:

- Chrome DevTools
- Context7
- Next DevTools
- Playwright
- Mapbox
- Vercel

## Shell Layout

- `zsh/zprofile.symlink`: login-shell setup for Homebrew, OrbStack, and `mise` shims for non-interactive command runners.
- `zsh/zshrc.symlink`: interactive shell setup for locale, Pure prompt, aliases, completions, pnpm, Bun, Turso, `mise` activation, and direnv.
- iTerm2 profile appearance is documented as a manual setup step; no iTerm2 profile JSON, plist, or Apple Terminal settings are managed here.
- Optional integrations are guarded so a fresh shell can start before every tool is configured.

## Tooling Policy

- Homebrew is the app and CLI package baseline.
- `mise` manages language/runtime versions and can use latest-by-default tools. Login shells expose shims, while interactive zsh uses normal activation so project versions take effect when moving between repos.
- `brew bundle check --file=osx/Brewfile` should pass on the primary machine.
- `rake doctor` is the quick drift check before relying on this repo for a rebuild. It verifies symlinks, required commands, Pure prompt loading, documentation coverage, and Brewfile drift.
