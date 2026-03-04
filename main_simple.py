"""
双语教学模式与质量评价机制系统 - 简化版本
用于测试基础功能
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import uvicorn
from datetime import datetime
import random
import time
from fastapi import Path

# 创建FastAPI应用
app = FastAPI(
    title="双语教学模式与质量评价机制系统",
    description="基于AI技术构建的一体化平台，优化双语教学流程与教学质量评价",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# 配置CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    """根路径"""
    return {
        "message": "双语教学模式与质量评价机制系统",
        "version": "1.0.0",
        "status": "running",
        "timestamp": datetime.now().isoformat()
    }

@app.get("/health")
async def health_check():
    """健康检查"""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat()
    }

def _mock_teachers(n: int = 20):
    """生成 n 名教师模拟数据"""
    subjects = ["计算机科学", "数学", "英语", "物理", "化学", "生物"]
    return [
        {
            "id": i,
            "name": f"教师{i}",
            "email": f"teacher{i}@example.com",
            "subject": subjects[(i - 1) % len(subjects)],
            "teaching_years": 1 + (i - 1) % 20,
            "overall_rating": round(0.6 + random.random() * 0.35, 2)
        }
        for i in range(1, n + 1)
    ]

def _mock_students(n: int = 500):
    """生成 n 名学生模拟数据"""
    majors = ["计算机科学", "数学", "英语", "物理", "化学", "生物", "经济学", "管理学"]
    grades = ["大一", "大二", "大三", "大四"]
    return [
        {
            "id": i,
            "name": f"学生{i}",
            "student_id": f"2021{i:04d}",
            "grade": grades[(i - 1) % len(grades)],
            "major": majors[(i - 1) % len(majors)]
        }
        for i in range(1, n + 1)
    ]

@app.get("/api/v1/teachers")
async def get_teachers():
    """获取教师列表（20 名）"""
    teachers = _mock_teachers(20)
    return {"success": True, "data": teachers, "total": len(teachers), "message": "教师列表获取成功"}

@app.get("/api/v1/students")
async def get_students():
    """获取学生列表（500 名）"""
    students = _mock_students(500)
    return {"success": True, "data": students, "total": len(students), "message": "学生列表获取成功"}

@app.get("/api/v1/courses")
async def get_courses():
    """获取课程列表"""
    courses = [
        {
            "id": 1,
            "name": "Python编程基础",
            "code": "CS101",
            "subject": "计算机科学",
            "teacher_name": "张老师",
            "credits": 3
        },
        {
            "id": 2,
            "name": "数据结构与算法",
            "code": "CS201",
            "subject": "计算机科学",
            "teacher_name": "李老师",
            "credits": 4
        }
    ]
    return {"success": True, "data": courses, "message": "课程列表获取成功"}

@app.get("/api/v1/dashboard/stats")
async def get_dashboard_stats():
    """获取仪表板统计数据（20 教师、500 学生）"""
    stats = {
        "total_teachers": 20,
        "total_students": 500,
        "total_courses": 28,
        "total_evaluations": 856,
        "avg_evaluation_score": 87.5,
        "bilingual_course_ratio": 65.2
    }
    return {"success": True, "data": stats, "message": "获取统计数据成功"}

@app.get("/api/v1/dashboard/charts/{chart_type}")
async def get_chart_data(chart_type: str):
    """获取图表数据"""
    if chart_type == "score_distribution":
        data = {
            "labels": ["优秀 (90-100)", "良好 (80-89)", "中等 (70-79)", "及格 (60-69)"],
            "datasets": [{
                "label": "评价分数分布",
                "data": [35, 45, 15, 5],
                "backgroundColor": ["#52c41a", "#1890ff", "#faad14", "#ff4d4f"]
            }]
        }
    elif chart_type == "bilingual_trend":
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
    else:
        data = {"labels": [], "datasets": []}
    
    return {"success": True, "data": data, "message": "获取图表数据成功"}

# AI优化相关API
@app.post("/api/v1/ai-optimization")
async def ai_optimization():
    """AI优化建议"""
    optimization_result = {
        "id": random.randint(1000, 9999),
        "course_id": 1,
        "optimization_type": "teaching_optimization",
        "recommendations": [
            "建议增加课堂互动环节，提高学生参与度",
            "可以尝试更多小组讨论活动，促进双语交流",
            "建议调整课程难度，适应不同水平学生",
            "推荐使用更多多媒体教学资源"
        ],
        "confidence_score": round(random.uniform(75, 95), 1),
        "created_at": datetime.now().isoformat()
    }
    return {"success": True, "data": optimization_result, "message": "AI优化建议生成成功"}

@app.get("/api/v1/ai-optimization/history")
async def get_optimization_history():
    """获取AI优化历史"""
    history = [
        {
            "id": 1,
            "course_id": 1,
            "optimization_type": "teaching_optimization",
            "recommendations": [
                "增加课堂互动环节",
                "使用更多双语教学资源"
            ],
            "confidence_score": 87.5,
            "created_at": "2024-01-15T10:30:00"
        },
        {
            "id": 2,
            "course_id": 2,
            "optimization_type": "content_optimization",
            "recommendations": [
                "优化课程内容结构",
                "增加实践案例分析"
            ],
            "confidence_score": 92.3,
            "created_at": "2024-01-14T14:20:00"
        }
    ]
    return {"success": True, "data": history, "message": "获取优化历史成功"}

# SVD++评价相关API
@app.get("/api/v1/evaluations/svd")
async def get_svd_evaluations():
    """获取SVD++评价结果"""
    svd_evaluations = [
        {
            "id": 1,
            "teacher_id": 1,
            "teacher_name": "张教授",
            "svd_score": 88.5,
            "factors": {
                "teaching_quality": 90,
                "student_satisfaction": 85,
                "course_difficulty": 75,
                "bilingual_effectiveness": 92
            },
            "recommendations": [
                "继续保持高质量的教学水平",
                "可以适当增加课程难度",
                "双语教学效果优秀，建议分享经验"
            ],
            "created_at": "2024-01-15T09:00:00"
        },
        {
            "id": 2,
            "teacher_id": 2,
            "teacher_name": "李教授",
            "svd_score": 82.3,
            "factors": {
                "teaching_quality": 85,
                "student_satisfaction": 80,
                "course_difficulty": 70,
                "bilingual_effectiveness": 78
            },
            "recommendations": [
                "建议提高双语教学效果",
                "可以增加学生互动环节",
                "课程难度适中，继续保持"
            ],
            "created_at": "2024-01-14T16:30:00"
        }
    ]
    return {"success": True, "data": svd_evaluations, "message": "获取SVD++评价成功"}

# 评价管理API
@app.get("/api/v1/evaluations")
async def get_evaluations():
    """获取评价列表"""
    evaluations = [
        {
            "id": 1,
            "course_id": 1,
            "course_name": "英语语言学",
            "teacher_id": 1,
            "teacher_name": "张教授",
            "student_id": 1,
            "student_name": "李同学",
            "evaluation_type": "课程评价",
            "score": 92,
            "feedback": "课程内容丰富，教师讲解清晰，双语教学效果很好。",
            "ai_analysis": "该评价显示学生对双语教学满意度较高，建议继续保持当前教学方式。",
            "created_at": "2024-01-15T14:30:00",
            "updated_at": "2024-01-15T14:30:00"
        },
        {
            "id": 2,
            "course_id": 2,
            "course_name": "计算机科学导论",
            "teacher_id": 2,
            "teacher_name": "王教授",
            "student_id": 2,
            "student_name": "陈同学",
            "evaluation_type": "教师评价",
            "score": 88,
            "feedback": "教师专业知识扎实，但可以增加更多互动环节。",
            "ai_analysis": "评价显示教师专业能力得到认可，建议增加课堂互动以提高学生参与度。",
            "created_at": "2024-01-14T13:15:00",
            "updated_at": "2024-01-14T13:15:00"
        }
    ]
    return {"success": True, "data": {"items": evaluations, "total": 2, "page": 1, "size": 10, "pages": 1}, "message": "获取评价列表成功"}

# 安全相关API
@app.get("/api/v1/security/logs")
async def get_security_logs():
    """获取安全日志"""
    logs = [
        {
            "id": 1,
            "user_id": 1,
            "user_type": "admin",
            "action": "登录系统",
            "ip_address": "192.168.1.100",
            "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "status": "success",
            "created_at": "2024-01-15T10:00:00"
        },
        {
            "id": 2,
            "user_id": 2,
            "user_type": "teacher",
            "action": "查看课程信息",
            "ip_address": "192.168.1.101",
            "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "status": "success",
            "created_at": "2024-01-15T09:30:00"
        }
    ]
    return {"success": True, "data": {"items": logs, "total": 2, "page": 1, "size": 10, "pages": 1}, "message": "获取安全日志成功"}

@app.get("/api/v1/security/alerts")
async def get_security_alerts():
    """获取安全警报"""
    alerts = [
        {
            "id": 1,
            "alert_type": "异常登录",
            "severity": "medium",
            "message": "检测到来自异常IP地址的登录尝试",
            "user_id": 3,
            "ip_address": "192.168.1.200",
            "resolved": False,
            "created_at": "2024-01-15T11:00:00"
        },
        {
            "id": 2,
            "alert_type": "权限访问",
            "severity": "low",
            "message": "用户尝试访问未授权资源",
            "user_id": 2,
            "ip_address": "192.168.1.101",
            "resolved": True,
            "created_at": "2024-01-15T08:00:00",
            "resolved_at": "2024-01-15T08:15:00"
        }
    ]
    return {"success": True, "data": {"items": alerts, "total": 2, "page": 1, "size": 10, "pages": 1}, "message": "获取安全警报成功"}

@app.put("/api/v1/security/alerts/{alert_id}/resolve")
async def resolve_security_alert(alert_id: int):
    """解决安全警报"""
    return {"success": True, "data": {"id": alert_id, "resolved": True, "resolved_at": datetime.now().isoformat()}, "message": "警报已解决"}

# 用户认证相关API

class LoginRequest(BaseModel):
    username: str
    password: str

@app.post("/api/v1/auth/login")
async def login(request: LoginRequest):
    """用户登录"""
    # 模拟用户验证
    users = [
        {
            "id": 1, 
            "username": "admin", 
            "password": "admin123", 
            "role": "admin", 
            "name": "系统管理员",
            "email": "admin@example.com",
            "avatar": "https://api.dicebear.com/7.x/avataaars/svg?seed=admin",
            "permissions": ["dashboard", "teachers", "students", "courses", "evaluations", "ai_optimization", "ai_analytics", "security"]
        },
        {
            "id": 2, 
            "username": "teacher", 
            "password": "teacher123", 
            "role": "teacher", 
            "name": "张教授",
            "email": "teacher@example.com",
            "avatar": "https://api.dicebear.com/7.x/avataaars/svg?seed=teacher",
            "permissions": ["dashboard", "courses", "evaluations", "ai_optimization", "ai_analytics"]
        },
        {
            "id": 3, 
            "username": "student", 
            "password": "student123", 
            "role": "student", 
            "name": "李同学",
            "email": "student@example.com",
            "avatar": "https://api.dicebear.com/7.x/avataaars/svg?seed=student",
            "permissions": ["dashboard", "courses", "evaluations"]
        }
    ]
    
    user = next((u for u in users if u["username"] == request.username and u["password"] == request.password), None)
    
    if user:
        token = f"token_{user['id']}_{int(time.time())}"
        return {
            "success": True,
            "data": {
                "token": token,
                "user": {
                    "id": user["id"],
                    "username": user["username"],
                    "role": user["role"],
                    "name": user["name"],
                    "email": user["email"],
                    "avatar": user["avatar"],
                    "permissions": user["permissions"]
                }
            },
            "message": "登录成功"
        }
    else:
        return {"success": False, "message": "用户名或密码错误"}

@app.post("/api/v1/auth/logout")
async def logout():
    """用户登出"""
    return {"success": True, "message": "登出成功"}

@app.get("/api/v1/auth/profile")
async def get_profile():
    """获取用户信息"""
    # 模拟用户数据
    users = [
        {
            "id": 1, 
            "username": "admin", 
            "role": "admin", 
            "name": "系统管理员",
            "email": "admin@example.com",
            "avatar": "https://api.dicebear.com/7.x/avataaars/svg?seed=admin",
            "permissions": ["dashboard", "teachers", "students", "courses", "evaluations", "ai_optimization", "ai_analytics", "security"]
        },
        {
            "id": 2, 
            "username": "teacher", 
            "role": "teacher", 
            "name": "张教授",
            "email": "teacher@example.com",
            "avatar": "https://api.dicebear.com/7.x/avataaars/svg?seed=teacher",
            "permissions": ["dashboard", "courses", "evaluations", "ai_optimization", "ai_analytics"]
        },
        {
            "id": 3, 
            "username": "student", 
            "role": "student", 
            "name": "李同学",
            "email": "student@example.com",
            "avatar": "https://api.dicebear.com/7.x/avataaars/svg?seed=student",
            "permissions": ["dashboard", "courses", "evaluations"]
        }
    ]
    
    # 为了演示，我们返回管理员信息
    # 在实际应用中，这里应该根据token解析用户ID，然后返回对应用户信息
    user = users[0]  # 默认返回管理员
    return {"success": True, "data": user, "message": "获取用户信息成功"}

@app.put("/api/v1/auth/profile")
async def update_profile():
    """更新用户信息"""
    return {"success": True, "message": "用户信息更新成功"}

@app.post("/api/v1/auth/change-password")
async def change_password():
    """修改密码"""
    return {"success": True, "message": "密码修改成功"}

# 权限管理API
@app.get("/api/v1/permissions")
async def get_permissions():
    """获取权限列表"""
    permissions = [
        {
            "id": 1,
            "name": "dashboard",
            "display_name": "仪表板",
            "description": "访问系统仪表板"
        },
        {
            "id": 2,
            "name": "teachers",
            "display_name": "教师管理",
            "description": "管理教师信息"
        },
        {
            "id": 3,
            "name": "students",
            "display_name": "学生管理",
            "description": "管理学生信息"
        },
        {
            "id": 4,
            "name": "courses",
            "display_name": "课程管理",
            "description": "管理课程信息"
        },
        {
            "id": 5,
            "name": "evaluations",
            "display_name": "评价管理",
            "description": "管理评价信息"
        },
        {
            "id": 6,
            "name": "ai_optimization",
            "display_name": "AI优化",
            "description": "访问AI优化功能"
        },
        {
            "id": 7,
            "name": "ai_analytics",
            "display_name": "AI分析",
            "description": "访问AI分析功能"
        },
        {
            "id": 8,
            "name": "security",
            "display_name": "安全管理",
            "description": "访问安全管理功能"
        }
    ]
    return {"success": True, "data": permissions, "message": "获取权限列表成功"}

@app.get("/api/v1/roles")
async def get_roles():
    """获取角色列表"""
    roles = [
        {
            "id": 1,
            "name": "admin",
            "display_name": "系统管理员",
            "description": "拥有所有权限",
            "permissions": ["dashboard", "teachers", "students", "courses", "evaluations", "ai_optimization", "ai_analytics", "security"]
        },
        {
            "id": 2,
            "name": "teacher",
            "display_name": "教师",
            "description": "教师权限",
            "permissions": ["dashboard", "courses", "evaluations", "ai_optimization", "ai_analytics"]
        },
        {
            "id": 3,
            "name": "student",
            "display_name": "学生",
            "description": "学生权限",
            "permissions": ["dashboard", "courses", "evaluations"]
        }
    ]
    return {"success": True, "data": roles, "message": "获取角色列表成功"}

# 系统设置相关API
@app.get("/api/v1/settings")
async def get_settings():
    """获取系统设置"""
    settings = {
        "general": {
            "system_name": "双语教学与评价平台",
            "max_file_size": 10,
            "session_timeout": 30,
            "language": "zh-CN"
        },
        "notifications": {
            "email_notifications": True,
            "system_notifications": True,
            "evaluation_reminders": True,
            "ai_optimization_notifications": True,
            "security_alerts": True,
            "notification_frequency": "realtime"
        },
        "security": {
            "password_complexity": True,
            "two_factor_auth": False,
            "login_lockout": True,
            "session_management": True,
            "password_min_length": 8,
            "login_fail_lockout_count": 5,
            "lockout_duration": 15
        },
        "ai": {
            "ai_optimization_enabled": True,
            "svd_evaluation_enabled": True,
            "learning_analytics_enabled": True,
            "smart_recommendations_enabled": True,
            "confidence_threshold": 0.8,
            "data_retention_days": 90,
            "auto_optimization_frequency": "weekly"
        }
    }
    return {"success": True, "data": settings, "message": "获取系统设置成功"}

@app.put("/api/v1/settings")
async def update_settings():
    """更新系统设置"""
    return {"success": True, "message": "系统设置更新成功"}

@app.get("/api/v1/system/status")
async def get_system_status():
    """获取系统状态"""
    status = {
        "system_uptime": "5天 12小时 30分钟",
        "cpu_usage": 45.2,
        "memory_usage": 67.8,
        "disk_usage": 23.4,
        "active_users": 156,
        "total_requests": 12450,
        "error_rate": 0.02,
        "ai_models_status": {
            "svd_model": "active",
            "optimization_model": "active",
            "recommendation_model": "active"
        },
        "database_status": "healthy",
        "last_backup": "2024-01-15T02:00:00"
    }
    return {"success": True, "data": status, "message": "获取系统状态成功"}

@app.post("/api/v1/teaching/analyze")
async def analyze_teaching():
    """教学分析"""
    analysis_result = {
        "attendance_rate": round(random.uniform(0.8, 1.0), 2),
        "interaction_frequency": round(random.uniform(0.5, 0.9), 2),
        "student_engagement": round(random.uniform(0.6, 0.95), 2),
        "teaching_score": round(random.uniform(0.7, 0.95), 2),
        "improvement_suggestions": [
            "建议增加课堂互动环节",
            "可以尝试更多小组讨论活动"
        ],
        "timestamp": datetime.now().isoformat()
    }
    return {"success": True, "data": analysis_result, "message": "教学分析完成"}

# 智能推荐API
@app.get("/api/v1/recommendations/teaching")
async def get_teaching_recommendations():
    """获取教学推荐"""
    recommendations = [
        {
            "id": 1,
            "type": "teaching_method",
            "title": "双语教学最佳实践",
            "description": "基于SVD++算法分析，推荐以下双语教学方法",
            "content": [
                "使用TPR（全身反应法）进行词汇教学",
                "采用CLIL（内容与语言整合学习）模式",
                "实施任务型语言教学法",
                "运用多媒体辅助教学"
            ],
            "confidence": 89.5,
            "created_at": "2024-01-15T10:00:00"
        },
        {
            "id": 2,
            "type": "course_design",
            "title": "课程设计优化建议",
            "description": "针对当前课程结构，AI推荐以下优化方案",
            "content": [
                "增加实践环节，提高学生动手能力",
                "优化课程难度梯度，适应不同水平学生",
                "加强双语内容的连贯性",
                "引入真实案例，增强实用性"
            ],
            "confidence": 92.3,
            "created_at": "2024-01-15T09:30:00"
        }
    ]
    return {"success": True, "data": recommendations, "message": "获取教学推荐成功"}

@app.get("/api/v1/recommendations/student")
async def get_student_recommendations():
    """获取学生个性化推荐"""
    recommendations = [
        {
            "id": 1,
            "student_id": 1,
            "type": "learning_path",
            "title": "个性化学习路径",
            "description": "基于学生学习数据，推荐个性化学习路径",
            "content": [
                "建议参加英语角活动，提高口语能力",
                "推荐阅读相关英文文献，扩展专业知识",
                "建议参加国际交流项目，提升跨文化能力",
                "推荐使用在线学习平台，补充课堂内容"
            ],
            "confidence": 87.6,
            "created_at": "2024-01-15T11:00:00"
        }
    ]
    return {"success": True, "data": recommendations, "message": "获取学生推荐成功"}

# 教学质量评估API
@app.get("/api/v1/quality/assessment")
async def get_quality_assessment():
    """获取教学质量评估"""
    assessment = {
        "overall_score": 88.5,
        "dimensions": {
            "content_quality": 90.0,
            "teaching_effectiveness": 87.0,
            "student_satisfaction": 89.0,
            "bilingual_competence": 92.0,
            "interaction_quality": 85.0,
            "assessment_fairness": 88.0
        },
        "strengths": [
            "双语教学能力突出",
            "课程内容丰富实用",
            "学生满意度较高"
        ],
        "improvements": [
            "可以增加更多互动环节",
            "建议优化评价方式",
            "可以加强实践教学"
        ],
        "ai_insights": [
            "基于SVD++算法分析，该教师在双语教学方面表现优秀",
            "学生参与度较高，但仍有提升空间",
            "建议继续保持当前教学优势，同时关注改进建议"
        ]
    }
    return {"success": True, "data": assessment, "message": "获取质量评估成功"}

# 学习分析API
@app.get("/api/v1/analytics/learning")
async def get_learning_analytics():
    """获取学习分析数据"""
    analytics = {
        "student_performance": {
            "average_score": 85.6,
            "score_distribution": {
                "excellent": 25,
                "good": 45,
                "average": 20,
                "below_average": 10
            },
            "improvement_trend": [82, 84, 86, 85, 87, 88]
        },
        "engagement_metrics": {
            "attendance_rate": 92.5,
            "participation_rate": 78.3,
            "homework_completion": 89.7,
            "discussion_activity": 75.2
        },
        "bilingual_progress": {
            "language_proficiency": 83.4,
            "cultural_understanding": 87.1,
            "communication_skills": 81.9,
            "academic_writing": 85.6
        },
        "predictions": {
            "final_score_prediction": 87.2,
            "improvement_potential": 8.5,
            "risk_students": 3,
            "recommendations": [
                "重点关注风险学生，提供额外支持",
                "加强口语训练，提高沟通能力",
                "增加文化背景知识，提升跨文化理解"
            ]
        }
    }
    return {"success": True, "data": analytics, "message": "获取学习分析成功"}

# 教学分析API
@app.get("/api/v1/analytics/teaching")
async def get_teaching_analytics():
    """获取教学分析数据"""
    analytics = {
        "total_courses": 8,
        "total_students": 245,
        "average_score": 87.3,
        "growth_trend": [
            {"month": "1月", "average_score": 82},
            {"month": "2月", "average_score": 84},
            {"month": "3月", "average_score": 86},
            {"month": "4月", "average_score": 85},
            {"month": "5月", "average_score": 87},
            {"month": "6月", "average_score": 89}
        ],
        "course_performance": [
            {
                "course_name": "Python编程基础",
                "student_count": 60,
                "average_score": 92
            },
            {
                "course_name": "大学英语",
                "student_count": 55,
                "average_score": 88
            },
            {
                "course_name": "高等数学",
                "student_count": 70,
                "average_score": 85
            },
            {
                "course_name": "数据结构",
                "student_count": 45,
                "average_score": 90
            },
            {
                "course_name": "计算机网络",
                "student_count": 50,
                "average_score": 87
            }
        ]
    }
    return {"success": True, "data": analytics, "message": "获取教学分析成功"}

@app.get("/api/v1/evaluation/teacher/{teacher_id}")
async def get_teacher_evaluation(teacher_id: int):
    """获取教师评价"""
    evaluation = {
        "teacher_id": teacher_id,
        "overall_score": round(random.uniform(3.5, 5.0), 2),
        "language_ability": round(random.uniform(3.0, 5.0), 2),
        "interaction_effect": round(random.uniform(3.0, 5.0), 2),
        "course_design": round(random.uniform(3.0, 5.0), 2),
        "knowledge_delivery": round(random.uniform(3.0, 5.0), 2),
        "student_engagement": round(random.uniform(3.0, 5.0), 2),
        "teaching_innovation": round(random.uniform(3.0, 5.0), 2),
        "recommendations": [
            "建议增加课堂互动频率",
            "可以尝试更多双语教学技巧",
            "建议定期收集学生反馈"
        ]
    }
    return {"success": True, "data": evaluation, "message": "教师评价获取成功"}

@app.get("/api/v1/courses/my")
async def get_my_courses():
    """获取当前学生的课程列表（模拟数据）"""
    courses = [
        {
            "id": 1,
            "name": "Python编程基础",
            "code": "CS101",
            "subject": "计算机科学",
            "teacher_name": "张老师",
            "credits": 3,
            "description": "学习Python基础语法和编程思维",
            "schedule": "每周一 10:00-12:00",
            "classroom": "A101",
            "enrollment_count": 60,
            "max_enrollment": 80,
            "status": "active"
        },
        {
            "id": 2,
            "name": "大学英语",
            "code": "EN101",
            "subject": "英语",
            "teacher_name": "李老师",
            "credits": 2,
            "description": "提升英语听说读写能力",
            "schedule": "每周三 14:00-16:00",
            "classroom": "B202",
            "enrollment_count": 55,
            "max_enrollment": 60,
            "status": "active"
        },
        {
            "id": 3,
            "name": "高等数学",
            "code": "MA101",
            "subject": "数学",
            "teacher_name": "王老师",
            "credits": 4,
            "description": "微积分基础及应用",
            "schedule": "每周五 8:00-10:00",
            "classroom": "C303",
            "enrollment_count": 70,
            "max_enrollment": 80,
            "status": "inactive"
        }
    ]
    return {"success": True, "data": courses, "message": "获取我的课程成功"}

@app.get("/api/v1/evaluations/my")
async def get_my_evaluations():
    """获取当前学生的评价列表（模拟数据）"""
    evaluations = [
        {
            "id": 1,
            "course_id": 1,
            "course_name": "Python编程基础",
            "teacher_name": "张老师",
            "student_id": 1001,
            "student_name": "李同学",
            "overall_score": 92,
            "teaching_score": 95,
            "content_score": 90,
            "interaction_score": 88,
            "bilingual_score": 93,
            "comments": "老师讲解细致，课堂气氛活跃。",
            "created_at": "2024-06-01 10:30:00"
        },
        {
            "id": 2,
            "course_id": 2,
            "course_name": "大学英语",
            "teacher_name": "李老师",
            "student_id": 1001,
            "student_name": "李同学",
            "overall_score": 85,
            "teaching_score": 87,
            "content_score": 84,
            "interaction_score": 80,
            "bilingual_score": 88,
            "comments": "课程内容丰富，互动较多。",
            "created_at": "2024-06-02 14:00:00"
        }
    ]
    return {"success": True, "data": evaluations, "message": "获取我的评价成功"}

@app.get("/api/v1/courses/{course_id}")
async def get_course_detail(course_id: int = Path(..., description="课程ID")):
    """获取课程详情（模拟数据）"""
    courses = [
        {
            "id": 1,
            "name": "Python编程基础",
            "code": "CS101",
            "subject": "计算机科学",
            "teacher_name": "张老师",
            "credits": 3,
            "description": "学习Python基础语法和编程思维",
            "schedule": "每周一 10:00-12:00",
            "classroom": "A101",
            "enrollment_count": 60,
            "max_enrollment": 80,
            "status": "active"
        },
        {
            "id": 2,
            "name": "大学英语",
            "code": "EN101",
            "subject": "英语",
            "teacher_name": "李老师",
            "credits": 2,
            "description": "提升英语听说读写能力",
            "schedule": "每周三 14:00-16:00",
            "classroom": "B202",
            "enrollment_count": 55,
            "max_enrollment": 60,
            "status": "active"
        },
        {
            "id": 3,
            "name": "高等数学",
            "code": "MA101",
            "subject": "数学",
            "teacher_name": "王老师",
            "credits": 4,
            "description": "微积分基础及应用",
            "schedule": "每周五 8:00-10:00",
            "classroom": "C303",
            "enrollment_count": 70,
            "max_enrollment": 80,
            "status": "inactive"
        }
    ]
    course = next((c for c in courses if c["id"] == course_id), None)
    if course:
        return {"success": True, "data": course, "message": "获取课程详情成功"}
    else:
        return {"success": False, "message": "未找到该课程"}

@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    """全局异常处理"""
    return JSONResponse(
        status_code=500,
        content={"message": f"内部服务器错误: {str(exc)}"}
    )

if __name__ == "__main__":
    uvicorn.run(
        "main_simple:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    ) 