# Dotfiles

## Getting started
```
git clone git@github.com:phildionne/dotfiles.git
```
Install [bash-it](https://github.com/revans/bash-it) and pick useful completions and plugins.

Create symlinks to your dotfiles in `~`. This will overwrite `~/.bash_profile` created by bash-it.
```
cd ~/dotfiles
rake install
```

### Sublime
Overwrite Sublime preferences:
Symlink `~/dotfiles/sublime2/User/Preferences.Default (OSX).sublime-keymap` and `~/dotfiles/sublime2/User/Preferences.sublime-settings` to `Packages/User/Preferences.Default (OSX).sublime-keymap` and `Packages/User/Preferences.sublime-settings`

#### Packages
First, install [Sublime Package Controll](http://wbond.net/sublime_packages/package_control) and then:

1. Emmet
2. ERB Insert and Toggle Commands
3. GitGutter
4. SideBarEnhancements
