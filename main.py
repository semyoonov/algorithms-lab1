import pytest
from plot import generate_plots

if __name__ == "__main__":
    pytest.main(["-s", "tests/test.py", "test_time.py"])
    generate_plots()
