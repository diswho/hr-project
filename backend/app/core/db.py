from sqlmodel import SQLModel, Session, create_engine, select

from app import crud
from app.core.config import settings
# from app.models.user import User, UserCreate
from app.models.company import HRCompanyCreate
from app.models.department import HRDepartmentCreate
from app.models.position import HRPositionCreate
from app.models.employee import HREmployee, HREmployeeCreate

engine = create_engine(str(settings.SQLALCHEMY_DATABASE_URI), echo=False)


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

    user = session.exec(
        select(HREmployee).where(HREmployee.email == settings.FIRST_SUPERUSER)
    ).first()
    if not user:
        company_in = HRCompanyCreate(cmp_name="my company")
        company = crud.create_company(session=session, company_create=company_in)

        department_in = HRDepartmentCreate(dept_code=1, dept_parentcode=0, dept_name="IT", company_id=company.id)
        department_in.company = company
        department = crud.create_department(session=session, department_create=department_in)

        position_in = HRPositionCreate(posi_code=1, posi_name="Manager", posi_parentcode=0, company_id=company.id)
        position = crud.create_position(session=session, position_create=position_in)

        user_in = HREmployeeCreate(
            email=settings.FIRST_SUPERUSER,
            password=settings.FIRST_SUPERUSER_PASSWORD,
            is_superuser=True,
            department_id=department.id,
            position_id=position.id
        )
        user = crud.create_user(session=session, user_create=user_in)
