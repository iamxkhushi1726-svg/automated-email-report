import argparse
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.report_generator import load_data, build_html_report
from src.email_sender import send_report_email

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATA_FILE = os.path.join(BASE_DIR, "data", "sample_sales.csv")
REPORT_OUTPUT = os.path.join(BASE_DIR, "output", "report.html")

def main():
    parser = argparse.ArgumentParser(
        description="Automated Email Report Sender"
    )
    parser.add_argument(
        "--preview",
        action="store_true",
        help="Generate HTML report only"
    )
    parser.add_argument(
        "--send",
        type=str,
        help="Send report to this email address"
    )
    args = parser.parse_args()

    print("\n  Loading data...")
    df = load_data(DATA_FILE)
    print(f"  Loaded {len(df)} rows from {DATA_FILE}")

    print("  Building HTML report...")

    os.makedirs(os.path.dirname(REPORT_OUTPUT), exist_ok=True)
    
    html = build_html_report(df, output_path=REPORT_OUTPUT)

    if args.preview:
        print(f"\n  Preview saved to: {REPORT_OUTPUT}")
        
    if args.send:
        print(f"\n  Sending report to: {args.send}")
        send_report_email(html, recipient_email=args.send)
            
    if not args.preview and not args.send:
        print("\n  Usage:")
        print("    python src/main.py --preview")
        print("    python src/main.py --send")
        print("    python src/main.py --preview --send")

if __name__ == "__main__":
    main()