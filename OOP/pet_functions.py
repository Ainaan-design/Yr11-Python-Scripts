#animal_category = 'Cat'
#age = 3
#vaccinated = True
#ccard = '3423 2326 7543 1234'
#billing_address = '17 Park Drive, The Shire 2695'
#owner_name = 'Alex Ngyuen'
#account_balance = 129.95

#def help():
  #print('Welcome to the Pet Data Management System')
  #print("Every vet's best friend")

#def increase_age():
 # global age
  #age = age + 1

#def verify_credit_card(card_num):
 # if len(card_num) == 19:
  #  if len(card_num.split()) == 4:
  #    return True
 # return False

#num = '1234 4334 1001 0000'
#if verify_credit_card(num) == True:
#  print('VALID')
#else:
# print('INVALID')


#help()
#increase_age()
#print(age)

#animal_category = 'Cat'
#age = 3
#vaccinated = True
#ccard = '3423 2326 7543 1234'
#billing_address = '17 Park Drive, The Shire 2695'
#owner_name = 'Alex Ngyuen'
#account_balance = 129.95

#def help():
  #print('Welcome to the Pet Data Management System')
  #print("Every vet's best friend")

#def increase_age():
 # global age
  #age = age + 1

#def verify_credit_card(card_num):
  #card_num = input("What is your credit card number? ")
  #if len(card_num) == 19:
    #if len(card_num.split()) == 4:
      #return True
  #return False

#num = ccard
#if verify_credit_card(num) == True:
 # print('VALID')
#else:
 #print('INVALID')


#help()
#increase_age()
#print(age)

#animal_category = 'Cat'
#age = 3
#vaccinated = True
#ccard = '3423 2326 7543 1234'
#billing_address = '17 Park Drive, The Shire 2695'
#owner_name = 'Alex Ngyuen'
#account_balance = 129.95

#def help():
 # print('Welcome to the Pet Data Management System')
 # print("Every vet's best friend")

#def increase_age():
  #global age
  #age = age + 1

#def verify_credit_card(card_num):
  #card_num = input("What is your credit card number? ")
  #if len(card_num) == 19:
   # if len(card_num.split()) == 4:
     # return True
  #return False

#num = ccard
#if verify_credit_card(num) == True:
 # print('VALID')
#else:
 #print('INVALID')
 #if verify_credit_card == True:
   # account_balance = account_balance - 39
    #print('$'+account_balance)

#help()
#increase_age()
#print(age)

animal_category = 'Cat'
age = 3
vaccinated = True
ccard = '3423 2326 7543 1234'
billing_address = '17 Park Drive, The Shire 2695'
owner_name = 'Alex Ngyuen'
account_balance = 129.95

def help():
  print('Welcome to the Pet Data Management System')
  print("Every vet's best friend")

def increase_age():
  global age
  age = age + 1

def verify_credit_card(card_num):
  card_num = input("What is your credit card number? ")
  if len(card_num) == 19:
    if len(card_num.split()) == 4:
      return True
  return False
  
num = ccard
if verify_credit_card(num) == True:
  print('VALID')
else:
 print('INVALID')

help()
increase_age()
print(age)