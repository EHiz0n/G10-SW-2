# Data types in Python
from pyscript import display

restaurant_name = 'Platter of Rubicon' # string
owner_name = 'Owner: Kopei Zagreuu' # string
year_established = 1999 # integer
popular_item_price = 'Dolmades: 15' # string

product_names = ['Moussaka', 'Souvlaki', 'Gyro'] # list
has_delivery = True # boolean
business_hours = '11am-8pm on Weekdays, 11am-10pm on Weekends' # string

menu_prices = ['Spanakopita: 13', 'Dolmades: 15', 'Zucchini: 9', 'Feta me meli: 12', 'Tirokroketes: 14'] # list
tax_rate = 0.78 # float

common_allergens = ['Shrimp', 'Tomatoes', 'Egg'] # string

display(f'{restaurant_name}')
display(f'{owner_name}')
display(f'{year_established}')
display(f'{popular_item_price}')

display(f'{product_names}')
display(f'{has_delivery}')
display(f'{business_hours}')

display(f'{menu_prices}')
display(f'{tax_rate}')

display(f'{common_allergens}')