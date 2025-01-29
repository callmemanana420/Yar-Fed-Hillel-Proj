# import codecs

# def delete_html_tags(html_file, result_file='cleaned.txt'):
    
#     with open(result_file, 'w', encoding='utf-8') as txt:
#         txt.write("")

#     with codecs.open(html_file, 'r', 'utf-8') as file:
#         for row in file:

#             find_first_closing_bracket = row.find(">")
#             find_first_bracket = row.find('<')
#             find_second_bracket = row.find('<', find_first_bracket + 1)

#             if find_first_closing_bracket != -1\
#                 and find_second_bracket != -1:

#                 for index in range(len(row)):
                    
#                     symbol = row[index]

#                     if symbol.isalpha() and\
#                         find_first_closing_bracket < index < find_second_bracket:
#                         # with open(result_file, 'a', encoding='utf-8') as txt:
#                         # txt.write(symbol)
#                         append_to_file(result_file, symbol)
#                     else:
#                         append_to_file(result_file, " ")
#             else:
#                 # with open(result_file, 'a', encoding='utf-8') as txt:
#                 #     txt.write("\n")             
#                 append_to_file(result_file, "\n")


# def append_to_file(file, symbol):
#     with open(file, 'a', encoding='utf-8') as txt:
#         txt.write(symbol)    




# file_name = "draft.html"
# delete_html_tags(file_name, result_file='cleaned.txt')








import codecs
import re

find_text = r'>\s*([а-яА-ЯіїєґІЇЄҐ\s\w-]+)\s*<'
find_text2 = r'<p[^>]*>\s*([^<]+)\s*</p>'



def delete_html_tags(html_file, result_file='cleaned.txt'): 
        words = list()

        with codecs.open(html_file, 'r', 'utf-8') as file: 
            html = file.read()
            
            findall_html = re.findall(find_text, html)
            findall_html2 = re.findall(find_text2, html)

        with open(result_file, 'w', encoding='utf-8') as txt:
            txt.write("\n".join(findall_html))
            txt.write("\n".join(findall_html2))

        with open(result_file, 'r', encoding='utf-8') as txt:
            for i in txt:
                if i.strip():
                    words.append(i)

        with open(result_file, 'w', encoding='utf-8') as txt:
            for i in words:
                 txt.write(i)

file_name = "draft.html"

delete_html_tags(file_name, result_file='cleaned.txt')

