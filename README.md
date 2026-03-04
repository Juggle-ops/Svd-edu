# Bilingual Teaching Model and Quality Evaluation System

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Project Overview
An integrated platform built on AI technology to optimize bilingual teaching processes and teaching quality evaluation, supporting teacher growth tracking, international exchange security management, and data-driven teaching decision-making.

## Authors & Maintainers

* **Zhai Slim**
* **Xie Zhaoxian**


## Tech Stack

### Backend
- **Main Framework**: FastAPI (Python 3.10+)
- **AI/ML Frameworks**: TensorFlow 2.x, PyTorch, scikit-learn, OpenCV
- **Data Processing**: Pandas, NumPy, Dask
- **Message Queue**: Apache Kafka
- **Cache**: Redis
- **Databases**: PostgreSQL, MongoDB, InfluxDB, Elasticsearch

## Core Features
1. **Bilingual Teaching Optimization Module**: Real-time classroom analysis, teaching effect prediction
2. **SVD++ Teaching Evaluation Mechanism**: Personalized teacher evaluation, hexagonal radar chart visualization
3. **AI Testing & Evaluation Mechanism**: Automated testing based on TDD
4. **Teacher Growth Tracking Module**: Growth path analysis, personalized improvement suggestions
5. **International Exchange Security Management**: Content filtering, security detection
6. **Admin Platform Integration**: Unified data management, integrated AI interfaces

## Quick Start

```bash
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
