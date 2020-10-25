#!/usr/bin/env python
# coding: utf-8

# In[2]:


database={1001:{'name':'satish bokka',
                'age':22,
                'email':'bokkasatish019@gmail.com',
                'password':1935,
                'amount':5000
               },
          1002:{'name':'jaya',
                'age':35,
                'email':'jaya@gmail.com',
                'password':1335,
                'amount':15000
               }
         }
i=int(input("Enter your choice:\n 1.signin\n 2.sign up\n 3.Exit"))
if(i==1):
    account=int(input("Enter Account Number:"))
    passkey=int(input("Enter password:"))
    if(account in database.keys() and passkey==database[account]['password']):
        print("welcome",database[account]['name'])
        j=int(input("Enter your choice:\n1.check balance\n2.Deposit balance\n3.withdrawal\n4.logout"))
        while (j<5):
            if(j==1):
                print("Your balance:",database[account]['amount'])
                
            elif(j==2):
                y=int(input("deposit amount:"))
                database[account]['amount']=database[account]['amount']+y
                
            elif(j==3):
                z=int(input("Enter withdraw amount"))
                print("collect your cash:",z)
                database[account]['amount']=database[account]['amount']-z
                
            else:
                print("sucessfully logged out")
                break
            j=int(input("Enter your choice:\n1.check balance\n2.Deposit balance\n3.withdrawal\n4.logout"))
    else:
        print("wrong password")
elif(i==2):
    account=int(input("enter the account number:"))
    details=input("enter the fields:name,age,password,amount each seperated by coma and against colon")
    database[account]=details
    print(database)
    print("account is updated successfully")
else:
    print("exited successfully")


# In[ ]:




