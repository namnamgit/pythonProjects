while True:
	number_trick = int(input('Think of a number: '))
	number, number_trick = number_trick, number_trick * 2
	print('Double it: %d' % number_trick)
	number_trick = number_trick + 6
	print('Add on six: %d' % number_trick)
	number_trick = number_trick / 2
	print('Halve it. That means cut it into half: %d' % number_trick)
	number_trick = number_trick - number
	print('Take away the first number you thought of: %d' % number_trick)
	input('And your answer is three: %d\n' % number_trick)
