"""
数据库连接配置
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pymongo import MongoClient
import redis
from influxdb_client import InfluxDBClient
from elasticsearch import Elasticsearch
from app.core.config import settings
import logging

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# PostgreSQL数据库配置
engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True,
    pool_recycle=300,
    pool_size=20,
    max_overflow=30
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# MongoDB配置
mongo_client = MongoClient(settings.MONGODB_URL)
mongo_db = mongo_client.svd_edu

# Redis配置
redis_client = redis.from_url(settings.REDIS_URL, decode_responses=True)

# InfluxDB配置
influx_client = InfluxDBClient(
    url=settings.INFLUXDB_URL,
    token=settings.INFLUXDB_TOKEN,
    org=settings.INFLUXDB_ORG
)
influx_write_api = influx_client.write_api()
influx_query_api = influx_client.query_api()

# Elasticsearch配置
es_client = Elasticsearch([settings.ELASTICSEARCH_URL])

def get_db():
    """获取数据库会话"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_mongo_db():
    """获取MongoDB数据库"""
    return mongo_db

def get_redis_client():
    """获取Redis客户端"""
    return redis_client

def get_influx_client():
    """获取InfluxDB客户端"""
    return influx_client

def get_es_client():
    """获取Elasticsearch客户端"""
    return es_client

def init_db():
    """初始化数据库"""
    try:
        # 创建所有表
        Base.metadata.create_all(bind=engine)
        logger.info("数据库表创建成功")
        
        # 测试连接
        db = SessionLocal()
        db.execute("SELECT 1")
        db.close()
        logger.info("PostgreSQL连接测试成功")
        
        # 测试MongoDB连接
        mongo_db.command('ping')
        logger.info("MongoDB连接测试成功")
        
        # 测试Redis连接
        redis_client.ping()
        logger.info("Redis连接测试成功")
        
        # 测试InfluxDB连接
        influx_client.ping()
        logger.info("InfluxDB连接测试成功")
        
        # 测试Elasticsearch连接
        es_client.ping()
        logger.info("Elasticsearch连接测试成功")
        
    except Exception as e:
        logger.error(f"数据库初始化失败: {e}")
        raise

def close_db():
    """关闭数据库连接"""
    try:
        influx_client.close()
        mongo_client.close()
        logger.info("数据库连接已关闭")
    except Exception as e:
        logger.error(f"关闭数据库连接失败: {e}") 