from typing import Any, List, Optional

from pydantic import BaseModel
from tgboost.processing.validation import SmilesDataInputSchema
from tgboost.processing.validation import MultipleSmilesDataInputs


class PredictionResults(BaseModel):
    errors: Optional[Any]
    version: str
    predictions: Optional[List[float]]


class MultipleSmilesDataInputs(BaseModel):
    inputs: List[SmilesDataInputSchema]
    
    class Config:
        # There might be an error here, it should be "SMILE" : "np.array([embedding])"
        # JSON does not read np.arrays, so most likely you have to convert the array
        # to a list
        schema_extra = {
            "example": {
                "inputs": [
                    {"SMILES": "Oc1cccc(O)c1"},
                ]
            }
        }
