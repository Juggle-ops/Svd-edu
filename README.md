Bilingual Teaching Model and Quality Evaluation System

Project Overview
An integrated platform built on AI technology to optimize bilingual teaching processes and teaching quality evaluation, supporting teacher growth tracking, international exchange security management, and data-driven teaching decision-making.
Tech Stack
Backend
Main Framework: FastAPI (Python 3.10+)
AI/ML Frameworks: TensorFlow 2.x, PyTorch, scikit-learn, OpenCV
Data Processing: Pandas, NumPy, Dask
Message Queue: Apache Kafka
Cache: Redis
Databases: PostgreSQL, MongoDB, InfluxDB, Elasticsearch
Core Features
Bilingual Teaching Optimization Module: Real-time classroom analysis, teaching effect prediction
SVD++ Teaching Evaluation Mechanism: Personalized teacher evaluation, hexagonal radar chart visualization
AI Testing & Evaluation Mechanism: Automated testing based on TDD
Teacher Growth Tracking Module: Growth path analysis, personalized improvement suggestions
International Exchange Security Management: Content filtering, security detection
Admin Platform Integration: Unified data management, integrated AI interfaces
Quick Start
bash
运行
# Go to the backend directory
cd backend

# Create a virtual environment (optional)
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# OR
.venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Start development server
python main_simple.py
System Architecture
The system currently focuses on an admin panel for administrators to manage and monitor bilingual teaching comprehensively.Future extensions can include student portals, teacher dashboards, and other user interfaces.
License
MIT License
