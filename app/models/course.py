"""
课程数据模型
"""

from sqlalchemy import Column, String, Integer, Float, JSON, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.models.base import BaseModel

class Course(BaseModel):
    """课程模型"""
    __tablename__ = "courses"
    
    # 基本信息
    name = Column(String(200), nullable=False, index=True)
    code = Column(String(50), unique=True, nullable=False)  # 课程代码
    description = Column(Text)  # 课程描述
    
    # 课程属性
    subject = Column(String(100))  # 学科
    level = Column(String(20))  # 课程级别：beginner/intermediate/advanced
    credits = Column(Integer)  # 学分
    duration = Column(Integer)  # 课程时长（小时）
    
    # 教学语言
    primary_language = Column(String(20), default="chinese")  # 主要语言
    secondary_language = Column(String(20), default="english")  # 次要语言
    language_ratio = Column(JSON)  # 语言使用比例
    
    # 课程设置
    max_students = Column(Integer, default=50)  # 最大学生数
    current_students = Column(Integer, default=0)  # 当前学生数
    status = Column(String(20), default="active")  # 状态：active/inactive/archived
    
    # 评价相关
    overall_rating = Column(Float, default=0.0)  # 总体评分
    total_evaluations = Column(Integer, default=0)  # 评价总数
    
    # 关联关系
    teacher_id = Column(Integer, ForeignKey("teachers.id"), nullable=False)
    teacher = relationship("Teacher", back_populates="courses")
    enrollments = relationship("CourseEnrollment", back_populates="course")
    student_evaluations = relationship("StudentEvaluation", back_populates="course")
    sessions = relationship("TeachingSession", back_populates="course")
    
    def __repr__(self):
        return f"<Course(id={self.id}, name='{self.name}', code='{self.code}')>"

class TeachingSession(BaseModel):
    """教学会话模型"""
    __tablename__ = "teaching_sessions"
    
    course_id = Column(Integer, ForeignKey("courses.id"), nullable=False)
    teacher_id = Column(Integer, ForeignKey("teachers.id"), nullable=False)
    
    # 会话信息
    session_date = Column(DateTime, nullable=False)  # 会话日期
    duration = Column(Integer)  # 持续时间（分钟）
    topic = Column(String(200))  # 主题
    
    # 实时数据
    attendance_count = Column(Integer)  # 出勤人数
    attendance_rate = Column(Float)  # 出勤率
    interaction_count = Column(Integer)  # 互动次数
    student_engagement = Column(Float)  # 学生参与度
    
    # AI分析结果
    video_analysis = Column(JSON)  # 视频分析结果
    audio_analysis = Column(JSON)  # 音频分析结果
    teaching_effect_score = Column(Float)  # 教学效果评分
    
    # 关联关系
    course = relationship("Course", back_populates="sessions")
    teacher = relationship("Teacher")
    
    def __repr__(self):
        return f"<TeachingSession(id={self.id}, course_id={self.course_id}, date='{self.session_date}')>"

class CourseMaterial(BaseModel):
    """课程材料模型"""
    __tablename__ = "course_materials"
    
    course_id = Column(Integer, ForeignKey("courses.id"), nullable=False)
    
    # 材料信息
    title = Column(String(200), nullable=False)
    type = Column(String(50))  # 类型：document/video/audio/image
    file_path = Column(String(500))  # 文件路径
    file_size = Column(Integer)  # 文件大小
    
    # 内容信息
    description = Column(Text)
    tags = Column(JSON)  # 标签
    language = Column(String(20))  # 语言
    
    # 关联关系
    course = relationship("Course")
    
    def __repr__(self):
        return f"<CourseMaterial(id={self.id}, title='{self.title}', type='{self.type}')>" 