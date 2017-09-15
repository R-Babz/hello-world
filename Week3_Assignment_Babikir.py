import json

sort_field = ''

while (True):

        sort_field = input('Please enter the sort field name: ')
        if sort_field == 'gender' or sort_field == 'state' or sort_field == 'sale_date':
           break
        print('Invalid value, please try again!')


filename = 'Assignment_3_datafile.json'

with open(filename) as fin:
        json_data= json.loads(fin.read())

        sales ={}
        for record in json_data:
            amount = float(record['sale_amount'])
            key = record[sort_field]
            if key in sales:
                sales[key] += amount
            else:
                sales[key] = amount

        count = 1
        total = 0.0
        print('______________________________________________________________')
        print('Sales by', sort_field)
        print('______________________________________________________________')
        for key in sorted(sales, key=sales.get, reverse=True):
            print('{0}\t{1:25}\t\t{2:12,.2f}'.format(count, key, sales[key]))
            total += sales[key]
            count += 1
        print('Total\t\t\t\t\t\t\t\t{0:12,.2f}'.format(total))
        print('=============================================')
