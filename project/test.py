def count_duplicates():
    arq = open('xpress/project/teste.txt', 'r')
    st_arr = arq.read()
    st_arr = st_arr.split('\n')
    for el in st_arr:
        if st_arr.count(el) > 1:
            print(f'{el} aparece {st_arr.count(el)} vezes\n')

count_duplicates()