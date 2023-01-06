data = []
count = 0
with open('reviews.txt','r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0: # 百分比符號%表示求餘數 
		print(len(data)) #讀取檔案的進度
print(len(data))