import re
 
def organisation_idchecker():
  
   match = re.compile(r"") # Your Regex goes between the double quotes
 
   organisation_id = input("Enter the organisation id: ")
 
   if re.fullmatch("^\d*([a-z]*$)/", organisation_id):
       print (f"'{organisation_id}'looks like a valid organisation id")
   else:
       print ("Invalid Organisation id")
