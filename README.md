# Pulse Review Scraper

## Objective
This project is a Python-based script developed as part of the Pulse Coding Assignment.
It scrapes product reviews from G2 for a given company within a specified date range
and outputs the results in a structured JSON format.

---

## Features
- Accepts company name, start date, end date, and source as input
- Scrapes reviews from G2
- Filters reviews based on the provided date range
- Handles pagination automatically
- Outputs clean and structured JSON
- Graceful handling of missing or malformed data

---

## Folder Structure
```text
pulse-review-scraper/
│
├── scraper.py
├── requirements.txt
├── README.md
└── output/
    └── sample_reviews.json
```
---

## Setup Instructions

1. Install Python (version 3.8 or above recommended)
2. Install dependencies:
   pip install -r requirements.txt

---

## Usage

Run the script using the following command:

python scraper.py --company "HubSpot" --start_date 2024-01-01 --end_date 2024-03-31 --source g2

---

## Output
The script generates a JSON file at:

output/sample_reviews.json

Each review contains:
- title
- review text
- date
- rating (if available)

---

## Assumptions
- G2 product review pages are publicly accessible
- Page structure remains mostly consistent
- Only English reviews are processed

---

## Limitations
- Excessive requests may trigger rate limiting
- Only G2 is supported in the current version

---

## Future Enhancements
- Add support for Capterra and other SaaS review platforms
- Introduce retry and caching mechanisms
- Improve robustness against UI changes

---

## Author Notes
This solution focuses on correctness, clarity, and maintainability while meeting all
assignment requirements.

