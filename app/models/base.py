"""
基础数据模型
"""

from sqlalchemy import Column, Integer, DateTime, Boolean
from sqlalchemy.sql import func
from app.core.database import Base
from datetime import datetime

class BaseModel(Base):
    """基础模型类"""
    __abstract__ = True
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    is_active = Column(Boolean, default=True)
    
    def to_dict(self):
        """转换为字典"""
        return {
            column.name: getattr(self, column.name)
            for column in self.__table__.columns
        }
    
    def update(self, **kwargs):
        """更新字段"""
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.updated_at = datetime.utcnow() 