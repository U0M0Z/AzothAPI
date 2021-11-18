import math

import numpy as np
import pandas as pd
import tgboost.processing.smiles_manager as sm
from fastapi.testclient import TestClient
from tgboost.config.core import config
from tgboost.predict import make_prediction


def test_make_prediction(client: TestClient, test_data: pd.DataFrame) -> None:
    # Given
    # result = test_data.values.tolist()
    result = make_prediction(input_data=test_data)

    transformer = sm.SmilesWrapper(
        variables=[config.model_config.smiles_to_extract],
        param_scaler=config.model_config.scaler,
    )

    embedder = sm.SmilesEmbedder(variables=[config.model_config.smiles_to_embed])

    df_input = pd.DataFrame(test_data)

    transformation = transformer.fit_transform(df_input)
    df_embedded = embedder.fit_transform(transformation)
    df_embedded.columns = ["SMILES", "embeddings"]
    df_embedded["embeddings"] = df_embedded["embeddings"].apply(lambda x: x.tolist())
    df_embedded["predictions"] = result["predictions"]

    payload = {
        # ensure pydantic plays well with np.nan
        # "inputs": df_embedded[["SMILES", "embeddings", "predictions"]]
        "inputs": df_embedded.replace({np.nan: None}).to_dict(orient="records")
    }

    # When
    response = client.post(
        "http://localhost:8001/api/v1/predict",
        json=payload,
    )

    # Then
    assert response.status_code == 200
    prediction_data = response.json()
    assert prediction_data["predictions"]
    assert prediction_data["errors"] is None
    assert math.isclose(prediction_data["predictions"][0], 230.6, rel_tol=10)
