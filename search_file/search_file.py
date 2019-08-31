
search_string = 'verifying'

print('---- Without using with -----')

file_news = open('news.txt')
news = file_news.readlines()

for line_no, line in enumerate(news, 1):
    if search_string in line:
        print(line_no, ':', line)

file_news.close()


print('---- Using with -----')


with open('news.txt') as news_file:
    for line_no, line in enumerate(news_file, 1):
        if search_string.lower() in line.lower():
            print(line_no, ':', line)
