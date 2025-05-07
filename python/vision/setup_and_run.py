import os
import subprocess
import sys
import venv
from pathlib import Path

# Setup paths
venv_dir = Path("venv")
flag_file = Path(".setup_complete")
python_exe = venv_dir / "Scripts" / "python.exe" if os.name == "nt" else venv_dir / "bin" / "python"

# Handle --force override
force = "--force" in sys.argv

# Check for setup completion
if flag_file.exists() and not force:
    print("⚠️  Setup has already been completed. To rerun, use: python setup_and_run.py --force")
    sys.exit(0)

# 1. Create virtual environment if needed
if not venv_dir.exists():
    print("🛠️  Creating virtual environment...")
    venv.create(venv_dir, with_pip=True)
else:
    print("✅ Virtual environment already exists.")

# 2. Install dependencies
print("📦 Installing dependencies...")
subprocess.check_call([str(python_exe), "-m", "pip", "install", "--upgrade", "pip"])
req_path = Path(__file__).parent / "requirements.txt"
subprocess.check_call([str(python_exe), "-m", "pip", "install", "-r", str(req_path)])

# 3. Mark setup as complete (unless --force)
if not flag_file.exists():
    flag_file.write_text("Setup complete")

# 4. Run webcam detection
print("🎯 Running webcam detection...")
webcam_script = Path(__file__).parent / "yolov5" / "run_webcam.py"
subprocess.check_call([str(python_exe), str(webcam_script)])
