import android
import time

droid = android.Android()

contact_list=[]
#get all contact ids
contacts= droid.contactsGetContactIds()
#print droid.contactsGetAttributes().result
for contact in contacts:
    if hasattr(contact, "__len__"):
    	
        for con in contact:
        	#get attributes for contact
            q = droid.contactsGetContactById(con,['display_name','has_phone_number','phonebook_label','lookup'])
            
            res=q.result
            contact_list.append(res["display_name"])
            print res['display_name'].upper()
            time.sleep(1)
        #print type(contact)
    #break
#for names in sorted(contact_list):
	#print names.upper()
#print sorted(contact_list)
