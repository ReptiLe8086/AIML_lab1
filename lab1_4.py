import json
import csv


def data_convert(file):
    handle = open(file)
    data = json.loads(handle.read())
    handle.close()
    return data


def csv_write(file, data):
    handle = open(file, 'w', newline='')
    out = csv.writer(handle, delimiter=",")
    header = ["item", "country", "year", "sales"]
    out.writerow(header)
    for unit in data:

        item = unit['item']
        country_info = unit['sales_by_country']

        for country in country_info:
            years_info = country_info[country]

            for year in years_info:
                sales_count = years_info[year]
                row = [item, country, year, sales_count]
                out.writerow(row)


if __name__ == '__main__':
    converted = data_convert("sales.json")
    csv_write("output.csv", converted)
