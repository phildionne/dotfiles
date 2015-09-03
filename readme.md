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
