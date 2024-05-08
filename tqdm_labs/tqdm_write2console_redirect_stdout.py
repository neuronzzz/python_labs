import contextlib
import sys
import time

from tqdm import tqdm


class DummyFile:
    def __init__(self, file):
        if file is None:
            file = sys.stderr
        self.file = file

    def write(self, x):
        if len(x.rstrip()) > 0:
            tqdm.write(x, file=self.file)


@contextlib.contextmanager
def redirect_stdout(file=None):
    if file is None:
        file = sys.stderr
    old_stdout = file
    sys.stdout = DummyFile(file)
    yield
    sys.stdout = old_stdout


for batch in tqdm(range(100), position=0, desc="desc"):
    time.sleep(0.1)
    with redirect_stdout():
        print(batch)
