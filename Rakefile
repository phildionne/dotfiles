# Totally stolen from https://github.com/holman/dotfiles
require 'fileutils'
require 'rake'
require 'shellwords'

DOTFILES_ROOT = File.expand_path(__dir__)
HOMEBREW_PREFIX = '/opt/homebrew'.freeze
HOMEBREW_BIN = File.join(HOMEBREW_PREFIX, 'bin/brew').freeze
GHOSTTY_APP_BIN = '/Applications/Ghostty.app/Contents/MacOS/ghostty'.freeze
GHOSTTY_XDG_CONFIG = '.config/ghostty/config.ghostty'.freeze
GHOSTTY_MACOS_CONFIG = 'Library/Application Support/com.mitchellh.ghostty/config.ghostty'.freeze
SSH_SIGNING_KEY = '.ssh/id_ed25519_signing.pub'.freeze
CODEX_AUTH_JSON = '.codex/auth.json'.freeze
CODEX_LOCAL_CONFIG = 'codex/config.local.toml'.freeze
CODEX_TEMPLATE_CONFIG = 'codex/config.template.toml'.freeze
CODEX_SCANNED_CONFIGS = [CODEX_TEMPLATE_CONFIG, CODEX_LOCAL_CONFIG].freeze
CODEX_TEMPLATE_PORTABILITY_PATTERNS = [
  [/^\[projects\./, '[projects.*]'],
  [/^notify\s*=/, 'notify'],
  [/writable_roots/, 'writable_roots'],
  [/^\[marketplaces\./, '[marketplaces.*]'],
  [/node_repl/, 'node_repl'],
  [/perPath/, 'desktop per-path preferences'],
  [%r{/Users/}, '/Users paths'],
  [%r{/Applications/}, '/Applications paths']
].freeze

LINKABLES = {
  CODEX_LOCAL_CONFIG => '.codex/config.toml',
  'codex/mcp.json.symlink' => '.codex/.mcp.json',
  'codex/agents.symlink' => '.codex/agents',
  'codex/prompts.symlink' => '.codex/prompts',
  'codex/rules.symlink' => '.codex/rules',
  'git/gitattributes.symlink' => '.gitattributes',
  'git/gitconfig.symlink' => '.gitconfig',
  'ghostty/config.ghostty.symlink' => GHOSTTY_XDG_CONFIG,
  'osx/hushlogin.symlink' => '.hushlogin',
  'zsh/zprofile.symlink' => '.zprofile',
  'zsh/zshrc.symlink' => '.zshrc'
}.freeze

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

DOCS_REQUIRED_STRINGS = (
  LINKABLES.keys + [
    'brew bundle install --file=osx/Brewfile',
    'rake install',
    'rake doctor',
    'Apple Silicon',
    HOMEBREW_BIN,
    GHOSTTY_APP_BIN,
    GHOSTTY_XDG_CONFIG,
    SSH_SIGNING_KEY,
    CODEX_AUTH_JSON,
    CODEX_TEMPLATE_CONFIG,
    'agent-skills',
    'codex --strict-config doctor --summary --ascii',
    'gh ssh-key add ~/.ssh/id_ed25519_signing.pub --type signing'
  ]
).freeze

DOCS_REQUIRED_CONCEPTS = [
  ['Codex'],
  ['Ghostty'],
  ['Snazzy Soft'],
  ['Pure'],
  ['Apple Terminal', 'defaults'],
  ['agent-skills', 'skills'],
  ['SSH', 'signing']
].freeze

def link_target(target)
  File.join(ENV.fetch('HOME'), target)
end

def backup_target(target)
  backup = "#{target}.backup"
  return backup unless File.exist?(backup) || File.symlink?(backup)

  "#{backup}.#{Time.now.strftime('%Y%m%d%H%M%S')}"
end

def remove_target(target)
  if File.directory?(target) && !File.symlink?(target)
    abort "Refusing to overwrite directory #{target}; use BACKUP=1 or move it manually"
  end

  FileUtils.rm_f(target)
end

def git_config_value(key)
  gitconfig = File.join(DOTFILES_ROOT, 'git/gitconfig.symlink')
  `git config --file #{Shellwords.escape(gitconfig)} --get #{Shellwords.escape(key)}`.strip
end

def expand_home(path)
  path.sub(/\A~/, ENV.fetch('HOME'))
end

def ghostty_macos_config_path
  link_target(GHOSTTY_MACOS_CONFIG)
end

def codex_skill_paths
  Dir.glob(File.join(DOTFILES_ROOT, 'codex', 'skills*'))
end

def prepare_codex_local_config
  local_config_path = File.join(DOTFILES_ROOT, CODEX_LOCAL_CONFIG)
  return if File.exist?(local_config_path)

  template_config_path = File.join(DOTFILES_ROOT, CODEX_TEMPLATE_CONFIG)
  abort "#{CODEX_TEMPLATE_CONFIG} is missing; cannot create #{CODEX_LOCAL_CONFIG}" unless File.file?(template_config_path)

  FileUtils.cp(template_config_path, local_config_path)
  puts "Created #{CODEX_LOCAL_CONFIG} from #{CODEX_TEMPLATE_CONFIG}"
end

def codex_config_secret_failures
  failures = []

  CODEX_SCANNED_CONFIGS.each do |relative_config_path|
    config_path = File.join(DOTFILES_ROOT, relative_config_path)
    unless File.file?(config_path)
      failures << "#{relative_config_path} is missing"
      next
    end

    File.readlines(config_path).each_with_index do |line, index|
      next if line.match?(/\A\s*(#|$)/)
      next unless line.match?(/Bearer\s+\S{16,}|ghp_[A-Za-z0-9_]{16,}|sk-[A-Za-z0-9_-]{16,}/)

      failures << "#{relative_config_path}:#{index + 1} appears to contain a secret token"
    end
  end

  failures
end

def codex_template_portability_failures
  template_config_path = File.join(DOTFILES_ROOT, CODEX_TEMPLATE_CONFIG)
  return ["#{CODEX_TEMPLATE_CONFIG} is missing"] unless File.file?(template_config_path)

  failures = []
  File.readlines(template_config_path).each_with_index do |line, index|
    CODEX_TEMPLATE_PORTABILITY_PATTERNS.each do |pattern, label|
      failures << "#{CODEX_TEMPLATE_CONFIG}:#{index + 1} contains #{label}" if line.match?(pattern)
    end
  end

  failures
end

def remove_empty_ghostty_macos_config
  config_path = ghostty_macos_config_path
  return unless File.exist?(config_path) || File.symlink?(config_path)

  if File.file?(config_path) && File.zero?(config_path)
    FileUtils.rm_f(config_path)
    puts "Removed empty Ghostty macOS config #{config_path}"
  else
    abort "Refusing to overwrite Ghostty macOS config #{config_path}; move it manually so #{GHOSTTY_XDG_CONFIG} is the only managed config"
  end
end

def docs_check_failures(readme)
  missing = []

  DOCS_REQUIRED_STRINGS.each do |required_string|
    missing << "readme.md is missing #{required_string.inspect}" unless readme.include?(required_string)
  end

  DOCS_REQUIRED_CONCEPTS.each do |concept|
    next if concept.all? { |required_string| readme.include?(required_string) }

    missing << "readme.md is missing concept #{concept.join(' + ').inspect}"
  end

  missing
end

desc "Hook our dotfiles into system-standard positions."
task :install do
  skip_all = ENV['SKIP'] == '1'
  overwrite_all = ENV['OVERWRITE'] == '1'
  backup_all = ENV['BACKUP'] == '1'

  remove_empty_ghostty_macos_config
  prepare_codex_local_config

  LINKABLES.each do |source, target_name|
    overwrite = false
    backup = false

    source_path = File.join(DOTFILES_ROOT, source)
    target = link_target(target_name)

    if File.exist?(target) || File.symlink?(target)
      if File.symlink?(target) && File.readlink(target) == source_path
        puts "Already linked #{target}"
        next
      end

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
      if backup || backup_all
        FileUtils.mv(target, backup_target(target))
      elsif overwrite || overwrite_all
        remove_target(target)
      end
    end
    FileUtils.mkdir_p(File.dirname(target))
    FileUtils.ln_s(source_path, target)
  end
end

desc "Check managed symlinks, required commands, and Brewfile presence."
task :doctor do
  failures = []
  readme = File.read(File.join(DOTFILES_ROOT, 'readme.md'))

  if File.executable?(HOMEBREW_BIN)
    puts "ok homebrew #{HOMEBREW_BIN}"
  else
    failures << "#{HOMEBREW_BIN} is missing or not executable"
  end

  if File.executable?(GHOSTTY_APP_BIN)
    puts "ok ghostty #{GHOSTTY_APP_BIN}"
  else
    failures << "#{GHOSTTY_APP_BIN} is missing or not executable"
  end

  if File.exist?(ghostty_macos_config_path) || File.symlink?(ghostty_macos_config_path)
    failures << "Ghostty macOS config #{ghostty_macos_config_path} exists; remove it so #{GHOSTTY_XDG_CONFIG} is the only managed config"
  else
    puts 'ok ghostty single managed config'
  end

  LINKABLES.each do |source, target_name|
    target = link_target(target_name)
    expected = File.join(DOTFILES_ROOT, source)
    actual = File.symlink?(target) ? File.readlink(target) : nil

    if actual == expected
      puts "ok symlink #{target} -> #{actual}"
    elsif File.exist?(target)
      failures << "#{target} exists but does not point to #{expected}"
    else
      failures << "#{target} is missing"
    end
  end

  if LINKABLES.any? { |source, target_name| source.start_with?('codex/skills') || target_name.start_with?('.codex/skills') }
    failures << 'Codex skills must not be managed by this dotfiles inventory; use the agent-skills repo'
  else
    puts 'ok codex skills unmanaged by dotfiles inventory'
  end

  if codex_skill_paths.empty?
    puts 'ok no codex skills stored in dotfiles'
  else
    failures << "Codex skill paths are present in dotfiles: #{codex_skill_paths.join(', ')}"
  end

  codex_auth_path = link_target(CODEX_AUTH_JSON)
  if File.symlink?(codex_auth_path)
    failures << "#{codex_auth_path} must remain local-only and must not be a symlink"
  elsif File.file?(codex_auth_path)
    puts "ok codex auth local-only #{codex_auth_path}"
  else
    failures << "#{codex_auth_path} is missing; run codex login after setup"
  end

  codex_secret_failures = codex_config_secret_failures
  failures.concat(codex_secret_failures)
  puts 'ok codex config secret scan' if codex_secret_failures.empty?

  codex_template_failures = codex_template_portability_failures
  failures.concat(codex_template_failures)
  puts 'ok codex template portable' if codex_template_failures.empty?

  REQUIRED_COMMANDS.each do |command|
    if system("command -v #{Shellwords.escape(command)} >/dev/null 2>&1")
      puts "ok command #{command}"
    else
      failures << "missing command: #{command}"
    end
  end

  if system('zsh', '-lic', '[[ $PROMPT == *prompt_pure* ]]')
    puts 'ok zsh prompt Pure'
  else
    failures << 'zsh prompt is not Pure'
  end

  docs_failures = docs_check_failures(readme)
  failures.concat(docs_failures)

  puts 'ok docs drift check' if docs_failures.empty?

  if git_config_value('gpg.format') == 'ssh'
    puts 'ok git gpg.format ssh'
  else
    failures << 'git gpg.format is not ssh'
  end

  signing_key = git_config_value('user.signingkey')
  expected_signing_key = File.join(ENV.fetch('HOME'), SSH_SIGNING_KEY)
  expanded_signing_key = expand_home(signing_key)
  if expanded_signing_key == expected_signing_key
    puts "ok git user.signingkey #{signing_key}"
  else
    failures << "git user.signingkey is #{signing_key.inspect}, expected #{expected_signing_key.inspect}"
  end

  if File.readable?(expanded_signing_key)
    puts "ok ssh signing public key #{expanded_signing_key}"
  else
    failures << "ssh signing public key #{expanded_signing_key} is missing; restore it from Bitwarden and add it to GitHub as a signing key"
  end

  private_signing_key = expanded_signing_key.sub(/\.pub\z/, '')
  if File.readable?(private_signing_key)
    puts "ok ssh signing private key #{private_signing_key}"
  else
    failures << "ssh signing private key #{private_signing_key} is missing; restore it from Bitwarden"
  end

  if git_config_value('commit.gpgsign') == 'true'
    puts 'ok git commit.gpgsign true'
  else
    failures << 'git commit.gpgsign is not true'
  end

  unless system({ 'HOMEBREW_NO_AUTO_UPDATE' => '1' }, 'brew', 'bundle', 'check', '--no-upgrade', '--file=osx/Brewfile')
    failures << 'brew bundle presence check failed for osx/Brewfile'
  end

  if failures.empty?
    puts 'doctor passed'
  else
    puts failures.map { |failure| "error #{failure}" }
    exit 1
  end
end

task :default => 'install'
