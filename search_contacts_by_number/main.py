import android
#import socketIO_client

droid = android.Android()

def contactFromPhone(phone):

  uri='content://com.android.contacts/data'
  filter='data3 LIKE?'
  args=['%'+phone+'%']
  columns=['display_name']

  contacts=droid.contactsQueryContent(uri, columns,filter,args).result
  print contacts
  cs=[]
  #if len(contacts)>0:
    #for c in contacts:
      #cs.append(c['data4'])

  #print cs
while True:
    contact = raw_input('Contact Phone: ')
    contactFromPhone(contact)
