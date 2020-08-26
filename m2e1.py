"""
Python script to solve Module 2 - Exercise 1 from C1b3rw4ll
We have tuned an SDR receiver in 1090 MHz and we have received a sequence ...
It is "8D34508F201432CF060000303030" but we do not know how to interpret it so
you will have to indicate the flag of the form
module2 {capital letters (Reg.ID + Callsign)}
"""


import pyModeS as pms
import webbrowser


# Function to convert list into string
def listToString(L):
    # return string
    return "".join(str(x) for x in L)


# Hex values to binary
binData = pms.hex2bin('8D34508F201432CF060000303030')

# Identifying components of the ADS-B codification
# String to list
res = [str(x) for x in str(binData)]
# Components
df_bin = res[0:5]
ca_bin = res[5:8]
icao_bin = res[8:32]
data_bin = res[32:88]
pi_bin = res[88:112]

print('-------- ADS-B String HexDecoded --------')
print('DF:' + pms.bin2hex(listToString(df_bin)))
print('CA:' + pms.bin2hex(listToString(ca_bin)))
print('ICAO:' + pms.bin2hex(listToString(icao_bin)))
print('DATA:' + pms.bin2hex(listToString(data_bin)))
print('PI:' + pms.bin2hex(listToString(pi_bin)))

# The pyModeS include functions that implements above code in order to obtain the ICAO
# but i preferred to make all the process instead. Here is the easy-way:
# pms.adsb.icao('8D34508F201432CF060000303030'))
# It could be use the same library to obtain the CallSign:
print('CallSign:'+pms.adsb.callsign('8D34508F201432CF060000303030'))

# With the ICAO we can obtain the Reg.ID available in some aircraft databases:
url = 'https://junzis.com/adb/?q=' + pms.bin2hex(listToString(icao_bin))
webbrowser.open(url, new=2)
print('Opening a web browser with the aircraft Reg.ID and other info.....')

exit()
