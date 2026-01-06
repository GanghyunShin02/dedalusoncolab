from pathlib import Path
import subprocess
import sys

# ==================================================
# Repository root
# ==================================================
REPO_DIR = Path(__file__).resolve().parent

INSTALL_SCRIPT = REPO_DIR / "setup" / "install_dedalus.sh"
MAGIC_FILE     = REPO_DIR / "magic" / "dedalus_magic.py"

# ==================================================
# Helper
# ==================================================
def run(cmd, cwd=None):
    subprocess.run(
        cmd,
        cwd=cwd,
        check=True
    )

# ==================================================
# Sanity check
# ==================================================
if not INSTALL_SCRIPT.exists():
    raise FileNotFoundError(f"install_dedalus.sh not found: {INSTALL_SCRIPT}")

if not MAGIC_FILE.exists():
    raise FileNotFoundError(f"dedalus_magic.py not found: {MAGIC_FILE}")

# ==================================================
# 1. Install / update Dedalus environment
# ==================================================
print("🔧 Installing Dedalus environment...")
opts = sys.argv[1:]   # e.g. --clean
run(["bash", str(INSTALL_SCRIPT), *opts], cwd=REPO_DIR)

# ==================================================
# 2. Load %%dedalus magic into CURRENT kernel
# ==================================================
print("✨ Loading Dedalus Jupyter magic...", end=" ")

code = MAGIC_FILE.read_text()
exec(compile(code, str(MAGIC_FILE), "exec"), globals())

print("%%dedalus registered ✅")
