import os
import prosmotr as pr
import proverka_izmenen as prover
import proverka_izmenen as pro
import izmenit as izm
def izmin():
    print(pr.prosm())

    with open('D:\Python_Learning\Lesson_8\Seminar8_2\sleSH2_file.txt', 'r', encoding='utf-8') as file:
            with open("D:\Python_Learning\Lesson_8\Seminar8_2\ееempl.txt", "a+",encoding='utf-8') as links:        
             
                d = izm.b
                for line in file:
                    # if substring contain in a line then don't write it
                    if d not in line.strip("\n"):
                        links.write(line + '\n' )                                                          

    os.replace("D:\Python_Learning\Lesson_8\Seminar8_2\ееempl.txt",  'D:\Python_Learning\Lesson_8\Seminar8_2\sleSH2_file.txt')
    print(pr.prosm())   # переписал изменяемый файл отдельно     