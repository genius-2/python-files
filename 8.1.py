s = "У лукоморья 123 дуб зеленый 456"
if 'я' in s:
    print (f'1)я в этой строке под индексом {s.index("я")} .')
else: 
    print ('1)я не встречается')
print (f'2)в этой строке {s.count("у")} раз')
if s.isalpha() == False:
    print(f'3)не только буквы в верхнем регистре {s.upper()}')
else:
    print('3)Строка состоит только из букв')
if len(s) > 4:
    print(f'4)длина строки {len(s)} в нижнем регистре {s.lower()}')
print(f'5) О{s[1:]}')
print("type 'end' to exit ")
e=str(input())