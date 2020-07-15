###베스트 앨범 데이터 응용##

genres = ['classic', 'pop', 'classic', 'classic', 'pop']
plays = [500, 600, 150, 800, 2500]
genres_set = []

for genre, play in zip(genres,plays):
    tmp = (genre,play)
    genres_set.append(tmp)

print(genres_set)

genres_dict = dict()
for genre in genres:  ### dictionary 의 value에 값을 넣을때는 key값이 사전에 존재하지 않으면 오류가 뜸!
    if genre not in genres_dict:  ## 그래서 key값을 미리 넣어서 딕셔너리를 생성 해 주었당
        genres_dict[genre] = 0

print(genres_dict)
for data in genres_set:  
    if data[0] in genres_dict:
        genres_dict[data[0]] += data[1]

print(genres_dict)


genres_dict = dict()
for genre, play in genres_set:
    genres_dict.setdefault(genre,0)  ##딕셔너리를 생성
    genres_dict[genre] += play  ## 알맞은 value값들을 넣어준다.

print(genres_dict)
