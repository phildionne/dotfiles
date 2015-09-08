## Getting started
```
cd & git clone git@github.com:phildionne/dotfiles.git
```

### Bash
Install [bash-it](https://github.com/revans/bash-it) and pick useful completions and plugins. Mine are:

#### Aliases
- Bundler
- General
- Git

#### Plugins
none

#### Completions
- Brew
- Defaults
- Gem
- Git
- Grunt
- Gulp
- Rake
- SSH

### OSX

Set OSX defaults:

```
source $HOME/dotfiles/osx/set-defaults.sh
```

### Atom

Overwrite Atom preferences with your own:

```
ln -s $HOME/dotfiles/atom/* $HOME/.atom/
```

### Everything else

- `.bash_profile`
- `.git_config`
- `.global_ignore`
- `.gemrc`
- `.irbrc`
- `.pryrc`
- `.rspec`

Create symlinks to your dotfiles in `~`. This will overwrite `~/.bash_profile` created by bash-it.

```
cd ~/dotfiles
rake install
```

### OSX

Make you mac secure; mostly taken from [this guide](https://github.com/drduh/OS-X-Yosemite-Security-and-Privacy-Guide).

1. Enable [firewall](https://github.com/drduh/OS-X-Yosemite-Security-and-Privacy-Guide#firewall)
2. Disable [spotlight suggestions](https://github.com/drduh/OS-X-Yosemite-Security-and-Privacy-Guide#spotlight-suggestions)
3. Configure [hosts file](https://github.com/drduh/OS-X-Yosemite-Security-and-Privacy-Guide#hosts-file)
4. Use latest OpenSSL: `brew install openssl && brew link --force openssl`
5. Use curl with openssl: `brew install curl --with-openssl && brew link --force curl`
6. Deactivate Chrome's Flash plugin by visiting `chrome://plugins/`
