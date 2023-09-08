import time

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import get_async_session
from sqlalchemy import select, insert
from src.operations.models import operation
from src.operations.schemas import OperationCreate
from fastapi_cache.decorator import cache
from src.roles.schemas import CreateRole
from src.auth.models import role

router = APIRouter(
    prefix="/role"
)


@router.post("")
async def post_new_role(new_role: CreateRole, session: AsyncSession = Depends(get_async_session)):
    statement = insert(role).values(**new_role.dict())
    await session.execute(statement)
    await session.commit()
    return {
        "status": "success"
    }
