import time
import progressbar

data = []
count = 0
bar = progressbar.ProgressBar(max_value=1000000)
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		bar.update(count)
print('檔案讀取完了，總共有',len(data), '筆資料')
print(data[0])


#計算留言的平均長度
sum_len = 0
for d in data:
	sum_len = sum_len + len(d)

print('平均留言長度是', sum_len/len(data))

#清單的概念，篩出多少筆留言長度少於100
new = []
for d in data:
 	if len(d) < 100:
 		new.append(d)
print('一共有',len(new),'筆留言長度小於100')
print(new[0])

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有', len(good), '筆留言提到good')
print(good[0])

#list comprehension 清單快寫法 
good = ['wow' for d in data if 'good' in d]
# print(good)

bad = ['bad' in d for d in data]
# print(bad)

#以上快寫法相等於:
bad = []
for d in data:
	bad.append('bad' in d)


#文字計數
start_time = time.time()
wc = {} #word_count
for d in data:
	words = d.split()  #spli預設空白建
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1 #新增key進wc字典
for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])
end_time = time.time()
print('花了', end_time - start_time, 'seconds')
print(len(wc))
print(wc['Allen'])

while True:
	word = input('請問你想查什麼字: ')
	if word == 'q':
		break
	if word in wc:
		print(word, '出現過的次數為', wc[word])
	else:
		print('這個字沒出現過喔')
print('感謝使用')