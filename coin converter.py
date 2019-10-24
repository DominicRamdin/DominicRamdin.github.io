def fromUSD():
    
    print('what currency do you want to convert to?')
    print('Possible conversions - Canadian Dollar, Austrailian Dollar, Great Britain Pound, Euro, Mexican Peso, Japenese Yen, Indian Rupee, Chinese Yuan Renminbi')
    currency = input('choose currency: ')
  
    
    if currency == ("Canadian Dollar"):
     

      print('you chose', currency)

      amount = input('how much USD would you like to convert: ')
      
      print(amount, 'USD chosen')
      print(int(amount)*1.31, 'CAD')

    elif currency == ("Austrailian Dollar"):


      amount = input('how much USD would you like to convert: ')
      
      print(amount, 'USD chosen')
      print(int(amount)*1.46, 'AUD')
    
    elif currency == ("Great Britain Pound"):


      amount = input('how much USD would you like to convert: ')
      
      print(amount, 'USD chosen')
      print(int(amount)*0.78, 'GBP')
    
    elif currency == ("Euro"):


      amount = input('how much USD would you like to convert: ')
      
      print(amount, 'USD chosen')
      print(int(amount)*0.9, 'Euro')
    
    elif currency == ("Mexican Peso"):


      amount = input('how much USD would you like to convert: ')
      
      print(amount, 'USD chosen')
      print(int(amount)*19.12, 'MXN')
    
    elif currency == ("Japanese Yen"):


      amount = input('how much USD would you like to convert: ')
      
      print(amount, 'USD chosen')
      print(int(amount)*108.61, 'JPY')
    
    
    elif currency == ("Indian Rupee"):


      amount = input('how much USD would you like to convert: ')
      
      print(amount, 'USD chosen')
      print(int(amount)*70.77, 'INR')   
    
    
    elif currency == ("Chinese Yuan Renminbi"):


      amount = input('how much USD would you like to convert: ')
      
      print(amount, 'USD chosen')
      print(int(amount)*7.01, 'CNY')



def toUSD():
    
    print('what currency do you want to convert from?')
    print('Possible conversions - Canadian Dollar, Austrailian Dollar, Great Britain Pound, Euro, Mexican Peso, Japenese Yen, Indian Rupee, Chinese Yuan Renminbi')
    currency = input('choose currency: ')
  
    if currency == ("Canadian Dollar"):
     

      print('you chose', currency)

      amount = input('how much of this Currency would you like to convert: ')
      
      print(amount, 'CAD chosen')
      print(int(amount)*0.76, 'USD')

    elif currency == ("Austrailian Dollar"):


      amount = input('how much USD would you like to convert: ')
      
      print(amount, 'AUD chosen')
      print(int(amount)*0.68, 'USD')
    
    elif currency == ("Great Britain Pound"):


      amount = input('how much USD would you like to convert: ')
      
      print(amount, 'GBP chosen')
      print(int(amount)*1.29, 'USD')
    
    elif currency == ("Euro"):


      amount = input('how much USD would you like to convert: ')
      
      print(amount, 'EUR chosen')
      print(int(amount)*1.11, 'USD')
    
    elif currency == ("Mexican Peso"):


      amount = input('how much USD would you like to convert: ')
      
      print(amount, 'MXN chosen')
      print(int(amount)*0.052, 'USD')
    
    elif currency == ("Japanese Yen"):


      amount = input('how much USD would you like to convert: ')
      
      print(amount, 'JPY chosen')
      print(int(amount)*0.0092, 'USD')
    
    
    elif currency == ("Indian Rupee"):


      amount = input('how much USD would you like to convert: ')
      
      print(amount, 'INR chosen')
      print(int(amount)*0.014, 'USD')   
    
    
    elif currency == ("Chinese Yuan Renminbi"):


      amount = input('how much USD would you like to convert: ')
      
      print(amount, 'CNY Chosen')
      print(int(amount)*0.14, 'USD') 




whichway = input('do you want to convert from USD or to USD? Type from for from USD or to form to USD: ')

if whichway == ('to'):
  
  toUSD()

elif whichway == ('from'):
  
  fromUSD()

else: 
  print('invalid input')