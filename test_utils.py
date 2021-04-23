
from utils import genname


def test_genname():
    assert len(genname(0)) == 0
    assert len(genname(10)) == 10 and type(genname(10)) is str

