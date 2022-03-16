def palindrome(words):
	w = []

	for word in words:
		w.append(word)
	
	l = len(w)
	j = l - 1
	i = 0
	
	while i != l:
		if w[j] != w[i]:
			print(words, '不是回文唷!')
			break
		j -= 1
		i += 1

	if i == l:
		print(words, '是回文。')

palindrome(input('回文判斷，請輸入英文單字：'))