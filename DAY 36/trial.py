import requests

from main import TWILIO_SID, TWILIO_AUTH_TOKEN

stock_data = {
    "Meta Data": {
        "1. Information": "Daily Prices (open, high, low, close) and Volumes",
        "2. Symbol": "TSLA",
        "3. Last Refreshed": "2024-09-20",
        "4. Output Size": "Compact",
        "5. Time Zone": "US/Eastern"
    },
    "Time Series (Daily)": {
        "2024-09-20": {
            "1. open": "241.5200",
            "2. high": "243.9900",
            "3. low": "235.9200",
            "4. close": "238.2500",
            "5. volume": "99879070"
        },
        "2024-09-19": {
            "1. open": "234.0000",
            "2. high": "244.2400",
            "3. low": "232.1300",
            "4. close": "243.9200",
            "5. volume": "102694576"
        },
        "2024-09-18": {
            "1. open": "230.0900",
            "2. high": "235.6800",
            "3. low": "226.8800",
            "4. close": "227.2000",
            "5. volume": "78010204"
        },
        "2024-09-17": {
            "1. open": "229.4500",
            "2. high": "234.5700",
            "3. low": "226.5533",
            "4. close": "227.8700",
            "5. volume": "66761636"
        },
        "2024-09-16": {
            "1. open": "229.3000",
            "2. high": "229.9600",
            "3. low": "223.5300",
            "4. close": "226.7800",
            "5. volume": "54322995"
        },
        "2024-09-13": {
            "1. open": "228.0000",
            "2. high": "232.6700",
            "3. low": "226.3200",
            "4. close": "230.2900",
            "5. volume": "59515114"
        },
        "2024-09-12": {
            "1. open": "224.6600",
            "2. high": "231.4500",
            "3. low": "223.8300",
            "4. close": "229.8100",
            "5. volume": "72020042"
        },
        "2024-09-11": {
            "1. open": "224.5500",
            "2. high": "228.4700",
            "3. low": "216.8003",
            "4. close": "228.1300",
            "5. volume": "83548633"
        },
        "2024-09-10": {
            "1. open": "220.0700",
            "2. high": "226.4000",
            "3. low": "218.6377",
            "4. close": "226.1700",
            "5. volume": "78891136"
        },
        "2024-09-09": {
            "1. open": "216.2000",
            "2. high": "219.8700",
            "3. low": "213.6700",
            "4. close": "216.2700",
            "5. volume": "67443518"
        },
        "2024-09-06": {
            "1. open": "232.6000",
            "2. high": "233.6000",
            "3. low": "210.5100",
            "4. close": "210.7300",
            "5. volume": "112177004"
        },
        "2024-09-05": {
            "1. open": "223.4900",
            "2. high": "235.0000",
            "3. low": "222.2500",
            "4. close": "230.1700",
            "5. volume": "119355013"
        },
        "2024-09-04": {
            "1. open": "210.5900",
            "2. high": "222.2200",
            "3. low": "210.5700",
            "4. close": "219.4100",
            "5. volume": "80217329"
        },
        "2024-09-03": {
            "1. open": "215.2600",
            "2. high": "219.9043",
            "3. low": "209.6400",
            "4. close": "210.6000",
            "5. volume": "76714222"
        },
        "2024-08-30": {
            "1. open": "208.6300",
            "2. high": "214.5701",
            "3. low": "207.0300",
            "4. close": "214.1100",
            "5. volume": "63370608"
        },
        "2024-08-29": {
            "1. open": "209.8000",
            "2. high": "214.8900",
            "3. low": "205.9700",
            "4. close": "206.2800",
            "5. volume": "62308818"
        },
        "2024-08-28": {
            "1. open": "209.7200",
            "2. high": "211.8400",
            "3. low": "202.5900",
            "4. close": "205.7500",
            "5. volume": "64116350"
        },
        "2024-08-27": {
            "1. open": "213.2500",
            "2. high": "215.6600",
            "3. low": "206.9400",
            "4. close": "209.2100",
            "5. volume": "62821390"
        },
        "2024-08-26": {
            "1. open": "218.7500",
            "2. high": "219.0900",
            "3. low": "211.0100",
            "4. close": "213.2100",
            "5. volume": "59301187"
        },
        "2024-08-23": {
            "1. open": "214.4550",
            "2. high": "221.4800",
            "3. low": "214.2100",
            "4. close": "220.3200",
            "5. volume": "81525207"
        },
        "2024-08-22": {
            "1. open": "223.8200",
            "2. high": "224.8000",
            "3. low": "210.3200",
            "4. close": "210.6600",
            "5. volume": "79514482"
        },
        "2024-08-21": {
            "1. open": "222.6700",
            "2. high": "224.6594",
            "3. low": "218.8600",
            "4. close": "223.2700",
            "5. volume": "70145964"
        },
        "2024-08-20": {
            "1. open": "224.8800",
            "2. high": "228.2200",
            "3. low": "219.5600",
            "4. close": "221.1000",
            "5. volume": "74001182"
        },
        "2024-08-19": {
            "1. open": "217.0700",
            "2. high": "222.9800",
            "3. low": "214.0900",
            "4. close": "222.7200",
            "5. volume": "76435222"
        },
        "2024-08-16": {
            "1. open": "211.1500",
            "2. high": "219.8000",
            "3. low": "210.8000",
            "4. close": "216.1200",
            "5. volume": "88765122"
        },
        "2024-08-15": {
            "1. open": "205.0200",
            "2. high": "215.8800",
            "3. low": "204.8200",
            "4. close": "214.1400",
            "5. volume": "89848530"
        },
        "2024-08-14": {
            "1. open": "207.3900",
            "2. high": "208.4400",
            "3. low": "198.7500",
            "4. close": "201.3800",
            "5. volume": "70250014"
        },
        "2024-08-13": {
            "1. open": "198.4700",
            "2. high": "208.4900",
            "3. low": "197.0600",
            "4. close": "207.8300",
            "5. volume": "76247387"
        },
        "2024-08-12": {
            "1. open": "199.0200",
            "2. high": "199.2600",
            "3. low": "194.6700",
            "4. close": "197.4900",
            "5. volume": "64044903"
        },
        "2024-08-09": {
            "1. open": "197.0500",
            "2. high": "200.8800",
            "3. low": "195.1100",
            "4. close": "200.0000",
            "5. volume": "58648274"
        },
        "2024-08-08": {
            "1. open": "195.7000",
            "2. high": "200.7000",
            "3. low": "192.0400",
            "4. close": "198.8400",
            "5. volume": "65033874"
        },
        "2024-08-07": {
            "1. open": "200.7700",
            "2. high": "203.4900",
            "3. low": "191.4800",
            "4. close": "191.7600",
            "5. volume": "71159778"
        },
        "2024-08-06": {
            "1. open": "200.7500",
            "2. high": "202.9000",
            "3. low": "192.6700",
            "4. close": "200.6400",
            "5. volume": "73783942"
        },
        "2024-08-05": {
            "1. open": "185.2200",
            "2. high": "203.8799",
            "3. low": "182.0000",
            "4. close": "198.8800",
            "5. volume": "100308836"
        },
        "2024-08-02": {
            "1. open": "214.8800",
            "2. high": "216.1300",
            "3. low": "205.7800",
            "4. close": "207.6700",
            "5. volume": "82880120"
        },
        "2024-08-01": {
            "1. open": "227.6900",
            "2. high": "231.8670",
            "3. low": "214.3328",
            "4. close": "216.8600",
            "5. volume": "83861898"
        },
        "2024-07-31": {
            "1. open": "227.9000",
            "2. high": "234.6800",
            "3. low": "226.7875",
            "4. close": "232.0700",
            "5. volume": "67497011"
        },
        "2024-07-30": {
            "1. open": "232.2500",
            "2. high": "232.4100",
            "3. low": "220.0000",
            "4. close": "222.6200",
            "5. volume": "100560334"
        },
        "2024-07-29": {
            "1. open": "224.9000",
            "2. high": "234.2700",
            "3. low": "224.7000",
            "4. close": "232.1000",
            "5. volume": "129201789"
        },
        "2024-07-26": {
            "1. open": "221.1900",
            "2. high": "222.2799",
            "3. low": "215.3300",
            "4. close": "219.8000",
            "5. volume": "94604145"
        },
        "2024-07-25": {
            "1. open": "216.8000",
            "2. high": "226.0000",
            "3. low": "216.2310",
            "4. close": "220.2500",
            "5. volume": "100636466"
        },
        "2024-07-24": {
            "1. open": "225.4200",
            "2. high": "225.9900",
            "3. low": "214.7100",
            "4. close": "215.9900",
            "5. volume": "167942939"
        },
        "2024-07-23": {
            "1. open": "253.6000",
            "2. high": "255.7594",
            "3. low": "245.6300",
            "4. close": "246.3800",
            "5. volume": "111928192"
        },
        "2024-07-22": {
            "1. open": "244.2100",
            "2. high": "253.2100",
            "3. low": "243.7500",
            "4. close": "251.5100",
            "5. volume": "101225430"
        },
        "2024-07-19": {
            "1. open": "247.7900",
            "2. high": "249.4400",
            "3. low": "236.8300",
            "4. close": "239.2000",
            "5. volume": "87403903"
        },
        "2024-07-18": {
            "1. open": "251.0900",
            "2. high": "257.1400",
            "3. low": "247.2000",
            "4. close": "249.2300",
            "5. volume": "110869037"
        },
        "2024-07-17": {
            "1. open": "252.7300",
            "2. high": "258.4700",
            "3. low": "246.1820",
            "4. close": "248.5000",
            "5. volume": "115584810"
        },
        "2024-07-16": {
            "1. open": "255.3100",
            "2. high": "258.6200",
            "3. low": "245.8001",
            "4. close": "256.5600",
            "5. volume": "126332470"
        },
        "2024-07-15": {
            "1. open": "255.9700",
            "2. high": "265.6000",
            "3. low": "251.7300",
            "4. close": "252.6400",
            "5. volume": "146912920"
        },
        "2024-07-12": {
            "1. open": "235.8000",
            "2. high": "251.8400",
            "3. low": "233.0912",
            "4. close": "248.2300",
            "5. volume": "155955773"
        },
        "2024-07-11": {
            "1. open": "263.3000",
            "2. high": "271.0000",
            "3. low": "239.6500",
            "4. close": "241.0300",
            "5. volume": "221707273"
        },
        "2024-07-10": {
            "1. open": "262.8000",
            "2. high": "267.5900",
            "3. low": "257.8600",
            "4. close": "263.2600",
            "5. volume": "128519430"
        },
        "2024-07-09": {
            "1. open": "251.0000",
            "2. high": "265.6100",
            "3. low": "250.3000",
            "4. close": "262.3300",
            "5. volume": "160742516"
        },
        "2024-07-08": {
            "1. open": "247.7100",
            "2. high": "259.4390",
            "3. low": "244.5700",
            "4. close": "252.9400",
            "5. volume": "157219580"
        },
        "2024-07-05": {
            "1. open": "249.8100",
            "2. high": "252.3700",
            "3. low": "242.4601",
            "4. close": "251.5200",
            "5. volume": "154501152"
        },
        "2024-07-03": {
            "1. open": "234.5600",
            "2. high": "248.3500",
            "3. low": "234.2500",
            "4. close": "246.3900",
            "5. volume": "166561471"
        },
        "2024-07-02": {
            "1. open": "218.8900",
            "2. high": "231.3000",
            "3. low": "218.0600",
            "4. close": "231.2600",
            "5. volume": "205047920"
        },
        "2024-07-01": {
            "1. open": "201.0200",
            "2. high": "213.2300",
            "3. low": "200.8500",
            "4. close": "209.8600",
            "5. volume": "135691395"
        },
        "2024-06-28": {
            "1. open": "199.5500",
            "2. high": "203.2000",
            "3. low": "195.2600",
            "4. close": "197.8800",
            "5. volume": "95438068"
        },
        "2024-06-27": {
            "1. open": "195.1700",
            "2. high": "198.7200",
            "3. low": "194.0500",
            "4. close": "197.4200",
            "5. volume": "72746521"
        },
        "2024-06-26": {
            "1. open": "186.5400",
            "2. high": "197.7550",
            "3. low": "186.3600",
            "4. close": "196.3700",
            "5. volume": "95737066"
        },
        "2024-06-25": {
            "1. open": "184.4000",
            "2. high": "187.9700",
            "3. low": "182.0100",
            "4. close": "187.3500",
            "5. volume": "63678265"
        },
        "2024-06-24": {
            "1. open": "184.9700",
            "2. high": "188.8000",
            "3. low": "182.5500",
            "4. close": "182.5800",
            "5. volume": "61992070"
        },
        "2024-06-21": {
            "1. open": "182.3000",
            "2. high": "183.9500",
            "3. low": "180.6900",
            "4. close": "183.0100",
            "5. volume": "63029482"
        },
        "2024-06-20": {
            "1. open": "184.6800",
            "2. high": "185.2100",
            "3. low": "179.6600",
            "4. close": "181.5700",
            "5. volume": "55893139"
        },
        "2024-06-18": {
            "1. open": "186.5600",
            "2. high": "187.2000",
            "3. low": "182.3700",
            "4. close": "184.8600",
            "5. volume": "68982265"
        },
        "2024-06-17": {
            "1. open": "177.9200",
            "2. high": "188.8100",
            "3. low": "177.0000",
            "4. close": "187.4400",
            "5. volume": "109786083"
        },
        "2024-06-14": {
            "1. open": "185.8000",
            "2. high": "186.0000",
            "3. low": "176.9200",
            "4. close": "178.0100",
            "5. volume": "82038194"
        },
        "2024-06-13": {
            "1. open": "188.3900",
            "2. high": "191.0800",
            "3. low": "181.2300",
            "4. close": "182.4700",
            "5. volume": "118984122"
        },
        "2024-06-12": {
            "1. open": "171.1200",
            "2. high": "180.5500",
            "3. low": "169.8000",
            "4. close": "177.2900",
            "5. volume": "90389446"
        },
        "2024-06-11": {
            "1. open": "173.9200",
            "2. high": "174.7500",
            "3. low": "167.4100",
            "4. close": "170.6600",
            "5. volume": "64761928"
        },
        "2024-06-10": {
            "1. open": "176.0600",
            "2. high": "178.5700",
            "3. low": "173.1700",
            "4. close": "173.7900",
            "5. volume": "50869682"
        },
        "2024-06-07": {
            "1. open": "176.1300",
            "2. high": "179.3500",
            "3. low": "175.5800",
            "4. close": "177.4800",
            "5. volume": "56244932"
        },
        "2024-06-06": {
            "1. open": "174.6000",
            "2. high": "179.7300",
            "3. low": "172.7300",
            "4. close": "177.9400",
            "5. volume": "69887024"
        },
        "2024-06-05": {
            "1. open": "175.3500",
            "2. high": "176.1500",
            "3. low": "172.1300",
            "4. close": "175.0000",
            "5. volume": "57953756"
        },
        "2024-06-04": {
            "1. open": "174.7750",
            "2. high": "177.7550",
            "3. low": "174.0000",
            "4. close": "174.7700",
            "5. volume": "60056340"
        },
        "2024-06-03": {
            "1. open": "178.1300",
            "2. high": "182.6389",
            "3. low": "174.4900",
            "4. close": "176.2900",
            "5. volume": "68568920"
        },
        "2024-05-31": {
            "1. open": "178.5000",
            "2. high": "180.3200",
            "3. low": "173.8200",
            "4. close": "178.0800",
            "5. volume": "67314602"
        },
        "2024-05-30": {
            "1. open": "178.5750",
            "2. high": "182.6700",
            "3. low": "175.3800",
            "4. close": "178.7900",
            "5. volume": "77784755"
        },
        "2024-05-29": {
            "1. open": "174.1900",
            "2. high": "178.1500",
            "3. low": "173.9300",
            "4. close": "176.1900",
            "5. volume": "54782649"
        },
        "2024-05-28": {
            "1. open": "176.4000",
            "2. high": "178.2500",
            "3. low": "173.1600",
            "4. close": "176.7500",
            "5. volume": "59736620"
        },
        "2024-05-24": {
            "1. open": "174.8350",
            "2. high": "180.0800",
            "3. low": "173.7300",
            "4. close": "179.2400",
            "5. volume": "65584478"
        },
        "2024-05-23": {
            "1. open": "181.8000",
            "2. high": "181.9000",
            "3. low": "173.2600",
            "4. close": "173.7400",
            "5. volume": "71975496"
        },
        "2024-05-22": {
            "1. open": "182.8500",
            "2. high": "183.8000",
            "3. low": "178.1200",
            "4. close": "180.1100",
            "5. volume": "88313477"
        },
        "2024-05-21": {
            "1. open": "175.5100",
            "2. high": "186.8750",
            "3. low": "174.7100",
            "4. close": "186.6000",
            "5. volume": "115266512"
        },
        "2024-05-20": {
            "1. open": "177.5600",
            "2. high": "177.7540",
            "3. low": "173.5200",
            "4. close": "174.9500",
            "5. volume": "61727425"
        },
        "2024-05-17": {
            "1. open": "173.5500",
            "2. high": "179.6300",
            "3. low": "172.7500",
            "4. close": "177.4600",
            "5. volume": "77445845"
        },
        "2024-05-16": {
            "1. open": "174.1000",
            "2. high": "175.7900",
            "3. low": "171.4300",
            "4. close": "174.8400",
            "5. volume": "59812220"
        },
        "2024-05-15": {
            "1. open": "179.9000",
            "2. high": "180.0000",
            "3. low": "173.1100",
            "4. close": "173.9900",
            "5. volume": "79662993"
        },
        "2024-05-14": {
            "1. open": "174.4959",
            "2. high": "179.4900",
            "3. low": "174.0700",
            "4. close": "177.5500",
            "5. volume": "86407422"
        },
        "2024-05-13": {
            "1. open": "170.0000",
            "2. high": "175.4000",
            "3. low": "169.0000",
            "4. close": "171.8900",
            "5. volume": "67018903"
        },
        "2024-05-10": {
            "1. open": "173.0500",
            "2. high": "173.0599",
            "3. low": "167.7500",
            "4. close": "168.4700",
            "5. volume": "72627178"
        },
        "2024-05-09": {
            "1. open": "175.0100",
            "2. high": "175.6200",
            "3. low": "171.3700",
            "4. close": "171.9700",
            "5. volume": "65950292"
        },
        "2024-05-08": {
            "1. open": "171.5900",
            "2. high": "176.0600",
            "3. low": "170.1500",
            "4. close": "174.7200",
            "5. volume": "79969488"
        },
        "2024-05-07": {
            "1. open": "182.4000",
            "2. high": "183.2600",
            "3. low": "177.4000",
            "4. close": "177.8100",
            "5. volume": "75045854"
        },
        "2024-05-06": {
            "1. open": "183.8000",
            "2. high": "187.5600",
            "3. low": "182.2000",
            "4. close": "184.7600",
            "5. volume": "84390253"
        },
        "2024-05-03": {
            "1. open": "182.1000",
            "2. high": "184.7800",
            "3. low": "178.4200",
            "4. close": "181.1900",
            "5. volume": "75491539"
        },
        "2024-05-02": {
            "1. open": "182.8600",
            "2. high": "184.6000",
            "3. low": "176.0200",
            "4. close": "180.0100",
            "5. volume": "89148041"
        },
        "2024-05-01": {
            "1. open": "182.0000",
            "2. high": "185.8600",
            "3. low": "179.0100",
            "4. close": "179.9900",
            "5. volume": "92829719"
        },
        "2024-04-30": {
            "1. open": "186.9800",
            "2. high": "190.9500",
            "3. low": "182.8401",
            "4. close": "183.2800",
            "5. volume": "127031787"
        }
    }
}
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

