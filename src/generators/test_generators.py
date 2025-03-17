from src.generators import data_generator as dg
import pytest
import tempfile
from pathlib import Path
import pandas as pd

@pytest.fixture
def test_data():
    return dg.DataGenerator("test",10*1024)

class TestDataGenerator:

    def test_generate(self, test_data):
        assert not test_data.generate().empty

    def test_write(self, test_data):
        d = Path( tempfile.gettempdir() )
        
        f = test_data.write(d)

        df = pd.read_json(f)
        assert not df.empty


if __name__ == "__main__":
    pytest.main([__file__])