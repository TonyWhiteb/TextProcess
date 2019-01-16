test_name = 'test.txt'
namelist = test_name.split('.')
filetype = namelist[len(namelist)-1]
file_name = namelist[0]

for i in range(3):
   with open((file_name + '{0}' +'.'+filetype).format(i),'w') as f:
       f.write("test")