import json
import urllib2
import urllib
import sys

testthis = urllib.urlopen('https://anontargets.org/OpBeast/Download/?type=webtargets&format=json')
jsontest = json.loads(testthis.read().replace(" ",""))
testthis.close()

i = 1

for key,value in jsontest.items():
    websites = value['Name']
    print "%s. %s" % (i, websites)
    i = i+1


websiteselect= raw_input("\nWhat website would you like to know more about? Type the URL from the list above and hit enter: ")
print "\n"
print "\n"

try:
    jsontest[websiteselect]['Name']
except KeyError as e:
    print "This website is not on the list. Exiting."
    sys.exit()

try:
    URL = jsontest[websiteselect]['Name']
except KeyError as e:
    URL = "N/A"

try:
    upstatus = jsontest[websiteselect]['State']
except KeyError as e:
    upstatus = "N/A"

try:
    jsontest[websiteselect]['CloudflareProtected']
    cfproc = 'Yes'
except KeyError as e:
    cfproc = 'No'

try:
    ipaddy = jsontest[websiteselect]['IPAddress']
except KeyError as e:
    ipaddy = "N/A"

try:
    host = jsontest[websiteselect]['Host']
except KeyError as e:
    host = "N/A"

try:
    registrar = jsontest[websiteselect]['Registrar']
except KeyError as e:
    registrar = "N/A"

try:
    abuseemail = jsontest[websiteselect]['AbuseEmail']
except KeyError as e:
    abuseemail = "N/A"

try:
    ownername = jsontest[websiteselect]['OwnerName']
except KeyError as e:
    ownername = "N/A"

try:
    owneremail = jsontest[websiteselect]['OwnerEmail']
except KeyError as e:
    owneremail = "N/A"

try:
    webhost = jsontest[websiteselect]['WebHost']
except KeyError as e:
    webhost = "N/A"

try:
    hostcountry = jsontest[websiteselect]['HostCountry']
except KeyError as e:
    hostcountry = "N/A"

try:
    hostemail = jsontest[websiteselect]['HostEmail']
except KeyError as e:
    hostemail = "N/A"

try:
    notes = jsontest[websiteselect]['Notes']
except KeyError as e:
    notes = "N/A"

if URL == '' or URL == 'N/A':
    pass
else:
    print "Website URL: %s \n" % (URL)
if upstatus == '' or upstatus == 'N/A':
    pass
else:
    print "Up Or Down?: %s \n" % (upstatus)
if cfproc == '' or cfproc == 'N/A':
    pass
else:
    print "Protected By CloudFlare?: %s \n" % (cfproc)
if ipaddy == '' or ipaddy == 'N/A':
    pass
else:
    print "IP Address: %s \n" % (ipaddy)
if host == '' or host == 'N/A':
    pass
else:
    print "Host: %s \n" % (host)
if ownername == "N/A" or ownername == "":
    pass
else:
    print "Owner Name: %s \n" % (ownername)
if owneremail == "N/A" or owneremail == "":
    pass
else:
    print "Owner Email: %s \n" % (owneremail)
if registrar == '' or registrar == 'N/A':
    pass
else:
    print "Registrar: %s \n" % (registrar)
if abuseemail == '' or abuseemail == 'N/A':
    pass
else:
    print "Registrar Abuse Email: %s \n" % (abuseemail)
if webhost == '' or webhost == 'N/A':
    pass
else:
    print "Web Host: %s \n" % (webhost)
if hostcountry == '' or hostcountry == 'N/A':
    pass
else:
    print "Web Host Country: %s \n" % (hostcountry)
if hostemail == '' or hostemail == 'N/A':
    pass
else:
    print "Web Host Email: %s \n" % (hostemail)
if notes == '' or notes == 'N/A':
    pass
else:
    print "\n Notes: %s \n" % (notes)



