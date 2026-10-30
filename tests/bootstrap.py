"""Run with python3 tests/bootstrap.py; all writes stay in a temporary home."""
import os
from pathlib import Path
import shutil
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
MISE = shutil.which("mise")

with tempfile.TemporaryDirectory(prefix="dotfiles-check-") as directory:
    home = Path(directory)
    env = dict(os.environ, HOME=str(home), MISE_CONFIG_DIR=str(home / "config"),
               MISE_STATE_DIR=str(home / "state"), MISE_CACHE_DIR=str(home / "cache"),
               MISE_DATA_DIR=str(home / "data"), MISE_TRUSTED_CONFIG_PATHS=str(ROOT))

    def run(*args, success=True):
        result = subprocess.run(args, cwd=ROOT, env=env, text=True, capture_output=True)
        assert (result.returncode == 0) == success, result.stdout + result.stderr
        return result

    # The guard removes only empty secondary Ghostty configs.
    ghostty = home / "Library/Application Support/com.mitchellh.ghostty/config.ghostty"
    ghostty.parent.mkdir(parents=True)
    ghostty.touch()
    run("rake", "setup:ghostty")
    assert not ghostty.exists()
    ghostty.write_text("theme = local\n")
    run("rake", "setup:ghostty", success=False)
    assert ghostty.read_text() == "theme = local\n"
    run(MISE, "bootstrap", "--only", "dotfiles", "--yes", success=False)
    assert not (home / ".gitconfig").exists()
    ghostty.unlink()

    # An unmanaged destination must survive a failed apply unchanged.
    conflict = home / ".gitconfig"
    conflict.write_text("local config\n")
    run(MISE, "bootstrap", "--only", "dotfiles", "--yes", success=False)
    assert not conflict.is_symlink() and conflict.read_text() == "local config\n"
    conflict.unlink()
    run(MISE, "bootstrap", "--only", "dotfiles", "--yes")
    run(MISE, "dot", "status", "--missing")
    for target, source in {
        ".codex/agents": "codex/agents.symlink",
        ".gitattributes": "git/gitattributes.symlink",
        ".gitconfig": "git/gitconfig.symlink",
        ".config/ghostty/config.ghostty": "ghostty/config.ghostty.symlink",
        ".hushlogin": "osx/hushlogin.symlink",
        ".zprofile": "zsh/zprofile.symlink",
        ".zshrc": "zsh/zshrc.symlink",
    }.items():
        assert (home / target).is_symlink()
        assert (home / target).resolve() == (ROOT / source).resolve()
    run(MISE, "bootstrap", "--only", "dotfiles", "--yes")
    assert not (home / ".codex/auth.json").exists()
    assert not (home / ".codex/skills").exists()

print("bootstrap checks passed")
