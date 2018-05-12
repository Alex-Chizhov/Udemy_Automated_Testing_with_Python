links = ['google.com', 'youtube.com', 'ebay.com',]
print((lambda x, y: x + y)('https://', 'mail.ru'))
print([(lambda x, y: x + y)('https://', y) for y in links])


l = [1, 2, 3, 4, 5, 6, 7]
for number in l:
    l[number - 1] = '№' + str(number)
print(l)

l2 = [1,2,3,4,5,6,7]
print(['№' + str(number) for number in l2])


full_links = ['https://' + url for url in links]
print(full_links)

