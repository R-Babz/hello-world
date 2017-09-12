job_code = 'A-E'
hours_worked = '0-40'

while (True):
    job_code = input('Please enter your job code (A-E): ')
    if job_code < 'A' or job_code > 'E':
        print('Invalid job code entered, please try again!')
    elif len(job_code) >1:
        print('Invalid,please try again')
    else:
       break

while True:
    try:
       hours_worked = float(input('Please enter the number of hours worked (0-40): '))
       if hours_worked < 0 or hours_worked > 40:
          print('Invalid hours worked entered, please try again!')
          continue
       break
    except ValueError: print('Try again')


salary = 0.0
if job_code == 'A':
    salary = hours_worked * 7.25
elif job_code == 'B':
    salary = hours_worked * 7.75
elif job_code == 'C':
    salary = hours_worked * 8.50
elif job_code == 'D':
    salary = hours_worked * 9.25
elif job_code == 'E':
    salary = hours_worked * 9.75

print('Your salary earned for', hours_worked, 'hours is $', salary)