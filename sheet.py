import gspread

gc = gspread.service_account(filename='scrapping-link-378022-add03958923b.json')

sh = gc.open("Scrapping")

worksheet = sh.get_worksheet(0)

print(worksheet.acell('A1').value)
# worksheet.update('A1','dominio')