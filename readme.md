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

5. Use Ghostty as the supported terminal.

The Ghostty config is symlink-managed at `~/.config/ghostty/config.ghostty`, uses the Snazzy Soft theme, and leaves font, shell integration, keybindings, and behavior on Ghostty defaults. Apple Terminal stays on macOS defaults outside this baseline.

6. Open a new Ghostty window and verify the setup:

```bash
cd ~/dotfiles
rake doctor
```

If `rake doctor` reports incomplete SSH signing, restore the signing key from Bitwarden using the SSH signing setup below and run it again.

If `rake doctor` reports missing Codex auth, run `codex login`. Codex auth stays machine-local.

## Managed Files

`rake install` links the explicit inventory in the `Rakefile`:

- `git/gitattributes.symlink` -> `~/.gitattributes`
- `git/gitconfig.symlink` -> `~/.gitconfig`
- `ghostty/config.ghostty.symlink` -> `~/.config/ghostty/config.ghostty`
- `codex/config.local.toml` -> `~/.codex/config.toml`
- `codex/mcp.json.symlink` -> `~/.codex/.mcp.json`
- `codex/agents.symlink` -> `~/.codex/agents`
- `codex/prompts.symlink` -> `~/.codex/prompts`
- `codex/rules.symlink` -> `~/.codex/rules`
- `osx/hushlogin.symlink` -> `~/.hushlogin`
- `zsh/zprofile.symlink` -> `~/.zprofile`
- `zsh/zshrc.symlink` -> `~/.zshrc`

The installer is intentionally symlink-based so edits in `~/dotfiles` are reflected immediately in the active shell and Git configuration.

## Baseline Tools And Apps

The exact install list lives in `osx/Brewfile`.

### Terminal And Shell

- Ghostty with zsh.
- Snazzy Soft theme with Ghostty defaults for font, shell integration, keybindings, and behavior.
- Pure prompt with zsh syntax highlighting.
- `mise` for runtime management.
- `eza` and `bat` as nicer defaults for `ls` and `cat`.

### Development Tools

- GitHub CLI, Git LFS, ripgrep, dotenvx, sshpass, Terraform, and OpenSSL.
- SSH commit signing with key material stored in Bitwarden and GitHub CLI key upload.
- Heroku, Railway, Vercel, Sentry, Supabase, Neon, Turso, and Google Cloud CLIs.
- OrbStack, ngrok, Postico, Cyberduck, and Dash.
- VS Code and GitHub Desktop.

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

Codex is installed as part of the Brewfile. This repo manages the Codex product baseline, MCP pointer, agents, prompts, and command rules:

- `codex/config.template.toml`: portable product defaults for model choice, sandbox behavior, MCP servers, feature flags, plugins, desktop preferences, memories, and agent limits.
- `codex/config.local.toml`: machine-local config generated from the template and linked to `~/.codex/config.toml`.
- `~/.codex/.mcp.json`
- `~/.codex/agents`
- `~/.codex/prompts`
- `~/.codex/rules`

Computer-specific Codex settings live in `codex/config.local.toml`: trusted projects, writable roots, notification helpers, local runtime paths, marketplace cache paths, and per-path desktop preferences. Codex auth stays local to each machine at `~/.codex/auth.json`. Logs, sessions, SQLite state, caches, generated images, memories, plugins, and `node_modules` live in the local Codex home.

Codex skills live in the `agent-skills` repo. Dotfiles covers the Codex config surface, while `agent-skills` is the source of truth for user-managed skills.

The tracked Codex template carries product choices without machine paths. Keep bearer tokens and API secrets in local auth, environment setup, or service-specific login flows. Codex may update trusted project paths, marketplace timestamps, or desktop preferences in the local config.

Verify Codex config health with:

```bash
codex --strict-config doctor --summary --ascii
```

Useful MCP servers to keep in mind when rebuilding or extending the agent setup:

- Chrome DevTools
- Context7
- Next DevTools
- Playwright
- Mapbox
- Vercel

## Shell Layout

- `zsh/zprofile.symlink`: login-shell setup for Homebrew, OrbStack, and `mise` shims for non-interactive command runners.
- `zsh/zshrc.symlink`: interactive shell setup for locale, Pure prompt, aliases, completions, pnpm, Bun, Turso, `mise` activation, and direnv.
- `ghostty/config.ghostty.symlink`: Ghostty config managed at `~/.config/ghostty/config.ghostty`. The XDG config is the single Ghostty config source, because Ghostty loads the macOS-specific config path after it.
- Apple Terminal settings stay on macOS defaults.
- Optional integrations are guarded so a fresh shell can start before every tool is configured.

## Tooling Policy

- Homebrew is the app and CLI package baseline.
- Ghostty is validated at `/Applications/Ghostty.app/Contents/MacOS/ghostty`.
- `mise` manages language/runtime versions and can use latest-by-default tools. Login shells expose shims, while interactive zsh uses normal activation so project versions take effect when moving between repos.
- `brew bundle check --no-upgrade --file=osx/Brewfile` should pass on the primary machine; this checks presence without enforcing available upgrades.
- `rake doctor` is the quick drift check before relying on this repo for a rebuild. It verifies symlinks, required commands, the Ghostty app bundle, the single managed Ghostty config, Codex local-only auth, Pure prompt loading, documentation coverage, and Brewfile presence.
