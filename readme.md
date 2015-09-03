# Dotfiles

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

#### Completion
- Brew
- Defaults
- Gem
- Git
- Rake
- SSH
- Grunt
- Gulp

Create symlinks to your dotfiles in `~`. This will overwrite `~/.bash_profile` created by bash-it.
```
cd ~/dotfiles
rake install
```

### Atom

Overwrite Atom preferences with your own:

```
ln -s $HOME/dotfiles/atom/* $HOME/.atom/
```



