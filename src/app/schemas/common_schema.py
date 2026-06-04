from pydantic import BaseModel
from typing import Generic, TypeVar

T = TypeVar("T")

class ApiResponseDTO(BaseModel, Generic[T]):
  success : bool
  message : str
  # None=None이 Optional 처리방법
  data: T | None=None #Optional
  