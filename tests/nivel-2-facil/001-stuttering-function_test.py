

import pytest
import sys
sys.path.insert(0, '/var/www/html/retos-python-backend/nivel-2-facil/001-stuttering-function/')
from stuttering import stutter

def test_stutter():
    assert stutter("incredible") == "in... in... incredible?"
    assert stutter("enthusiastic") == "en... en... enthusiastic?"
    assert stutter("outstanding") == "ou... ou... outstanding?"
    with pytest.raises(TypeError):
        stutter(233)
        stutter(1.23)
        stutter(True)
        stutter(["Hello"])
        stutter(("Hello",))
        stutter({"Hello": "Hello"})
        stutter(None)
        stutter()

