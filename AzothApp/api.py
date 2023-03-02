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

from pydantic import BaseModel
from typing import Optional, List
from fastapi import Query
from enum import Enum


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

@api_router.post("/predict", response_model=schemas.predict.PredictionResults, status_code=200)
async def predict(input_data: schemas.predict.MultipleSmilesDataList) -> Any:

    print('My name is tgBoost')
    """
    Make $T_{g}$ prediction with the tgBoost model
    """

    print(jsonable_encoder(input_data.inputs))

    #input_SMILES_list = jsonable_encoder(input_data.inputs)[0]['SMILES'].replace(' ', '').split(',')
    #input_df['SMILES'] = input_SMILES_list

    input_df = pd.DataFrame(jsonable_encoder(input_data.inputs))

    print(input_df)

    # Advanced: You can improve performance of your API by rewriting the
    # `make prediction` function to be async and using await here.
    logger.info(f"Making prediction on inputs: {input_data.inputs}")
    results = make_prediction(input_data=input_df)
    print('results =', results)

    if results["errors"] is not None:
        logger.warning(f"Prediction validation error: {results.get('errors')}")
        raise HTTPException(status_code=400, detail=json.loads(results["errors"]))

    logger.info(f"Prediction results: {results.get('predictions')}")

    return results




class tgBoost_model(BaseModel):
    version: str = __version__
    base_algorithm: str = 'tgBoost'

@api_router.post("/predict_smiles_explicitely", response_model = schemas.predict.PredictionResults, status_code=200)
async def predict_from_manual_smiles_inputs(model: tgBoost_model,
                                        SMILES: Optional[List[str]] = Query(None,
                                        description = "Insert Canonical SMILES (one by one)"
                                        )
                                    ) -> Any:

    input_df = pd.DataFrame(columns = ['SMILES'])
    smi_list = SMILES
    input_df['SMILES'] = smi_list
    
    results = make_prediction(input_data=input_df)

    if results["errors"] is not None:
        logger.warning(f"Prediction validation error: {results.get('errors')}")
        raise HTTPException(status_code=400, detail=json.loads(results["errors"]))

    logger.info(f"Prediction results: {results.get('predictions')}")    

    return results
