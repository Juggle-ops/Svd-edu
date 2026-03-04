from fastapi import APIRouter, HTTPException
from typing import Dict, Any
import random
from datetime import datetime, timedelta

router = APIRouter()

@router.get("/stats")
async def get_dashboard_stats() -> Dict[str, Any]:
    """获取仪表板统计数据"""
    try:
        # 模拟统计数据
        stats = {
            "total_teachers": 45,
            "total_students": 1200,
            "total_courses": 28,
            "total_evaluations": 856,
            "avg_evaluation_score": 87.5,
            "bilingual_course_ratio": 65.2
        }
        
        return {
            "success": True,
            "data": stats,
            "message": "获取统计数据成功"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取统计数据失败: {str(e)}")

@router.get("/charts/{chart_type}")
async def get_chart_data(chart_type: str) -> Dict[str, Any]:
    """获取图表数据"""
    try:
        if chart_type == "score_distribution":
            # 评价分数分布数据
            data = {
                "labels": ["优秀 (90-100)", "良好 (80-89)", "中等 (70-79)", "及格 (60-69)"],
                "datasets": [{
                    "label": "评价分数分布",
                    "data": [35, 45, 15, 5],
                    "backgroundColor": ["#52c41a", "#1890ff", "#faad14", "#ff4d4f"]
                }]
            }
        elif chart_type == "bilingual_trend":
            # 双语课程趋势数据
            months = ["1月", "2月", "3月", "4月", "5月", "6月"]
            data = {
                "labels": months,
                "datasets": [
                    {
                        "label": "双语课程数量",
                        "data": [12, 15, 18, 22, 25, 28],
                        "borderColor": "#1890ff",
                        "backgroundColor": "rgba(24, 144, 255, 0.1)"
                    },
                    {
                        "label": "平均评价分数",
                        "data": [85, 87, 89, 88, 91, 93],
                        "borderColor": "#52c41a",
                        "backgroundColor": "rgba(82, 196, 26, 0.1)"
                    }
                ]
            }
        elif chart_type == "department_distribution":
            # 院系分布数据
            data = {
                "labels": ["计算机学院", "外语学院", "商学院", "理学院", "工学院"],
                "datasets": [{
                    "label": "教师数量",
                    "data": [12, 8, 10, 7, 8],
                    "backgroundColor": ["#1890ff", "#52c41a", "#faad14", "#ff4d4f", "#722ed1"]
                }]
            }
        elif chart_type == "evaluation_trend":
            # 评价趋势数据
            dates = [(datetime.now() - timedelta(days=i)).strftime("%m-%d") for i in range(30, 0, -1)]
            data = {
                "labels": dates,
                "datasets": [{
                    "label": "每日评价数量",
                    "data": [random.randint(10, 30) for _ in range(30)],
                    "borderColor": "#1890ff",
                    "backgroundColor": "rgba(24, 144, 255, 0.1)"
                }]
            }
        else:
            raise HTTPException(status_code=400, detail="不支持的图表类型")
        
        return {
            "success": True,
            "data": data,
            "message": "获取图表数据成功"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取图表数据失败: {str(e)}")

@router.get("/recent-activities")
async def get_recent_activities() -> Dict[str, Any]:
    """获取最近活动"""
    try:
        activities = [
            {
                "id": 1,
                "type": "evaluation",
                "title": "新评价提交",
                "description": "张教授收到了来自李同学的新评价",
                "timestamp": "2024-01-15 14:30:00"
            },
            {
                "id": 2,
                "type": "course",
                "title": "新课程创建",
                "title": "王教授创建了新课程《国际商务》",
                "timestamp": "2024-01-15 13:15:00"
            },
            {
                "id": 3,
                "type": "ai_optimization",
                "title": "AI优化建议",
                "description": "系统为《英语语言学》课程生成了优化建议",
                "timestamp": "2024-01-15 12:00:00"
            },
            {
                "id": 4,
                "type": "teacher",
                "title": "新教师注册",
                "description": "刘教授完成了系统注册",
                "timestamp": "2024-01-15 11:45:00"
            }
        ]
        
        return {
            "success": True,
            "data": activities,
            "message": "获取最近活动成功"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取最近活动失败: {str(e)}")

@router.get("/performance-metrics")
async def get_performance_metrics() -> Dict[str, Any]:
    """获取性能指标"""
    try:
        metrics = {
            "system_uptime": "99.8%",
            "response_time": "120ms",
            "active_users": 156,
            "daily_requests": 2847,
            "error_rate": "0.2%",
            "cpu_usage": "45%",
            "memory_usage": "62%",
            "disk_usage": "38%"
        }
        
        return {
            "success": True,
            "data": metrics,
            "message": "获取性能指标成功"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取性能指标失败: {str(e)}") 