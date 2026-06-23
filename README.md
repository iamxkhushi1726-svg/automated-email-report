# Automated Email Report Sender

> Project 03/100 — Building a strong GitHub portfolio from scratch.

Reads sales data from CSV, generates a styled HTML report using pandas,
and emails it automatically via Gmail SMTP. Fully configurable via CLI flags.

## Features

- Loads and analyses CSV data with pandas (groupby, aggregation, sorting)
- Generates a styled multi-section HTML report with metrics and tables
- Sends report as HTML email via Gmail SMTP (smtplib + MIMEMultipart)
- Credentials loaded securely from .env using python-dotenv
- CLI flags: --preview (save locally) and --send (email delivery)
- Graceful SMTP error handling with actionable error messages

## Tech Stack

- Python 3.x
- pandas (data loading, aggregation, HTML table generation)
- smtplib + email.mime (email composition and delivery)
- python-dotenv (secure credential management)
- argparse (CLI interface)

## Setup

```bash
git clone https://github.com/iamxkhushi1726-svg/automated-email-report.git
cd automated-email-report
pip install -r requirements.txt
cp .env.example .env
# Edit .env with your Gmail credentials and App Password
```

### Getting a Gmail App Password
1. Go to https://myaccount.google.com/security
2. Enable 2-Step Verification
3. Go to App Passwords
4. Select:
    - App: Mail
    - Device: Other (Python App)
5. Copy the generated password into .env

## Usage

```bash
# Preview report as HTML (no email sent)
python src/main.py --preview

# Send report via email
python src/main.py --send your_email@gmail.com

# Send to a specific address
python src/main.py --send --to someone@gmail.com

# Preview and send
python src/main.py --preview --send your_email@gmail.com
```

## Project Structure

```
automated-email-report/
├── src/
│   ├── main.py              
│   ├── report_generator.py  
│   ├── email_sender.py      
├── data/
│   └── sample_sales.csv     
├── output/
│   └── report.html          
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```
## What This Project Does
- Reads sales dataset from CSV
- Calculates revenue, units sold, top products & regions
- Generates a styled HTML dashboard report
- Optionally emails the report automatically

## What I Learned

- How to aggregate and summarise data with pandas groupby and agg
- How to convert DataFrames to HTML tables with .to_html()
- How to compose and send HTML emails with smtplib and MIMEMultipart
- How to manage secrets securely with python-dotenv and .env files
- Why you never hardcode credentials — and how .gitignore protects you

## Part of 100 Projects Challenge

Project 03 of my 100-project challenge to secure AI/ML and SWE internships.

Follow my progress: [GitHub Profile](https://github.com/iamxkhushi1726-svg)