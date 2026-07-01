import json
from pathlib import Path

REPORT_PATH = Path("/app/report.json")


def load_report():
    """Load and return the generated report."""
    assert REPORT_PATH.exists(), "report.json was not created"

    with REPORT_PATH.open() as f:
        return json.load(f)


def test_report_contains_expected_fields():
    """Report contains the required summary fields."""

    report = load_report()

    assert set(report.keys()) == {
        "total_requests",
        "unique_ips",
        "top_path",
    }


def test_total_requests():
    """Total request count is correct."""

    report = load_report()

    assert report["total_requests"] == 6


def test_unique_ips():
    """Unique client count is correct."""

    report = load_report()

    assert report["unique_ips"] == 3


def test_top_path():
    """Most requested path is correct."""

    report = load_report()

    assert report["top_path"] == "/index.html"