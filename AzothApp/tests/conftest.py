from typing import Generator

import pandas as pd
import pytest
import tgboost.processing.smiles_manager as sm
from fastapi.testclient import TestClient
from tgboost.config.core import DATASET_DIR, config

from AzothApp.main import app


@pytest.fixture(scope="module")
def test_data() -> pd.DataFrame:
    return sm.DatabaseExtractor().extract(
        file=str(DATASET_DIR) + "/" + config.app_config.test_data_file
    )


@pytest.fixture()
def client() -> Generator:
    with TestClient(app) as _client:
        yield _client
        app.dependency_overrides = {}
