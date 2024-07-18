import yfinance as yf
from rest_framework.response import Response
from rest_framework.decorators import api_view

def fetch_market_data(indices):
    data = {}
    for name, ticker in indices.items():
        try:
            ticker_data = yf.Ticker(ticker)
            hist = ticker_data.history(period="1mo")
            if not hist.empty:
                close_price = hist['Close'].values[-1]
                open_price = hist['Open'].values[0]
                change = close_price - open_price
                percent_change = (change / open_price) * 100
                data[name] = {
                    "close_price": close_price,
                    "change": change,
                    "percent_change": percent_change
                }
        except Exception as e:
            print(f"Error fetching data for {ticker}: {e}")
            data[name] = {
                "close_price": None,
                "change": None,
                "percent_change": None
            }

    return data

@api_view(['GET'])
def global_market_data(request):
    indices = {
        "GIFT_NIFTY": "^NSEI",
        "SP500": "^GSPC",
        "DOW_JONES": "^DJI",
        "NASDAQ": "^IXIC",
        "NIKKEI_225": "^N225",
        "HANG_SENG": "^HSI"
    }
    data = fetch_market_data(indices)
    return Response(data)

@api_view(['GET'])
def indian_market_data(request):
    indices = {
        "NIFTY50": "^NSEI",
        "NIFTYBANK": "^NSEBANK",
        "SENSEX": "^BSESN",
        "BANKEX": "^BSEBANK",
        "FINNIFTY": "^NSEIFC",
        "INDIAVIX": "^INDIAVIX",
        "SENSEX50": "^BSESN50",
        "NIFTYNXT50": "^NSENEXT50"
    }
    data = fetch_market_data(indices)
    return Response(data)

@api_view(['GET'])
def top_indian_companies_data(request):
    companies = {
        "RELIANCE": "RELIANCE.NS",
        "TCS": "TCS.NS",
        "HDFCBANK": "HDFCBANK.NS",
        "INFY": "INFY.NS",
        "HINDUNILVR": "HINDUNILVR.NS",
        "ICICIBANK": "ICICIBANK.NS",
        "SBI": "SBIN.NS",
        "KOTAKBANK": "KOTAKBANK.NS",
        "BHARTIARTL": "BHARTIARTL.NS",
        "BAJAJFINANCE": "BAJFINANCE.NS"
    }
    data = fetch_market_data(companies)
    return Response(data)










# import requests
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status

# @api_view(['GET'])
# def get_stock_data(request):
#     url = "https://www.nseindia.com/api/quote-equity?symbol=RELIANCE"
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
#         "Accept": "application/json",
#         "Accept-Language": "en-US,en;q=0.9",
#         "Connection": "keep-alive",
#         "Referer": "https://www.nseindia.com/get-quotes/equity?symbol=RELIANCE",
#         "Sec-Fetch-Dest": "empty",
#         "Sec-Fetch-Mode": "cors",
#         "Sec-Fetch-Site": "same-origin"
#     }

