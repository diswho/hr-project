from sqlalchemy import DateTime
from sqlmodel import Field, SQLModel


class HRCompanyBase(SQLModel):
    cmp_code: str | None = None
    cmp_dateformat: str | None = None
    cmp_timeformat: str | None = None
    cmp_name: str
    cmp_operationmode: int | None = None
    cmp_address1: str | None = None
    cmp_address2: str | None = None
    cmp_city: str | None = None
    cmp_state: str | None = None
    cmp_country: str | None = None
    cmp_postal: str | None = None
    cmp_phone: str | None = None
    cmp_fax: str | None = None
    cmp_email: str | None = None
    # cmp_logo: bytes | None = None
    cmp_showlogoInreport: bool | None = None
    cmp_website: str | None = None
    autoSendSMS: bool | None = None
    onlyFirstInOut: bool | None = None
    sendSMSByDepartment: bool | None = None
    prefix: str | None = None
    token: str | None = None
    sendWithAttPhoto: bool | None = None
    sendDailyAttSummary: bool | None = None
    attSummarySendTime: DateTime | None = None
    SendLineOnWeekendAndHoliday: int | None = None


class HRCompanyCreate(HRCompanyBase):
    pass


class HRCompany(HRCompanyBase, table=True):
    id: int | None = Field(default=None, primary_key=True)


class HRCompanyUpdate(HRCompanyBase):
    cmp_name: str | None = None
