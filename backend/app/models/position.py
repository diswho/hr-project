from typing import TYPE_CHECKING, Optional
from sqlalchemy import ForeignKey
from sqlmodel import Field, SQLModel

if TYPE_CHECKING:
    from .company import HRCompany


class HRPositionBase(SQLModel):
    posi_code: int
    posi_name: str
    description: str | None = None
    posi_parentcode: int
    defaultPosition: int | None = None
    company: Optional["HRCompany"] = ForeignKey(sa_column="company_id")


class HRPosition(HRPositionBase, table=True):
    id: int | None = Field(default=None, primary_key=True)


class HRPositionCreate(HRPositionBase):
    pass


class HRPositionUpdate(HRPositionBase):
    posi_code: int | None = None
    posi_name: str | None = None
    posi_parentcode: int | None = None
    company: Optional["HRCompany"] | None = None
