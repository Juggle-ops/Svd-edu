"""
教师数据模型
"""

from sqlalchemy import Column, String, Integer, Float, JSON, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base import BaseModel

class Teacher(BaseModel):
    """教师模型"""
    __tablename__ = "teachers"
    
    # 基本信息
    name = Column(String(100), nullable=False, index=True)
    email = Column(String(100), unique=True, nullable=False, index=True)
    phone = Column(String(20))
    
    # 教育背景
    education_level = Column(String(50))  # 学历
    major = Column(String(100))  # 专业
    university = Column(String(100))  # 毕业院校
    
    # 语言能力
    chinese_level = Column(String(20), default="native")  # 中文水平
    english_level = Column(String(20), default="intermediate")  # 英文水平
    other_languages = Column(JSON)  # 其他语言
    
    # 教学经验
    teaching_years = Column(Integer, default=0)  # 教龄
    subjects = Column(JSON)  # 教授科目
    specializations = Column(JSON)  # 专业领域
    
    # 评价相关
    overall_rating = Column(Float, default=0.0)  # 总体评分
    total_evaluations = Column(Integer, default=0)  # 评价总数
    
    # 成长追踪
    growth_path = Column(JSON)  # 成长路径
    training_records = Column(JSON)  # 培训记录
    
    # 关联关系
    courses = relationship("Course", back_populates="teacher")
    evaluations = relationship("TeacherEvaluation", back_populates="teacher")
    
    def __repr__(self):
        return f"<Teacher(id={self.id}, name='{self.name}')>"

class TeacherEvaluation(BaseModel):
    """教师评价模型"""
    __tablename__ = "teacher_evaluations"
    
    teacher_id = Column(Integer, ForeignKey("teachers.id"), nullable=False)
    evaluator_id = Column(Integer, nullable=False)  # 评价者ID
    evaluator_type = Column(String(20))  # 评价者类型：student/peer/admin
    
    # 评价维度
    language_ability = Column(Float)  # 语言能力
    interaction_effect = Column(Float)  # 互动效果
    course_design = Column(Float)  # 课程设计
    knowledge_delivery = Column(Float)  # 知识传授
    student_engagement = Column(Float)  # 学生参与
    teaching_innovation = Column(Float)  # 教学创新
    
    # 总体评价
    overall_score = Column(Float, nullable=False)
    comments = Column(Text)  # 评价意见
    
    # 关联关系
    teacher = relationship("Teacher", back_populates="evaluations")
    
    def __repr__(self):
        return f"<TeacherEvaluation(teacher_id={self.teacher_id}, score={self.overall_score})>"

class TeacherGrowthRecord(BaseModel):
    """教师成长记录模型"""
    __tablename__ = "teacher_growth_records"
    
    teacher_id = Column(Integer, ForeignKey("teachers.id"), nullable=False)
    
    # 成长记录
    record_type = Column(String(50))  # 记录类型：training/achievement/improvement
    title = Column(String(200))  # 标题
    description = Column(Text)  # 描述
    date = Column(String(20))  # 日期
    
    # 相关数据
    data = Column(JSON)  # 相关数据
    
    def __repr__(self):
        return f"<TeacherGrowthRecord(teacher_id={self.teacher_id}, type='{self.record_type}')>" 