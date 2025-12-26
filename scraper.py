import requests
from bs4 import BeautifulSoup
import argparse
import json
from datetime import datetime
from dateutil import parser as date_parser

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def parse_date(date_text):
    try:
        return date_parser.parse(date_text)
    except:
        return None

def scrape_g2(company, start_date, end_date):
    reviews = []
    page = 1

    while True:
        url = f"https://www.g2.com/products/{company.lower().replace(' ', '-')}/reviews?page={page}"
        response = requests.get(url, headers=HEADERS)

        if response.status_code != 200:
            break

        soup = BeautifulSoup(response.text, "html.parser")
        review_blocks = soup.select("div.paper")

        if not review_blocks:
            break

        for block in review_blocks:
            try:
                title = block.select_one("h3").text.strip()
                body = block.select_one("div[itemprop='reviewBody']").text.strip()
                date_text = block.select_one("time")["datetime"]
                review_date = parse_date(date_text)

                if not review_date:
                    continue

                if start_date <= review_date <= end_date:
                    reviews.append({
                        "title": title,
                        "review": body,
                        "date": review_date.strftime("%Y-%m-%d"),
                        "rating": block.select_one("span[itemprop='ratingValue']").text.strip()
                    })
            except:
                continue

        page += 1

    return reviews

def main():
    parser = argparse.ArgumentParser(description="G2 Review Scraper")
    parser.add_argument("--company", required=True)
    parser.add_argument("--start_date", required=True)
    parser.add_argument("--end_date", required=True)
    parser.add_argument("--source", required=True, choices=["g2"])

    args = parser.parse_args()

    start_date = parse_date(args.start_date)
    end_date = parse_date(args.end_date)

    if not start_date or not end_date:
        raise ValueError("Invalid date format. Use YYYY-MM-DD")

    if args.source == "g2":
        reviews = scrape_g2(args.company, start_date, end_date)

    with open("output/sample_reviews.json", "w", encoding="utf-8") as f:
        json.dump(reviews, f, indent=2)

    print(f"Saved {len(reviews)} reviews to output/sample_reviews.json")

if __name__ == "__main__":
    main()
