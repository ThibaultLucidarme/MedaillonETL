import pandas as pd
import numpy as np
from pathlib import Path
from sys import getsizeof
import tempfile

class DataGenerator:
    def __init__(self, name, batch_size:int, nb_col:int=10):
        self.name = name
        self.nb_col = nb_col
        self.nb_row = int(batch_size/nb_col/getsizeof(int) )
        self.batch_size = batch_size
    def generate(self) -> pd.DataFrame:
        return pd.DataFrame(
            np.random.random((self.nb_row,self.nb_col))
        )
    def write(self,path:Path) -> Path:
        if path.is_dir(): 
            path = path / tempfile.mktemp(prefix=self.name,suffix=".json", dir=path)
        self.generate().to_json(path)
        return path