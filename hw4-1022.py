# coding: utf-8
mycourse = {'Mon':'programming', 'Tue':'math', 'Wed':'python'}
f = open('mycourse.csv','w') 
for eng in mycourse.keys():
    print(eng + ':' + mycourse[eng], file = f)   
f.close()
get_ipython().system('type mycourse.csv')
