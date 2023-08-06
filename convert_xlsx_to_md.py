
import pandas as pd

def determine_exchange(stock_code):
    if pd.isna(stock_code):
        return None
    code_str = str(int(stock_code))
    if code_str.startswith('000') or int(stock_code) in [1696, 1896, 1979, 1965]:
        return 'sz'
    elif code_str.startswith(('600', '601', '603')):
        return 'sh'
    elif code_str.startswith('002'):
        return 'sz'
    elif code_str.startswith('300'):
        return 'sz'
    elif code_str.startswith('688'):
        return 'sh'
    else:
        return None

file_path = "/path/to/your/xlsx/file.xls"
xls_data = pd.read_excel(file_path)
stock_data = []
for index, row in xls_data.iterrows():
    code = row['代码']
    name = row['名称']
    exchange = determine_exchange(code)
    if exchange:
        image_url = f"https://image.sinajs.cn/newchart/monthly/n/{exchange}{int(code):06}.gif"
        stock_data.append((name, image_url))

markdown_table = "| 股票名称 | daily走势图 | weekly走势图 | monthly走势图 |\n| --- | --- | --- | --- |\n"
for name, image_url in stock_data:
    daily_url = image_url.replace("monthly", "daily")
    weekly_url = image_url.replace("monthly", "weekly")
    markdown_table += f"| {name} | ![daily走势图]({daily_url}) | ![weekly走势图]({weekly_url}) | ![monthly走势图]({image_url}) |\n"

markdown_file_path = "/path/to/save/markdown/file.md"
with open(markdown_file_path, 'w', encoding='utf-8') as file:
    file.write(markdown_table)
