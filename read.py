data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1 # count = count + 1
		if count % 100000 == 0: # % 為求除1000的餘數
			print(len(data))

print('檔案讀取完畢，總共有', len(data), '筆資料')

#算留言平均長度
sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
print('平均是', sum_len/len(data))