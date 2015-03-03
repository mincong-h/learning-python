# definition
def health_calculator(age, apples_ates, cigs_smoled):
  answer = (100 - age) + (apples_ates * 3.5) - (cigs_smked * 2)
  print(answer)
  
# data preparation
mincong_data = [27, 20, 0]

# execution
health_calculator(mincong_data[0], mincong_data[1], mincong_data[2])
health_calculator(*mincong_data)
