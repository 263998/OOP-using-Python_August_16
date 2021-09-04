import re   
  
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  
  
def check(email):   
  
    if(re.search(regex,email)):   
        print("Valid Email")   
    else:   
        print("Invalid Email")   
      
if __name__ == '__main__' :   
      
    email = "rohit.gupta@mcnsolutions.net"  
    check(email)   
  
    email = "praveen@c-sharpcorner.com"  
    check(email)   
  
    email = "inform2atul@gmail.com"  
    check(email)   

 
    '''loc = "Aug_GENESIS_SDLC_List.xlsx"
    
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    sheet.cell_value(0, 0)
    
    for i in range(sheet.nrows):
        print(sheet.cell_value(i, 0))'''