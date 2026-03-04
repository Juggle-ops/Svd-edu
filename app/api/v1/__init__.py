"""
API v1 版本路由
"""

from fastapi import APIRouter
from app.api.v1 import teaching, evaluation, teacher, student, course, security

# 创建主路由
api_router = APIRouter()

# 注册子路由
api_router.include_router(teaching.router, prefix="/teaching", tags=["教学优化"])
api_router.include_router(evaluation.router, prefix="/evaluation", tags=["教学评价"])
api_router.include_router(teacher.router, prefix="/teacher", tags=["教师管理"])
api_router.include_router(student.router, prefix="/student", tags=["学生管理"])
api_router.include_router(course.router, prefix="/course", tags=["课程管理"])
api_router.include_router(security.router, prefix="/security", tags=["安全管理"]) 