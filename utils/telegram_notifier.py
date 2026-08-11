import os
import xml.etree.ElementTree as ET
from pathlib import Path
import requests

JUNIT_FILE = Path("reports/junit.xml")

def get_test_results():
    """Read test results from JUnit XML report"""
    
    tree = ET.parse(JUNIT_FILE)
    root = tree.getroot()

    if root.tag == "testsuites":
        root = root.find("testsuite")

    total = int(root.attrib.get("tests", 0))
    failures = int(root.attrib.get("failures", 0))
    errors = int(root.attrib.get("errors", 0))
    skipped = int(root.attrib.get("skipped", 0))
    duration = float(root.attrib.get("time", 0))

    failed = failures + errors
    passed = total - failed - skipped

    failed_tests = []

    for testcase in root.iter("testcase"):
        if (
            testcase.find("failure") is not None
            or testcase.find("error") is not None
        ):
            failed_tests.append(
                testcase.attrib.get("name")
            )

    return {
        "total": total,
        "passed": passed,
        "failed": failed,
        "skipped": skipped,
        "duration": duration,
        "failed_tests": failed_tests,
    }

def build_message(results):
    """Build Telegram Test Report message"""

    status = (
        "🔴 FAILED"
        if results["failed"] > 0
        else "🟢 PASSED"
    )

    workflow_url = (
        f'{os.environ["GITHUB_SERVER_URL"]}/'
        f'{os.environ["GITHUB_REPOSITORY"]}/'
        f'actions/runs/{os.environ["GITHUB_RUN_ID"]}'
    )

    allure_url = os.environ["ALLURE_REPORT_URL"]

    message = f"""
<b>📊 Ecommerce Web Automation Test Report</b>

<b>{status}</b>

<b>📝 Test Summary</b>
✅ Passed: {results["passed"]}
❌ Failed: {results["failed"]}
⏭️ Skipped: {results["skipped"]}
📋 Total: {results["total"]}
⏱ Duration: {results["duration"]:.2f}s
"""

    if results["failed_tests"]:
        message += "\n<b>❌ Failed Tests</b>\n"

        for test in results["failed_tests"]:
            message += f"• <code>{test}</code>\n"

    message += f"""
<b>🔗 Report Links</b>
📊 <a href="{allure_url}">View Allure Report</a>
▶️ <a href="{workflow_url}">View Pipeline</a>
"""

    return message

def send_telegram(message):
    """Send message to Telegram"""

    bot_token = os.environ["TELEGRAM_BOT_TOKEN"]
    chat_id = os.environ["TELEGRAM_CHAT_ID"]

    url = (
        f"https://api.telegram.org/"
        f"bot{bot_token}/sendMessage"
    )

    response = requests.post(
        url,
        json={
            "chat_id": chat_id,
            "text": message,
            "parse_mode": "HTML",
            "disable_web_page_preview": True,
        },
        timeout=10,
    )

    response.raise_for_status()

def main():
    results = get_test_results()

    message = build_message(results)

    send_telegram(message)

if __name__ == "__main__":
    main()