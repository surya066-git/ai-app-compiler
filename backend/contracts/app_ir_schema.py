from pydantic import BaseModel, Field
from typing import List, Optional

class DBField(BaseModel):
    name: str
    type: str = Field(description="SQL type, e.g. String, Integer")
    is_primary_key: bool = False
    is_foreign_key: bool = False
    references: Optional[str] = None

class DBTable(BaseModel):
    name: str
    fields: List[DBField]

class APIEndpoint(BaseModel):
    method: str = Field(description="GET, POST, PUT, DELETE")
    path: str
    requires_auth: bool = False
    description: str

class UIPage(BaseModel):
    name: str
    route: str
    description: str
    requires_auth: bool = False

class AppIR(BaseModel):
    app_name: str
    description: str
    tables: List[DBTable]
    endpoints: List[APIEndpoint]
    pages: List[UIPage]
    roles: List[str]
    assumptions: List[str] = []
