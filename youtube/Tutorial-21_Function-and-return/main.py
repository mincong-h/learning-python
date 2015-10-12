# 1
def allowed_dating_age(my_age) :
  girls_age = my_age / 2 + 7
  return girls_age
# 1.1 example
mincongs_limit = allowed_dating_age()
print("i can date firls", mincongs_limit, "or older")


# 2
def get_gender(sex='unknown') :
  if sex is 'm' :
    sex = "Male"
  elif sex is 'f' :
    sex = "Female"
  print(sex)
# 2.1 example
get_gender('m') # 'Male'
get_gender('f') # 'Female'
get_gender() # 'unknown'
