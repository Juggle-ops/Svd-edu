"""
应用配置模块
"""

from pydantic_settings import BaseSettings
from typing import Optional, List
import os

class Settings(BaseSettings):
    """应用配置类"""
    
    # 应用基础配置
    APP_NAME: str = "双语教学模式与质量评价机制系统"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = True
    
    # 数据库配置
    DATABASE_URL: str = "postgresql://user:password@localhost:5432/svd_edu"
    MONGODB_URL: str = "mongodb://localhost:27017/svd_edu"
    REDIS_URL: str = "redis://localhost:6379/0"
    INFLUXDB_URL: str = "http://localhost:8086"
    INFLUXDB_TOKEN: str = "your-token"
    INFLUXDB_ORG: str = "svd-edu"
    INFLUXDB_BUCKET: str = "teaching_data"
    
    # Elasticsearch配置
    ELASTICSEARCH_URL: str = "http://localhost:9200"
    
    # Kafka配置
    KAFKA_BOOTSTRAP_SERVERS: str = "localhost:9092"
    KAFKA_TOPIC_TEACHING_DATA: str = "teaching-data"
    KAFKA_TOPIC_EVALUATION: str = "evaluation-data"
    
    # AI模型配置
    MODEL_PATH: str = "./models"
    YOLO_MODEL_PATH: str = "./models/yolov8n.pt"
    SVD_MODEL_PATH: str = "./models/svd_model.pkl"
    
    # 文件上传配置
    UPLOAD_DIR: str = "./uploads"
    MAX_FILE_SIZE: int = 100 * 1024 * 1024  # 100MB
    
    # 安全配置
    SECRET_KEY: str = "your-secret-key-here"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # 跨域配置
    CORS_ORIGINS: List[str] = ["http://localhost:3000", "http://localhost:8080"]
    
    # 日志配置
    LOG_LEVEL: str = "INFO"
    LOG_FILE: str = "./logs/app.log"
    
    # 缓存配置
    CACHE_TTL: int = 3600  # 1小时
    
    # 评价配置
    EVALUATION_THRESHOLD: float = 0.7
    MIN_RATINGS_FOR_EVALUATION: int = 5
    
    class Config:
        env_file = ".env"
        case_sensitive = True

# 创建全局配置实例
settings = Settings()

# 确保必要的目录存在
os.makedirs(settings.UPLOAD_DIR, exist_ok=True)
os.makedirs(settings.MODEL_PATH, exist_ok=True)
os.makedirs(os.path.dirname(settings.LOG_FILE), exist_ok=True) 