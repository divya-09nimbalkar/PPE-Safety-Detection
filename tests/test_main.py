import os
from src.main import detect_ppe

def test_sample_image():
    sample_path = "data/raw/sample.jpg"
    assert os.path.exists(sample_path), "Sample image missing!"
    detect_ppe(sample_path)
