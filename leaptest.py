def Leap_year(start_year, end_year):
  new_var=end_year+1
  for x in range(new_var-start_year):
    if start_year%4==0:
      print(str(start_year)+" is a leap year.")
    start_year+=1
Leap_year(2020, 2024)
