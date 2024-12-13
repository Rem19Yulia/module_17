from models import Base, User, Task 
target_metadata = Base.metadata 

alembic revision --autogenerate -m "Initial migration

alembic upgrade head
