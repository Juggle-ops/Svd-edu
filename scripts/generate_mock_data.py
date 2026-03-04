"""
模拟数据生成脚本
用于生成测试数据
"""

import random
import json
from datetime import datetime, timedelta
from typing import List, Dict, Any

def generate_teachers(n_teachers: int = 20) -> List[Dict[str, Any]]:
    """生成教师数据"""
    teachers = []
    subjects = ["计算机科学", "数学", "英语", "物理", "化学", "生物"]
    universities = ["清华大学", "北京大学", "复旦大学", "上海交通大学", "浙江大学"]
    
    for i in range(1, n_teachers + 1):
        teacher = {
            "id": i,
            "name": f"教师{i}",
            "email": f"teacher{i}@example.com",
            "phone": f"138{random.randint(10000000, 99999999)}",
            "education_level": random.choice(["本科", "硕士", "博士"]),
            "major": random.choice(subjects),
            "university": random.choice(universities),
            "chinese_level": "native",
            "english_level": random.choice(["beginner", "intermediate", "advanced"]),
            "teaching_years": random.randint(1, 20),
            "subjects": random.sample(subjects, random.randint(1, 3)),
            "specializations": random.sample(["人工智能", "机器学习", "深度学习", "数据科学"], random.randint(1, 2)),
            "overall_rating": round(random.uniform(3.0, 5.0), 2),
            "total_evaluations": random.randint(10, 200)
        }
        teachers.append(teacher)
    
    return teachers

def generate_students(n_students: int = 100) -> List[Dict[str, Any]]:
    """生成学生数据"""
    students = []
    majors = ["计算机科学", "数学", "英语", "物理", "化学", "生物", "经济学", "管理学"]
    grades = ["大一", "大二", "大三", "大四"]
    
    for i in range(1, n_students + 1):
        student = {
            "id": i,
            "name": f"学生{i}",
            "student_id": f"2021{i:03d}",
            "email": f"student{i}@example.com",
            "phone": f"139{random.randint(10000000, 99999999)}",
            "grade": random.choice(grades),
            "major": random.choice(majors),
            "class_name": f"{random.choice(majors)}{random.randint(1, 5)}班",
            "chinese_level": "native",
            "english_level": random.choice(["beginner", "intermediate", "advanced"]),
            "enrollment_year": 2021,
            "gpa": round(random.uniform(2.0, 4.0), 2)
        }
        students.append(student)
    
    return students

def generate_courses(n_courses: int = 30) -> List[Dict[str, Any]]:
    """生成课程数据"""
    courses = []
    subjects = ["计算机科学", "数学", "英语", "物理", "化学", "生物"]
    course_names = [
        "Python编程基础", "数据结构与算法", "机器学习", "深度学习", "数据库系统",
        "计算机网络", "操作系统", "软件工程", "高等数学", "线性代数",
        "概率论与数理统计", "英语口语", "英语写作", "英语听力", "英语阅读",
        "大学物理", "有机化学", "生物化学", "细胞生物学", "遗传学"
    ]
    
    for i in range(1, n_courses + 1):
        course = {
            "id": i,
            "name": course_names[i % len(course_names)],
            "code": f"CS{i:03d}",
            "description": f"这是一门关于{course_names[i % len(course_names)]}的双语教学课程",
            "subject": random.choice(subjects),
            "level": random.choice(["beginner", "intermediate", "advanced"]),
            "credits": random.randint(2, 5),
            "duration": random.randint(32, 64),
            "primary_language": "chinese",
            "secondary_language": "english",
            "language_ratio": {"chinese": random.uniform(0.6, 0.8), "english": random.uniform(0.2, 0.4)},
            "max_students": random.randint(30, 80),
            "current_students": random.randint(20, 60),
            "status": "active",
            "overall_rating": round(random.uniform(3.5, 5.0), 2),
            "total_evaluations": random.randint(5, 100),
            "teacher_id": random.randint(1, 20)
        }
        courses.append(course)
    
    return courses

def generate_rating_data(n_ratings: int = 500) -> List[Dict[str, Any]]:
    """生成评分数据"""
    ratings = []
    
    for i in range(n_ratings):
        rating = {
            "teacher_id": random.randint(1, 20),
            "student_id": random.randint(1, 100),
            "rating": random.randint(1, 5),
            "timestamp": (datetime.now() - timedelta(days=random.randint(1, 365))).isoformat()
        }
        ratings.append(rating)
    
    return ratings

def generate_teaching_sessions(n_sessions: int = 200) -> List[Dict[str, Any]]:
    """生成教学会话数据"""
    sessions = []
    
    for i in range(n_sessions):
        session = {
            "id": i + 1,
            "course_id": random.randint(1, 30),
            "teacher_id": random.randint(1, 20),
            "session_date": (datetime.now() - timedelta(days=random.randint(1, 365))).isoformat(),
            "duration": random.randint(45, 120),
            "topic": f"第{random.randint(1, 20)}章内容",
            "attendance_count": random.randint(20, 50),
            "attendance_rate": round(random.uniform(0.7, 1.0), 2),
            "interaction_count": random.randint(5, 25),
            "student_engagement": round(random.uniform(0.5, 0.95), 2),
            "teaching_effect_score": round(random.uniform(0.6, 0.95), 2)
        }
        sessions.append(session)
    
    return sessions

def generate_teacher_evaluations(n_evaluations: int = 300) -> List[Dict[str, Any]]:
    """生成教师评价数据"""
    evaluations = []
    
    for i in range(n_evaluations):
        evaluation = {
            "teacher_id": random.randint(1, 20),
            "evaluator_id": random.randint(1, 100),
            "evaluator_type": random.choice(["student", "peer", "admin"]),
            "language_ability": round(random.uniform(3.0, 5.0), 2),
            "interaction_effect": round(random.uniform(3.0, 5.0), 2),
            "course_design": round(random.uniform(3.0, 5.0), 2),
            "knowledge_delivery": round(random.uniform(3.0, 5.0), 2),
            "student_engagement": round(random.uniform(3.0, 5.0), 2),
            "teaching_innovation": round(random.uniform(3.0, 5.0), 2),
            "overall_score": round(random.uniform(3.0, 5.0), 2),
            "comments": f"这是第{i+1}条评价意见",
            "evaluation_date": (datetime.now() - timedelta(days=random.randint(1, 365))).isoformat()
        }
        evaluations.append(evaluation)
    
    return evaluations

def main():
    """主函数"""
    print("开始生成模拟数据...")
    
    # 生成各种数据
    teachers = generate_teachers(20)
    students = generate_students(100)
    courses = generate_courses(30)
    ratings = generate_rating_data(500)
    sessions = generate_teaching_sessions(200)
    evaluations = generate_teacher_evaluations(300)
    
    # 保存数据到文件
    data = {
        "teachers": teachers,
        "students": students,
        "courses": courses,
        "ratings": ratings,
        "sessions": sessions,
        "evaluations": evaluations,
        "generated_at": datetime.now().isoformat()
    }
    
    with open("mock_data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"模拟数据生成完成！")
    print(f"教师数量: {len(teachers)}")
    print(f"学生数量: {len(students)}")
    print(f"课程数量: {len(courses)}")
    print(f"评分数量: {len(ratings)}")
    print(f"会话数量: {len(sessions)}")
    print(f"评价数量: {len(evaluations)}")
    print(f"数据已保存到 mock_data.json")

if __name__ == "__main__":
    main() 