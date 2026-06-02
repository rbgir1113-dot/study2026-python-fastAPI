from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from app.infrastructure.oracle import get_oracle_db

# DYO, VO, Query, DB session

# DML 자동적으로 만들어줌
from sqlalchemy import select, update, insert, delete


class DefaultRepositoty:

  # 생성자 주입
  def __init__(self, db: AsyncSession):
    self.db = db


# 주입 팩토리 메서드
def get_default_repository(db: AsyncSession = Depends(get_oracle_db)):
  return DefaultRepositoty(db)

