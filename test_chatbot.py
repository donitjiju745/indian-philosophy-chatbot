"""
Test Runner for Indian Philosophy Chatbot
Tests 39+ queries across all philosophical traditions
Evaluates answer quality, citations, and confidence scoring
"""

import requests
import json
import time
from typing import Dict, List
from datetime import datetime

API_BASE_URL = "http://localhost:8000"

class TestRunner:
    def __init__(self, test_file: str = "test_queries.json"):
        with open(test_file, 'r') as f:
            self.test_data = json.load(f)
        self.results = {
            "total_tests": 0,
            "passed": 0,
            "failed": 0,
            "results": []
        }
    
    def run_test(self, test_id: str, question: str, tradition: str, expected_coverage: List[str], test_type: str) -> Dict:
        """Run a single test"""
        try:
            start_time = time.time()
            
            response = requests.post(
                f"{API_BASE_URL}/chat",
                json={
                    "question": question,
                    "philosophical_tradition": tradition,
                    "language": "english"
                },
                timeout=10
            )
            
            elapsed_time = time.time() - start_time
            
            if response.status_code != 200:
                return {
                    "test_id": test_id,
                    "question": question,
                    "status": "FAILED",
                    "reason": f"HTTP {response.status_code}",
                    "elapsed_time": elapsed_time
                }
            
            data = response.json()
            
            # Evaluate response quality
            passed = self._evaluate_response(data, expected_coverage)
            
            return {
                "test_id": test_id,
                "question": question,
                "tradition": tradition,
                "test_type": test_type,
                "status": "PASSED" if passed else "PARTIAL",
                "confidence": data.get("confidence_score", 0),
                "citations_count": len(data.get("citations", [])),
                "source": data.get("source", "Unknown"),
                "method": data.get("method", "Unknown"),
                "elapsed_time": elapsed_time,
                "coverage_keywords": self._check_coverage(data["answer"], expected_coverage)
            }
        
        except requests.exceptions.Timeout:
            return {
                "test_id": test_id,
                "question": question,
                "status": "FAILED",
                "reason": "Request timeout",
                "elapsed_time": 10.0
            }
        except Exception as e:
            return {
                "test_id": test_id,
                "question": question,
                "status": "FAILED",
                "reason": str(e),
                "elapsed_time": 0
            }
    
    def _evaluate_response(self, response: Dict, expected_coverage: List[str]) -> bool:
        """Evaluate if response meets quality criteria"""
        checks = [
            len(response.get("answer", "")) > 50,  # Non-trivial answer
            len(response.get("citations", [])) > 0,  # Has citations
            response.get("confidence_score", 0) >= 0.5,  # Reasonable confidence
        ]
        return all(checks)
    
    def _check_coverage(self, answer: str, expected_keywords: List[str]) -> Dict:
        """Check if expected keywords are covered"""
        answer_lower = answer.lower()
        coverage = {}
        
        for keyword in expected_keywords:
            keyword_lower = keyword.lower()
            coverage[keyword] = keyword_lower in answer_lower
        
        return coverage
    
    def run_all_tests(self) -> None:
        """Run all tests from test suite"""
        print("\n" + "="*80)
        print("🕉️  INDIAN PHILOSOPHY CHATBOT - TEST SUITE")
        print("="*80)
        print(f"Start Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        
        test_categories = {
            "Vedanta": self.test_data["test_suite"]["vedanta_tests"],
            "Buddhism": self.test_data["test_suite"]["buddhism_tests"],
            "Yoga": self.test_data["test_suite"]["yoga_tests"],
            "Samkhya": self.test_data["test_suite"]["samkhya_tests"],
            "Nyaya": self.test_data["test_suite"]["nyaya_tests"],
            "Mimamsa": self.test_data["test_suite"]["mimamsa_tests"],
            "Cross-Tradition": self.test_data["test_suite"]["cross_tradition_tests"],
            "Edge Cases": self.test_data["test_suite"]["edge_cases"],
        }
        
        total_passed = 0
        total_failed = 0
        
        for category, tests in test_categories.items():
            print(f"\n📚 {category.upper()} TESTS")
            print("-" * 80)
            
            category_passed = 0
            category_failed = 0
            
            for test in tests:
                result = self.run_test(
                    test["id"],
                    test["question"],
                    test.get("tradition", "general"),
                    test.get("expected_coverage", []),
                    test.get("test_type", "unknown")
                )
                
                self.results["results"].append(result)
                
                status_emoji = "✅" if result["status"] == "PASSED" else "⚠️" if result["status"] == "PARTIAL" else "❌"
                
                print(f"{status_emoji} [{result['test_id']}] {result['question'][:60]}")
                print(f"   Status: {result['status']} | Confidence: {result.get('confidence', 0):.2f} | Time: {result['elapsed_time']:.2f}s")
                
                if result["status"] == "PASSED":
                    category_passed += 1
                    total_passed += 1
                elif result["status"] == "PARTIAL":
                    category_passed += 0.5
                    total_passed += 0.5
                else:
                    category_failed += 1
                    total_failed += 1
            
            print(f"\n{category} Results: {category_passed}/{len(tests)} passed")
        
        self.results["total_tests"] = len(self.results["results"])
        self.results["passed"] = total_passed
        self.results["failed"] = total_failed
        
        self._print_summary()
        self._save_results()
    
    def _print_summary(self) -> None:
        """Print test summary"""
        total = self.results["total_tests"]
        passed = self.results["passed"]
        failed = self.results["failed"]
        success_rate = (passed / total * 100) if total > 0 else 0
        
        print("\n" + "="*80)
        print("📊 TEST SUMMARY")
        print("="*80)
        print(f"Total Tests: {total}")
        print(f"Passed: {passed} ({passed/total*100:.1f}%)" if total > 0 else "N/A")
        print(f"Failed: {failed}")
        print(f"Success Rate: {success_rate:.1f}%")
        print(f"End Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("="*80 + "\n")
    
    def _save_results(self) -> None:
        """Save results to file"""
        filename = f"test_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(filename, 'w') as f:
            json.dump(self.results, f, indent=2)
        print(f"📁 Results saved to: {filename}")


def run_quick_test() -> None:
    """Run a quick test with a few key queries"""
    print("\n🚀 Running Quick Test (5 Essential Queries)\n")
    
    queries = [
        ("What is Atman?", "vedanta"),
        ("What are the Four Noble Truths?", "buddhism"),
        ("What is Samadhi?", "yoga"),
        ("Explain Prakriti and Purusha", "samkhya"),
        ("What are the Pramanas?", "nyaya"),
    ]
    
    for question, tradition in queries:
        try:
            response = requests.post(
                f"{API_BASE_URL}/chat",
                json={
                    "question": question,
                    "philosophical_tradition": tradition
                },
                timeout=10
            )
            
            if response.status_code == 200:
                data = response.json()
                print(f"✅ {question}")
                print(f"   Confidence: {data['confidence_score']:.2f} | Citations: {len(data['citations'])}")
                if data['citations']:
                    print(f"   Source: {data['citations'][0]['source']}")
            else:
                print(f"❌ {question} - Error {response.status_code}")
        
        except Exception as e:
            print(f"❌ {question} - {str(e)}")
        
        time.sleep(0.5)  # Avoid rate limiting


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "quick":
        run_quick_test()
    else:
        # Run full test suite
        runner = TestRunner()
        runner.run_all_tests()