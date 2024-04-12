import sys
from pathlib import Path

# This allows easy placement of apps within the interior
# coding_challenge directory.
ROOT_DIR = Path(__file__).resolve(strict=True).parent.parent
sys.path.append(str(ROOT_DIR / "coding_challenge"))
