from pydantic import BaseModel
from pydantic import Field
import typing

class PhraseInput(BaseModel):
    """Phrase model"""

    author: str = "Anonymous"
    text: str = Field(..., 
                      title="Text", 
                      description="Text of phrase", 
                      max_length=200
                      )
    
class PhraseOutput(PhraseInput):
    id: typing.Optional[int] = None  # ID фразы в нашей базе данных.
