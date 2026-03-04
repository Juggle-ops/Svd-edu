"""
学生数据模型
"""

from sqlalchemy import Column, String, Integer, Float, JSON, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base import BaseModel

class Student(BaseModel):
    """学生模型"""
    __tablename__ = "students"
    
    # 基本信息
    name = Column(String(100), nullable=False, index=True)
    email = Column(String(100), unique=True, nullable=False, index=True)
    phone = Column(String(20))
    student_id = Column(String(50), unique=True, nullable=False)  # 学号
    
    # 教育背景
    grade = Column(String(20))  # 年级
    major = Column(String(100))  # 专业
    class_name = Column(String(50))  # 班级
    
    # 语言能力
    chinese_level = Column(String(20), default="native")  # 中文水平
    english_level = Column(String(20), default="intermediate")  # 英文水平
    other_languages = Column(JSON)  # 其他语言
    
    # 学习相关
    enrollment_year = Column(Integer)  # 入学年份
    gpa = Column(Float, default=0.0)  # 平均绩点
    
    # 关联关系
    enrollments = relationship("CourseEnrollment", back_populates="student")
    evaluations = relationship("StudentEvaluation", back_populates="student")
    
    def __repr__(self):
        return f"<Student(id={self.id}, name='{self.name}', student_id='{self.student_id}')>"

class CourseEnrollment(BaseModel):
    """课程注册模型"""
    __tablename__ = "course_enrollments"
    
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    course_id = Column(Integer, ForeignKey("courses.id"), nullable=False)
    
    # 注册信息
    enrollment_date = Column(String(20))  # 注册日期
    status = Column(String(20), default="active")  # 状态：active/dropped/completed
    
    # 学习表现
    attendance_rate = Column(Float, default=0.0)  # 出勤率
    participation_score = Column(Float, default=0.0)  # 参与度评分
    final_grade = Column(Float)  # 最终成绩
    
    # 关联关系
    student = relationship("Student", back_populates="enrollments")
    course = relationship("Course", back_populates="enrollments")
    
    def __repr__(self):
        return f"<CourseEnrollment(student_id={self.student_id}, course_id={self.course_id})>"

class StudentEvaluation(BaseModel):
    """学生评价模型"""
    __tablename__ = "student_evaluations"
    
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    course_id = Column(Integer, ForeignKey("courses.id"), nullable=False)
    
    # 评价内容
    course_rating = Column(Float, nullable=False)  # 课程评分
    teacher_rating = Column(Float, nullable=False)  # 教师评分
    difficulty_level = Column(Integer)  # 难度等级
    interest_level = Column(Integer)  # 兴趣等级
    
    # 详细评价
    comments = Column(Text)  # 评价意见
    suggestions = Column(Text)  # 改进建议
    
    # 关联关系
    student = relationship("Student", back_populates="evaluations")
    course = relationship("Course", back_populates="student_evaluations")
    
    def __repr__(self):
        return f"<StudentEvaluation(student_id={self.student_id}, course_id={self.course_id})>" 