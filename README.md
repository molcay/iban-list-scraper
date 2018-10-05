# IBAN List Scraper
This scraper is for crawling the data of [IBAN Calculator](https://www.xe.com/ibancalculator/countrylist/) by [xe](https://www.xe.com)

# Usage

* Create `venv` and activate
```bash
python3 -m venv myvenv
source myvenv/bin/activate
```

* Install dependencies:
```
pip install -r requirements.txt
```

* Run crawler
```
scrapy crawl iban -o iban.json
```

> The previous command creates an `iban.json` and `flags` directory.

> * `iban.json` file contains list of IBAN information by countries:
```javascript
{
  "name": "Turkey", // name of the country
  "detail_url": "https://www.xe.com/ibancalculator/sample/?ibancountry=turkey", // IBAN information detail url
  "flag_url": [
    "https://www.xe.com/themes/xe/images/flags/countries/tr.png" // image url for flag of the country
  ],
  "data": { // this key contains IBAN information detail scraped from "detail_url" key
    "IBAN": "TR33 0006 1005 1978 6457 8413 26",
    "ISO Country Code": "TR (Turkey)",
    "IBAN Check Digits": "33",
    "BBAN": " 0006 1005 1978 6457 8413 26",
    "Bank Identifier": "00061",
    "Reserved Field": "0",
    "Account Number": "0519786457841326",
    "SEPA Member": "No"
  },
  "flag": [ // downloaded file details
    {
      "url": "https://www.xe.com/themes/xe/images/flags/countries/tr.png",
      "path": "full/1da3555204e22d2f886248abad3f8400a4ed0c84.jpg",
      "checksum": "6f19b4450fdeaf6b06fb824a5cec0bb4"
    }
  ]
}
```

> * `flags` file contains flag image for every country in `iban.json`
