import android
droid = android.Android()

def contactFromName(name):

  uri='content://com.android.contacts/data'
  filter='display_name LIKE?'
  args=['%'+name+'%']
  columns=['data4']

  contacts=droid.contactsQueryContent(uri, columns,filter,args).result
  print contacts
  
  #if len(contacts)>0:
    #for c in contacts:
      #cs.append(c['data4'])

  
while True:
    contact = raw_input('Contact Name: ')
    contactFromName(contact)