import android
droid = android.Android()
params = droid.getIntent().result[u'extras']
for key in params.keys():
    print key+" is " +params[key]