import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from main import main


def test_main():
    """Test that main runs without errors"""
    main()
