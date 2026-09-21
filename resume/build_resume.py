#!/usr/bin/env python3
from pathlib import Path
from weasyprint import HTML

ROOT = Path(__file__).resolve().parent
HTML_PATH = ROOT / "resume.html"
PDF_PATH = ROOT / "Manish_Pandey_Data_Engineer_Resume.pdf"


def main() -> None:
    HTML(filename=str(HTML_PATH), base_url=str(ROOT)).write_pdf(str(PDF_PATH))
    print(f"Wrote {PDF_PATH} ({PDF_PATH.stat().st_size / 1024:.1f} KB)")


if __name__ == "__main__":
    main()