API_KEY = " PATQ4T8T8NAR3SE8"
FUNCTION = "TIME_SERIES_DAILY"

TWILIO_SID= "ACd74a126cc857b8e974442bf1c0764d78",
TWILIO_AUTH_TOKEN = "e235bc67c10f95762d16aa35717e7c97"

## To get news from news api

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
API_KEY = "938ca3a2ddc3405294abbb95808f0a70"

COMPANY_NAME = "Tesla Inc"


# api_url = https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=IBM&apikey=demo
import requests
from twilio.rest import Client

stock_parameters = {
    "function": FUNCTION,
    "symbol": STOCK_NAME,
    "apikey": API_KEY,
}
response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
response.raise_for_status()
# print(response)

# stock_data = response.json()
# print(stock_data)

## LOGIC OF DAY 36

data = stock_data["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]

yesterday_data = data_list[0]
yesterday_data_close = yesterday_data["4. close"]

day_bef_yesterday_data = data_list[1]
day_bef_yesterday_data_close = day_bef_yesterday_data ["4. close"]

stock_difference = abs(float(yesterday_data_close) - float(day_bef_yesterday_data_close))
# print(stock_difference)

diff_percent = stock_difference / float(yesterday_data_close)*100
# print(diff_percent)

if diff_percent > 1:
    news_parameters = {
        "qInTitle": COMPANY_NAME,
        "apiKey": API_KEY,
    }

    response = requests.get(NEWS_ENDPOINT, params=news_parameters)
    response.raise_for_status()

    news_data = response.json()
    news_articles = news_data["articles"]
    three_articles = news_articles[:3]
    print(three_articles)

    # twiolio msg


    formatted_articles = [f"Headline: {news_articles['title']}.\nBrief: {news_articles['description']}" for article in three_articles]
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    for article in formatted_articles:
        message = client.messages.create(
            body = formatted_articles,
            from_="+13144925361",
            to = "+917021753382",
        )