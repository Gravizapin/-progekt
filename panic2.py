pharse = "Don't panic!"
phlist = list(pharse)
print(pharse)
print(phlist)
new = ''.join(phlist[1:3])
new = new + ''.join([phlist[5], phlist[4], phlist[7], phlist[6]])
print(phlist)
print(new)
