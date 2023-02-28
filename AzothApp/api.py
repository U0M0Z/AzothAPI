import json
from typing import Any

import pandas as pd
from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder
from loguru import logger
from tgboost import __version__ as model_version
from tgboost.predict import make_prediction

from AzothApp import __version__, schemas
from AzothApp.config import settings


api_router = APIRouter()

# Here we define the other routers to be used
@api_router.get("/health", response_model=schemas.Health, status_code=200)
def health() -> dict:
    """
    Root Get
    """
    health = schemas.Health(
        name=settings.PROJECT_NAME, api_version=__version__, model_version=model_version
    )

    return health.dict()


@api_router.post("/predict", response_model=schemas.PredictionResults, status_code=200)
async def predict(input_data: schemas.predict.MultipleSmilesDataInputs) -> Any:

    print('My name is tgBoost')
    """
    Make $T_{g}$ prediction with the tgBoost model
    """

    input_SMILES_list = jsonable_encoder(input_data.inputs)[0]['SMILES'].replace(' ', '').split(',')

    input_df = pd.DataFrame()
    input_df['SMILES'] = input_SMILES_list
    print(input_df)

    # Advanced: You can improve performance of your API by rewriting the
    # `make prediction` function to be async and using await here.
    logger.info(f"Making prediction on inputs: {input_data.inputs}")
    # results = make_prediction(input_data=input_df.replace({np.nan: None}))
    results = make_prediction(input_data=input_df)
    print('results =', results)

    if results["errors"] is not None:
        logger.warning(f"Prediction validation error: {results.get('errors')}")
        raise HTTPException(status_code=400, detail=json.loads(results["errors"]))

    logger.info(f"Prediction results: {results.get('predictions')}")

    return results
