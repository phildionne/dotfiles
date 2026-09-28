#!/bin/zsh
set -euo pipefail

if ! command -v dockutil >/dev/null 2>&1; then
  print -u2 'dockutil is missing; run brew bundle install --file=osx/Brewfile first'
  exit 1
fi

for app in '/Applications/Google Chrome.app' '/Applications/Ghostty.app' '/System/Applications/System Settings.app'; do
  if [[ ! -d "$app" ]]; then
    print -u2 "Required Dock app is missing: $app"
    exit 1
  fi
done

defaults write com.apple.finder FXPreferredViewStyle -string clmv
defaults write com.apple.finder ShowExternalHardDrivesOnDesktop -bool true
defaults write com.apple.finder ShowHardDrivesOnDesktop -bool false
defaults write com.apple.finder ShowRemovableMediaOnDesktop -bool true
defaults write com.apple.finder ShowSidebar -bool true
defaults write com.apple.finder SidebarPlacesSectionDisclosedState -bool true
defaults write com.apple.finder SidebarDevicesSectionDisclosedState -bool true
defaults write com.apple.finder SidebarTagsSctionDisclosedState -bool false

defaults write com.apple.dock autohide -bool true
defaults write com.apple.dock tilesize -int 64

defaults write -g KeyRepeat -int 1
defaults write -g InitialKeyRepeat -int 10
defaults write -g AppleKeyboardUIMode -int 0
defaults write -g NSAutomaticCapitalizationEnabled -bool true
defaults write -g NSAutomaticPeriodSubstitutionEnabled -bool true

# Replace pinned apps without changing folder-side items such as Downloads.
defaults write com.apple.dock persistent-apps -array
dockutil --add '/Applications/Google Chrome.app' --no-restart
if [[ -d '/Applications/ChatGPT.app' ]]; then
  dockutil --add '/Applications/ChatGPT.app' --no-restart
fi
dockutil --add '/Applications/Ghostty.app' --no-restart
dockutil --add '/System/Applications/System Settings.app' --no-restart

killall Dock
