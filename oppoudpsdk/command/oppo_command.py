from typing import List
from ..codes import *
from dataclasses import dataclass

@dataclass(repr=True, eq=True)
class OppoCommand:
  code: OppoCodeType
  _parameters: List[str]
  _response_codes: List[str]

  def __init__(self, code: OppoCodeType, parameters: List[str] = [], response_codes: List[str] = []):
    self.code = self._translate(code)
    self._parameters = parameters
    self._response_codes = response_codes + [self.code.value]

  def encode(self):
    params = ""
    if len(self._parameters) > 0:
      params = " " + " ".join(list(map(str, self._parameters)))
    return f"#{self.code.value}{params}\r".encode()

  @property
  def expected_response_codes(self):
    return self._response_codes

  def _translate(self, code: OppoCodeType):
    if isinstance(code, str):
      return OppoCode(code)
    return code


