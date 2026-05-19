## Dotfiles

This is my personal macOS development baseline for shell, Git, Homebrew apps, and editor tooling.

## New Mac Setup

1. Install Homebrew:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

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

5. Open a new terminal and verify the setup:

```bash
cd ~/dotfiles
rake doctor
```

## Managed Files

`rake install` links the explicit inventory in the `Rakefile`:

- `~/.gitattributes`
- `~/.gitconfig`
- `~/.hushlogin`
- `~/.zprofile`
- `~/.zshrc`

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
- Heroku, Railway, Vercel, Sentry, Supabase, Neon, Turso, and Google Cloud CLIs.
- OrbStack, ngrok, Postico, Cyberduck, and Dash.
- VS Code, GitHub Desktop, and the Fira Code Nerd Font.

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

- `zsh/zprofile.symlink`: login-shell setup for Homebrew, OrbStack, and `mise`.
- `zsh/zshrc.symlink`: interactive shell setup for locale, Pure prompt, aliases, completions, pnpm, Bun, Turso, and direnv.
- Optional integrations are guarded so a fresh shell can start before every tool is configured.

## Tooling Policy

- Homebrew is the app and CLI package baseline.
- `mise` manages language/runtime versions and can use latest-by-default tools.
- `brew bundle check --file=osx/Brewfile` should pass on the primary machine.
- `rake doctor` is the quick drift check before relying on this repo for a rebuild.
