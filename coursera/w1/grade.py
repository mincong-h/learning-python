def grade(score):
    '''
    Score	Grade
    90~100	A
    70~89	B
    60~69	C
    0~59	D
    others	Invalid score
    '''
    if(90 <= score <= 100): return 'A'
    elif (70 <= score <= 89): return 'B'
    elif (60 <= score <=69): return 'C'
    elif (0 <= score <= 59): return 'D'
    else: 'Invalid score'

# main
print grade(int(raw_input('your grade=')))
