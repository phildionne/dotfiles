# Totally stolen from https://github.com/holman/dotfiles
require 'fileutils'
require 'rake'
require 'shellwords'

DOTFILES_ROOT = File.expand_path(__dir__)
LINKABLES = [
  'git/gitattributes.symlink',
  'git/gitconfig.symlink',
  'osx/hushlogin.symlink',
  'zsh/zprofile.symlink',
  'zsh/zshrc.symlink'
].freeze

REQUIRED_COMMANDS = %w[
  bat
  brew
  direnv
  eza
  gh
  git
  git-lfs
  mise
  turso
  zsh
].freeze

def link_target(linkable)
  file = File.basename(linkable).sub(/\.symlink\z/, '')
  File.join(ENV.fetch('HOME'), ".#{file}")
end

desc "Hook our dotfiles into system-standard positions."
task :install do
  skip_all = ENV['SKIP'] == '1'
  overwrite_all = ENV['OVERWRITE'] == '1'
  backup_all = ENV['BACKUP'] == '1'

  LINKABLES.each do |linkable|
    overwrite = false
    backup = false

    target = link_target(linkable)

    if File.exists?(target) || File.symlink?(target)
      if skip_all
        puts "Skipping #{target}"
        next
      end

      unless skip_all || overwrite_all || backup_all
        puts "File already exists: #{target}, what do you want to do? [s]kip, [S]kip all, [o]verwrite, [O]verwrite all, [b]ackup, [B]ackup all"
        case STDIN.gets.chomp
        when 'o' then overwrite = true
        when 'b' then backup = true
        when 'O' then overwrite_all = true
        when 'B' then backup_all = true
        when 'S'
          skip_all = true
          next
        when 's' then next
        else
          puts "Skipping #{target}"
          next
        end
      end
      FileUtils.rm_rf(target) if overwrite || overwrite_all
      FileUtils.mv(target, "#{target}.backup") if backup || backup_all
    end
    FileUtils.ln_s(File.join(DOTFILES_ROOT, linkable), target)
  end
end

desc "Check managed symlinks, required commands, and Brewfile drift."
task :doctor do
  failures = []

  LINKABLES.each do |linkable|
    target = link_target(linkable)
    expected = File.join(DOTFILES_ROOT, linkable)
    actual = File.symlink?(target) ? File.readlink(target) : nil

    if actual == expected
      puts "ok symlink #{target} -> #{actual}"
    elsif File.exist?(target)
      failures << "#{target} exists but does not point to #{expected}"
    else
      failures << "#{target} is missing"
    end
  end

  REQUIRED_COMMANDS.each do |command|
    if system("command -v #{Shellwords.escape(command)} >/dev/null 2>&1")
      puts "ok command #{command}"
    else
      failures << "missing command: #{command}"
    end
  end

  unless system('brew', 'bundle', 'check', '--file=osx/Brewfile')
    failures << 'brew bundle check failed for osx/Brewfile'
  end

  if failures.empty?
    puts 'doctor passed'
  else
    puts failures.map { |failure| "error #{failure}" }
    exit 1
  end
end

task :default => 'install'
