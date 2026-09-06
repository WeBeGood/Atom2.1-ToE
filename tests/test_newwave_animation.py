"""Exercise full-space field equations without requiring rendering libraries."""
import importlib.util
from pathlib import Path

def test_newwave_field_checks():
    path=Path(__file__).resolve().parents[1]/'code/newwave_animation/animate.py'
    spec=importlib.util.spec_from_file_location('newwave_animation',path)
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.verify()
