import htmlmin

folder_reading = r'C:\Users\Aymen Mahmoudi\Lenovo_Sync\Personel\Personal_webpage\dev'
folder_writing = r'C:\Users\Aymen Mahmoudi\Lenovo_Sync\Personel\Personal_webpage\public'
files_reading = ['index','events','experience','publications','life','computer_skills']


for i in range (len(files_reading)):
        
    with open(folder_reading+'\\'+files_reading[i]+'.html','r',encoding='utf-8') as file:
            content = file.read()  
        #print(content)
    content = htmlmin.minify(content, remove_empty_space=True, remove_comments=True)

    with open(folder_writing+'\\'+files_reading[i]+'.html','w',encoding='utf-8') as file:
            file.write(content)
    
        



print ('DONE')