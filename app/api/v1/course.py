"""
课程管理API路由
"""

from fastapi import APIRouter, HTTPException
from typing import Dict, List, Any, Optional

router = APIRouter()

@router.get("/")
async def get_courses(
    skip: int = 0,
    limit: int = 10,
    subject: Optional[str] = None
):
    """获取课程列表"""
    try:
        # 模拟课程数据
        courses = [
            {
                "id": 1,
                "name": "Python编程基础",
                "code": "CS101",
                "subject": "计算机科学",
                "teacher_name": "张老师",
                "credits": 3,
                "status": "active"
            },
            {
                "id": 2,
                "name": "数据结构与算法",
                "code": "CS201",
                "subject": "计算机科学",
                "teacher_name": "李老师",
                "credits": 4,
                "status": "active"
            }
        ]
        
        return {
            "success": True,
            "data": courses[skip:skip+limit],
            "total": len(courses),
            "message": "课程列表获取成功"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取课程列表失败: {str(e)}")

@router.get("/{course_id}")
async def get_course(course_id: int):
    """获取课程详情"""
    try:
        # 模拟课程详情数据
        course = {
            "id": course_id,
            "name": f"课程{course_id}",
            "code": f"CS{course_id:03d}",
            "description": "这是一门双语教学课程",
            "subject": "计算机科学",
            "level": "intermediate",
            "credits": 3,
            "duration": 48,
            "primary_language": "chinese",
            "secondary_language": "english",
            "language_ratio": {"chinese": 0.7, "english": 0.3},
            "max_students": 50,
            "current_students": 35,
            "status": "active",
            "overall_rating": 0.82,
            "total_evaluations": 45
        }
        
        return {
            "success": True,
            "data": course,
            "message": "课程详情获取成功"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取课程详情失败: {str(e)}")

@router.post("/")
async def create_course(course_data: Dict[str, Any]):
    """创建课程"""
    try:
        # 模拟创建课程
        new_course = {
            "id": 999,
            **course_data,
            "created_at": "2024-01-01T00:00:00Z"
        }
        
        return {
            "success": True,
            "data": new_course,
            "message": "课程创建成功"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"创建课程失败: {str(e)}")

@router.put("/{course_id}")
async def update_course(course_id: int, course_data: Dict[str, Any]):
    """更新课程信息"""
    try:
        # 模拟更新课程
        updated_course = {
            "id": course_id,
            **course_data,
            "updated_at": "2024-01-01T00:00:00Z"
        }
        
        return {
            "success": True,
            "data": updated_course,
            "message": "课程信息更新成功"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"更新课程信息失败: {str(e)}")

@router.delete("/{course_id}")
async def delete_course(course_id: int):
    """删除课程"""
    try:
        return {
            "success": True,
            "data": {"course_id": course_id},
            "message": "课程删除成功"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"删除课程失败: {str(e)}") 