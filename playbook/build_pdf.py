#!/usr/bin/env python3
"""Build the 5 YOE High-Paying Data Engineer playbook PDF."""
from pathlib import Path
from weasyprint import HTML

ROOT = Path(__file__).resolve().parent
HTML_PATH = ROOT / "playbook.html"
PDF_PATH = ROOT / "High_Paying_Data_Engineer_Playbook_5YOE.pdf"


def main() -> None:
    HTML(filename=str(HTML_PATH), base_url=str(ROOT)).write_pdf(str(PDF_PATH))
    size_kb = PDF_PATH.stat().st_size / 1024
    print(f"Wrote {PDF_PATH} ({size_kb:.1f} KB)")


if __name__ == "__main__":
    main()
