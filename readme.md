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

Create symlinks to your dotfiles in `~`. This will overwrite `~/.bash_profile` created by bash-it.
```
cd ~/dotfiles
rake install
```

### SublimeText

Overwrite Sublime preferences with your own:

```
ln -s /Users/pdionne/dotfiles/sublime/User/* /Users/pdionne/Library/Application\ Support/Sublime\ Text\ 3/Packages/User/
```

#### Packages

First, install [Sublime Package Controll](http://wbond.net/sublime_packages/package_control) and then:

1. SideBarEnhancements
2. Emmet
3. SublimeERB
4. GitGutter
5. BetterCoffeeScript
6. LESS
7. SASS
8. RSpec
9. Theme - Flatland