#     cookies = {
#         "AKA_A2": "A",
#         "_abck": "1101BA16CD5A666CEF583B04812C077F~0~YAAQlMcsMTiP5LaQAQAAlhO6twxjgZ/D9dgS5wYKwtkEaQJ+3oEQPMgi7SsfqWDedp0pMjT7h7iHdRpL2TEUXS8liJvKZXi9Agf9/K/DnSuxCuQey9ty2y8iSp32TwyDkyKfjpO/OAYz/dzSDm0nl+PWmENUO10KQXez7U3dIHiIcoU9Y/FXgbDWWwYPxiKqQ8HKooZOsN6+3A3oXqO1zG9W3yYfJoFX17OLwh2oCDOtPksNt62RExC+CSu7OasTpJr+52TkPpz8g03Iw/jJNat+0epherTiEf2O0yK5k+8zyOW//UuzuPDquTAPdnLkYT0slArfbaOkaVm1jz+8XnJH11Xlaj8GSIsilc76hv35AyyQVJkRZ4QybcZNzCyauqp/kAp5w9X8mDHbSFWMKZIrKBOtTBooeeM=~-1~-1~-1",
#         "_ga": "GA1.1.1479807168.1720876281",
#         "_ga_87M7PJ3R97": "GS1.1.1721069336.2.1.1721070485.35.0.0",
#         "ak_bmsc": "B9047FC98F4B992B8ECA0EA9B90260A5~000000000000000000000000000000~YAAQhscsMdlJ/rWQAQAA2HvKtxj1Upb3nsF3zTm2xPWyYleUMnXDdZgz1ffb3aOg7daXUoZuC7MA0yMnTnCXbyb3AIwNrw2YW8/s4N9w/VlBLbs1a3gBTZTO9HlhHc3i8JXiwz9L9exlQvGlWHLAMFfrq6UnSgLtyFhNeKYmlpV8GF2vXueS0KSyHXq1of3xj4e3AJ6Gk/3nPLi4FxkXn2AFXXX8Sml5CtrmcT1UPuQc4fMzC/+N3ns19J983KXZCk5t8Yjlf8zVOPlbhI0++Y60olNc1YDCZQDVsU8J64AREBsNmPPjjz3MQ0qtTz3XZrv4pOjWvp0AH2Lw49L1a9Xao/Z1Zzpu0gze2J3V0GASJNnpmmF658Y9FEzhn9inxSwxlrPJCFO8dWvjfK8pZMG1Uq6/DM2dnHfyyZFtCCb6ai+tiV0wNxw2vELKfm0FJDcgD+5swxMsPT9qsxF1zATZb4D5EnPnQCR0co7A/bo07Y8W0plXyvIVSKOLbpxx2ua0FC9CdKGN5b4UVXm35QaUsA==",
#         "bm_mi": "8554A803F4D71208551CC8503F4F7E3D~YAAQlMcsMemM5LaQAQAAJNC5txidIaLPmW7eQNhT7x+Vp4WoRXZPsDILiUbgYzrfOpo96RvBn8ZXDZV8yt3H8DTDT7OfIw4wd2rOoPLSVf8k/xjdZaKqKmdylBzDo7pW3FxNTcTeVSzbLQTHPKhDc9CmfNwKuCtaHyf7OFC+OhpACm+HLUA6I687XBZKiDFLunmmqxnsD36jkZZKn/GwFGXXXElwKtnZ7wzmz79uSdWbmvT5lOy/+FH5V0wckp81PpPPK11O+v3D2c3xAz01tl4S9etwTr/vRH1TF5dB8fRjTtGOd2KTjkuF2yzub/rmr5FyS6AFkJmUVtf5I4UXAA==~1",
#         "bm_sv": "E5224FF53517346B3AD90F458ECA3C9A~YAAQlMcsMTAz5baQAQAAMhTPtxgflTRz2Sq2KXtPkVdTuMB8s3M6Jra8HWsz0vUDzCNx7MCsChzP8/n1r7370b9vaRl3v8PkUoipnYQxAxMG9ujDh0/daMkto2hnM4zXYHU/Oak0wPP8rUCS9JmlopEZzlqVspsCqgp3WdnFju6ZXHBydy4oxWCpqxc72ulIL2bFzZq/c8+2Mtm/Xet6JqliPxMyRbhMyZIfbdJdqoH8NTqVTCigLo6uTpmD64GUE3ZtEg==~1",
#         "bm_sz": "D871F3925F3C1285C70182DFD6580CDC~YAAQlMcsMTEz5baQAQAAMhTPtxiUQO9wxk3KMEkpiTJjeXmRHihYeAl6L0obXfdr1EZAKl+O/YbZZbjOdcrcqPbHSpOxGrVXPpsskP3ZVG4uCsBxIpSzYBcMKPMr+FnBgKdoXo01xpLkBcwMfk/9K088wv14IBDn5BzJQnY1UBoWY7yex6TO42Ln4bfEgO4PmKu16KAg7yQOyTt9kdKYFiTu9R3Y5xyBYKifbt85da4RPucxJyOX/02eEIf6ol0mA8T2DnqJvwqPYM5gRglJODrAvIRmrgC7Nmnz7633NKELeauZLqnlUhBzN5p1uaqaLyp06N27jQqGKkMHV8vU8joFP+J+ZcE3NNHlKjzasnjVEGyjmK5K00+sHvgg3c7pfWUnx7fDqDw3C0/QgwFLkxilm66kNDLIkZYPKGvDieW3xac9TptGNR4Oz0vQbGahaj6Gy1gnqX9C4M5rHmkK89TVMgybaAjrlHlnMv21aDliKf1hAbRqY00J/2ZGV9LuttE8BQS4QWPIzoGYpaDbvNR2tMnoCo+EGWX3~3359558~4408116",
#         "defaultLang": "en",
#         "nseQuoteSymbols": '[{"symbol":null,"identifier":null,"type":"equity"},{"symbol":null,"identifier":null,"type":"equity"}]',
#         "nseappid": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhcGkubnNlIiwiYXVkIjoiYXBpLm5zZSIsImlhdCI6MTcyMTA2OTM0NiwiZXhwIjoxNzIxMDc2NTQ2fQ.GaYhIMd44g2yKZPrenV3Vg-ald6t5FwX-cQMuxBuOlk",
#         "nsit": "Nsg0OLjjU5OQdsGLCYNpUweP"
#     }

#     try:
#         response = requests.get(url, headers=headers, cookies=cookies)
#         response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
#         data = response.json()
#         return Response(data, status=status.HTTP_200_OK)
#     except requests.exceptions.RequestException as e:
#         return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)