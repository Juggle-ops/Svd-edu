#!/usr/bin/env python3
"""
系统测试脚本
测试主要API接口的功能
"""

import requests
import json
import time
from typing import Dict, Any

class SystemTester:
    def __init__(self, base_url: str = "http://localhost:8000"):
        self.base_url = base_url
        self.session = requests.Session()
        self.test_results = []

    def log_test(self, test_name: str, success: bool, message: str = "", data: Any = None):
        """记录测试结果"""
        result = {
            "test_name": test_name,
            "success": success,
            "message": message,
            "data": data,
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }
        self.test_results.append(result)
        
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"{status} {test_name}: {message}")

    def test_health_check(self):
        """测试健康检查"""
        try:
            response = self.session.get(f"{self.base_url}/health")
            if response.status_code == 200:
                data = response.json()
                self.log_test("健康检查", True, "系统运行正常", data)
            else:
                self.log_test("健康检查", False, f"状态码: {response.status_code}")
        except Exception as e:
            self.log_test("健康检查", False, f"请求失败: {str(e)}")

    def test_dashboard_stats(self):
        """测试仪表板统计"""
        try:
            response = self.session.get(f"{self.base_url}/api/v1/dashboard/stats")
            if response.status_code == 200:
                data = response.json()
                if data.get("success"):
                    self.log_test("仪表板统计", True, "获取统计数据成功", data["data"])
                else:
                    self.log_test("仪表板统计", False, data.get("message", "未知错误"))
            else:
                self.log_test("仪表板统计", False, f"状态码: {response.status_code}")
        except Exception as e:
            self.log_test("仪表板统计", False, f"请求失败: {str(e)}")

    def test_teachers_api(self):
        """测试教师API"""
        try:
            response = self.session.get(f"{self.base_url}/api/v1/teachers")
            if response.status_code == 200:
                data = response.json()
                if data.get("success"):
                    self.log_test("教师API", True, f"获取到 {len(data['data'])} 个教师", data["data"])
                else:
                    self.log_test("教师API", False, data.get("message", "未知错误"))
            else:
                self.log_test("教师API", False, f"状态码: {response.status_code}")
        except Exception as e:
            self.log_test("教师API", False, f"请求失败: {str(e)}")

    def test_students_api(self):
        """测试学生API"""
        try:
            response = self.session.get(f"{self.base_url}/api/v1/students")
            if response.status_code == 200:
                data = response.json()
                if data.get("success"):
                    self.log_test("学生API", True, f"获取到 {len(data['data'])} 个学生", data["data"])
                else:
                    self.log_test("学生API", False, data.get("message", "未知错误"))
            else:
                self.log_test("学生API", False, f"状态码: {response.status_code}")
        except Exception as e:
            self.log_test("学生API", False, f"请求失败: {str(e)}")

    def test_courses_api(self):
        """测试课程API"""
        try:
            response = self.session.get(f"{self.base_url}/api/v1/courses")
            if response.status_code == 200:
                data = response.json()
                if data.get("success"):
                    self.log_test("课程API", True, f"获取到 {len(data['data'])} 个课程", data["data"])
                else:
                    self.log_test("课程API", False, data.get("message", "未知错误"))
            else:
                self.log_test("课程API", False, f"状态码: {response.status_code}")
        except Exception as e:
            self.log_test("课程API", False, f"请求失败: {str(e)}")

    def test_auth_login(self):
        """测试登录API"""
        try:
            # 测试管理员登录
            login_data = {"username": "admin", "password": "admin123"}
            response = self.session.post(f"{self.base_url}/api/v1/auth/login", json=login_data)
            if response.status_code == 200:
                data = response.json()
                if data.get("success"):
                    self.log_test("登录API", True, "管理员登录成功", data["data"])
                    # 保存token用于后续测试
                    self.session.headers.update({
                        "Authorization": f"Bearer {data['data']['token']}"
                    })
                else:
                    self.log_test("登录API", False, data.get("message", "未知错误"))
            else:
                self.log_test("登录API", False, f"状态码: {response.status_code}")
        except Exception as e:
            self.log_test("登录API", False, f"请求失败: {str(e)}")

    def test_ai_optimization(self):
        """测试AI优化API"""
        try:
            response = self.session.post(f"{self.base_url}/api/v1/ai-optimization")
            if response.status_code == 200:
                data = response.json()
                if data.get("success"):
                    self.log_test("AI优化API", True, "AI优化建议生成成功", data["data"])
                else:
                    self.log_test("AI优化API", False, data.get("message", "未知错误"))
            else:
                self.log_test("AI优化API", False, f"状态码: {response.status_code}")
        except Exception as e:
            self.log_test("AI优化API", False, f"请求失败: {str(e)}")

    def test_svd_evaluations(self):
        """测试SVD++评价API"""
        try:
            response = self.session.get(f"{self.base_url}/api/v1/evaluations/svd")
            if response.status_code == 200:
                data = response.json()
                if data.get("success"):
                    self.log_test("SVD++评价API", True, f"获取到 {len(data['data'])} 个评价", data["data"])
                else:
                    self.log_test("SVD++评价API", False, data.get("message", "未知错误"))
            else:
                self.log_test("SVD++评价API", False, f"状态码: {response.status_code}")
        except Exception as e:
            self.log_test("SVD++评价API", False, f"请求失败: {str(e)}")

    def test_quality_assessment(self):
        """测试教学质量评估API"""
        try:
            response = self.session.get(f"{self.base_url}/api/v1/quality/assessment")
            if response.status_code == 200:
                data = response.json()
                if data.get("success"):
                    self.log_test("教学质量评估API", True, "获取质量评估成功", data["data"])
                else:
                    self.log_test("教学质量评估API", False, data.get("message", "未知错误"))
            else:
                self.log_test("教学质量评估API", False, f"状态码: {response.status_code}")
        except Exception as e:
            self.log_test("教学质量评估API", False, f"请求失败: {str(e)}")

    def test_system_status(self):
        """测试系统状态API"""
        try:
            response = self.session.get(f"{self.base_url}/api/v1/system/status")
            if response.status_code == 200:
                data = response.json()
                if data.get("success"):
                    self.log_test("系统状态API", True, "获取系统状态成功", data["data"])
                else:
                    self.log_test("系统状态API", False, data.get("message", "未知错误"))
            else:
                self.log_test("系统状态API", False, f"状态码: {response.status_code}")
        except Exception as e:
            self.log_test("系统状态API", False, f"请求失败: {str(e)}")

    def run_all_tests(self):
        """运行所有测试"""
        print("🚀 开始系统测试...")
        print("=" * 50)
        
        # 基础功能测试
        self.test_health_check()
        self.test_dashboard_stats()
        self.test_teachers_api()
        self.test_students_api()
        self.test_courses_api()
        
        # 认证测试
        self.test_auth_login()
        
        # AI功能测试
        self.test_ai_optimization()
        self.test_svd_evaluations()
        self.test_quality_assessment()
        
        # 系统功能测试
        self.test_system_status()
        
        # 输出测试总结
        print("=" * 50)
        self.print_summary()

    def print_summary(self):
        """打印测试总结"""
        total_tests = len(self.test_results)
        passed_tests = sum(1 for result in self.test_results if result["success"])
        failed_tests = total_tests - passed_tests
        
        print(f"\n📊 测试总结:")
        print(f"总测试数: {total_tests}")
        print(f"通过: {passed_tests}")
        print(f"失败: {failed_tests}")
        print(f"成功率: {(passed_tests/total_tests*100):.1f}%")
        
        if failed_tests > 0:
            print(f"\n❌ 失败的测试:")
            for result in self.test_results:
                if not result["success"]:
                    print(f"  - {result['test_name']}: {result['message']}")
        
        # 保存测试结果到文件
        with open("test_results.json", "w", encoding="utf-8") as f:
            json.dump(self.test_results, f, ensure_ascii=False, indent=2)
        print(f"\n💾 测试结果已保存到 test_results.json")

if __name__ == "__main__":
    tester = SystemTester()
    tester.run_all_tests() 