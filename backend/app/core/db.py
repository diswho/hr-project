from sqlmodel import SQLModel, Session, create_engine, select

from app import crud
from app.core.config import settings
# from app.models.user import User, UserCreate
from app.models.company import HRCompanyCreate
from app.models.department import HRDepartmentCreate
from app.models.position import HRPositionCreate
from app.models.employee import HREmployee, HREmployeeCreate

engine = create_engine(str(settings.SQLALCHEMY_DATABASE_URI))


# make sure all SQLModel models are imported (app.models) before initializing DB
# otherwise, SQLModel might fail to initialize relationships properly
# for more details: https://github.com/tiangolo/full-stack-fastapi-template/issues/28


def init_db(session: Session) -> None:
    # Tables should be created with Alembic migrations
    # But if you don't want to use migrations, create
    # the tables un-commenting the next lines
    # from sqlmodel import SQLModel

    # from app.core.engine import engine
    # This works because the models are already imported and registered from app.models
    SQLModel.metadata.create_all(engine)
    company=HRCompanyCreate(cmp_name="Xtv")


    user = session.exec(
        select(HREmployee).where(HREmployee.email == settings.FIRST_SUPERUSER)
    ).first()
    if not user:
        user_in = HREmployeeCreate(
            email=settings.FIRST_SUPERUSER,
            password=settings.FIRST_SUPERUSER_PASSWORD,
            is_superuser=True,
        )
        user = crud.create_user(session=session, user_create=user_in)
