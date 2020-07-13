##베스트앨범
#스트리밍 사이트에서 장르 별로 가장 많이 재생된 노래를 두 개씩
# genres = ['classic', 'pop', 'classic', 'classic', 'pop']
# plays = [500, 600, 501, 800, 900]
# => [3, 2, 4, 1]


genres = ['classic', 'pop', 'classic', 'classic', 'pop']
plays = [500, 600, 150, 800, 2500]

genres_dict = dict()

genre_list=[]
for gen,play in zip(genres,plays):
    pairs = (gen,play)
    genre_list.append(pairs)

print(genre_list)
#딕셔너리 생성
for gen in genres:
    if gen not in genres_dict:
        genres_dict[gen] = 0

for data in genre_list:
    genres_dict[data[0]] += data[1]

print(genres_dict)

genres_dict_sort = sorted(genres_dict.items(),key=lambda x:x[1],reverse=True)
print(genres_dict_sort)

first_sort_list = []
for data in genres_dict_sort:
    first_sort_list.append(data[0])
print(first_sort_list)

#이제 genre_list를 필터대로 소팅하면됨...
##sorting 1##
genre_list_sort= sorted(genre_list,key=lambda x:x[1],reverse=True)
print(genre_list_sort)

##sorting2##
genre_list_sort_complete = []
for standard in first_sort_list:
    tmp = []
    for data in genre_list_sort:
        if data[0] == standard:
            tmp.append(data)
            if len(tmp) == 2:
                break
    genre_list_sort_complete += tmp


print(genre_list)
print(genre_list_sort_complete)
#

result = []
for data in genre_list_sort_complete:
    tmp = genre_list.index(data)
    result.append(tmp)
print(result)
