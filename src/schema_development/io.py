"""Small JSON helpers used by the historical notebooks."""

import json
from pathlib import Path
from typing import Any


def load_json(path: str | Path) -> Any:
    """Load a UTF-8 JSON document.

    Parameters
    ----------
    path : str | Path
        JSON file to read.

    Returns
    -------
    Any
        Decoded JSON value.
    """
    return json.loads(Path(path).read_text(encoding="utf-8"))
