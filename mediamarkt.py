import scrapy
import gspread

gc = gspread.service_account(filename='scrapping-link-378022-add03958923b.json')

sh = gc.open("Scrapping")

worksheet = sh.get_worksheet(0)

# print(worksheet.acell('A1').value)
# worksheet.update('A1','dominio')

class scrappingMediamarkt(scrapy.Spider):
    name = 'parascrapear'
    nrow = len(worksheet.row_values(1)) - 1
    print('Número de filas: ' + str(nrow))
    urls = worksheet.col_values(2)
    urls.pop(0)
    # print(urls)
    # allowed_domains = ['mediamarktcanarias.com']
    start_urls = urls
    rowActual=1

    def parse(self, response):
        # price = response.css('meta').attrib['property']
        
        url = response.url
        cell = worksheet.find(url)
        row = cell.row
        company = worksheet.cell(row,1).value
        if company == 'mediamarkt':
            data = response.css('meta[property="og:price:amount"]::attr(content)').extract_first()
        worksheet.update_cell(row,3,data)

        # class pccomponentes price <div class="priceBlock" id="priceBlock" data-baseprice="173.99" data-price="173.99" data-tax="1.21