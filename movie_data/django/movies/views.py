import requests
from django.shortcuts import render, get_object_or_404
from movies.models import Movie, Genre, Certification, OTT, Keyword, Actor, Director, Review
from dotenv import load_dotenv
import os
import random
from rest_framework import status

from rest_framework.decorators import api_view
from rest_framework.response import Response

from movies.serializers import MovieMainListSerializer, MovieSerializer, ReviewSerializer
load_dotenv()
API_KEY = os.environ.get('API_KEY')

order_certi = { 'ALL': 1, '12':2 , '15': 3, '18': 4}

def movie(request):
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
        'api_key': API_KEY,
        'language': 'ko',
        'page': 20,
    }
    response = requests.get(BASE_URL+path, params=params)
    data = response.json()['results']
    for d in data:
        id = d['id']
        path1 = '/movie/' + str(id)
        params1 = {
            'api_key': API_KEY,
            'language': 'ko',
            'append_to_response': 'releases',
        }
        response1 = requests.get(BASE_URL+path1, params=params1)
        data1 = response1.json()
        movie = Movie()
        movie.pk = id
        movie.title = data1['title']
        movie.orginal_title = data1['original_title']
        if data1['overview'] == '':
            continue
        movie.overview = data1['overview']
        movie.poster_path = data1['poster_path']
        if d['release_date'] == '':
            continue
        movie.release_date = data1['release_date']
        movie.runtime = data1['runtime']
        movie.vote_average = data1['vote_average']
        movie.vote_count = data1['vote_count']
        
        path2 = path1 + '/videos'
        params2 = {
            'api_key': API_KEY,
            'language': 'ko',
        }    
        response2 = requests.get(BASE_URL+path2, params=params2)  
        data2 = response2.json()['results']
        
        for d2 in data2:
            movie.video = ''
            if d2['type'] == 'Trailer' or d2['official'] == True:
                movie.video = d2['key']
                break
        if movie.video == '':
            continue
        movie.save()

        genres = data1['genres']
        for genre in genres:
            g1 = Genre(pk=genre['id'], name=genre['name'])
            g1.save()
            g1.movies.add(movie)

        certifi = data1['releases']['countries']
        for cer in certifi:
            if cer['iso_3166_1'] == 'KR' and cer['certification'] != '':
                if cer['certification'] == '전체관람가':
                    cer['certification'] = 'ALL'
                if cer['certification'] == '12세 이상 관람가' or cer['certification'] == '12세 관람가' or cer['certification'] == '12세이상관람가':
                    cer['certification'] = '12'
                if cer['certification'] == '15세 이상 관람가':
                    cer['certification'] = '15'
                if cer['certification'] == '청소년 관람불가' or cer['certification'] == '19':
                    cer['certification'] = '18'                
                c1 = Certification(pk=order_certi[cer['certification']], name=cer['certification'])
                c1.save()
                c1.movies.add(movie)
                break
        else:
            movie.delete()
            continue        

        path3 = path1 + '/watch/providers'
        params3 = {
            'api_key': API_KEY,
            'region' : 'KR',
            'language': 'ko',
        }    
        response3 = requests.get(BASE_URL+path3, params=params3)  
        data3 = response3.json()['results']
        if 'KR' in data3 and 'flatrate' in data3['KR']:
            for d3 in data3['KR']['flatrate']:
                f1 = OTT(pk=d3['provider_id'], name=d3['provider_name'])
                f1.save()
                f1.movies.add(movie)

        path4 = path1 + '/keywords'
        params4 = {
            'api_key': API_KEY,
        }
        response4 = requests.get(BASE_URL+path4, params=params4)
        data4 = response4.json()['keywords']
        for d4 in data4:
            k1 = Keyword(pk=d4['id'], name=d4['name'])
            k1.save()
            k1.movies.add(movie)

        path5 = path1 + '/credits'
        params5 = {
            'api_key': API_KEY,
            'language': 'ko',
        }
        response5 = requests.get(BASE_URL+path5, params=params5)
        data5_cast = response5.json()['cast']
        data5_cast_cut = data5_cast[:5]
        for cast in data5_cast_cut:
            a1 = Actor(pk=cast['id'], name=cast['original_name'])
            a1.profile_path = cast['profile_path'] or ''
            a1.save()
            a1.movies.add(movie)
        data5_crew = response5.json()['crew']
        for crew in data5_crew:
            if crew['job'] == 'Director':
                d1 = Director(pk=crew['id'], name=crew['original_name'])   
                d1.save()
                d1.movies.add(movie)

    return render(request, 'movies/index.html')

def movieid(request):
    print(API_KEY)
    BASE_URL = 'https://api.themoviedb.org/3'
    id = str('350650')
    path1 = '/movie/' + id
    params1 = {
        'api_key': API_KEY,
        'language': 'ko',
        'append_to_response': 'releases',
    }
    response1 = requests.get(BASE_URL+path1, params=params1)
    data1 = response1.json()
    movie = Movie()
    movie.pk = id
    movie.title = data1['title']
    movie.orginal_title = data1['original_title']
    if data1['overview'] == '':
        return
    movie.overview = data1['overview']
    movie.poster_path = data1['poster_path']
    if data1['release_date'] == '':
        return
    movie.release_date = data1['release_date']
    movie.runtime = data1['runtime']
    movie.vote_average = data1['vote_average']
    movie.vote_count = data1['vote_count']
    
    path2 = path1 + '/videos'
    params2 = {
        'api_key': API_KEY,
        'language': 'ko',
    }    
    response2 = requests.get(BASE_URL+path2, params=params2)  
    data2 = response2.json()['results']
    
    for d2 in data2:
        movie.video = ''
        if d2['type'] == 'Trailer' or d2['official'] == True:
            movie.video = d2['key']
            break
    if movie.video == '':
        return
    movie.save()

    genres = data1['genres']
    for genre in genres:
        g1 = Genre(pk=genre['id'], name=genre['name'])
        g1.save()
        g1.movies.add(movie)

    certifi = data1['releases']['countries']
    for cer in certifi:
        if cer['iso_3166_1'] == 'KR' and cer['certification'] != '':
            if cer['certification'] == '전체관람가':
                    cer['certification'] = 'ALL'
            if cer['certification'] == '12세 이상 관람가' or cer['certification'] == '12세 관람가' or cer['certification'] == '12세이상관람가':
                cer['certification'] = '12'
            if cer['certification'] == '15세 이상 관람가':
                cer['certification'] = '15'
            if cer['certification'] == '청소년 관람불가' or cer['certification'] == '19':
                cer['certification'] = '18'
            c1 = Certification(pk=order_certi[cer['certification']], name=cer['certification'])
            c1.save()
            c1.movies.add(movie)
            break
    else:
        movie.delete()
        return
    path3 = path1 + '/watch/providers'
    params3 = {
        'api_key': API_KEY,
        'region' : 'KR',
        'language': 'ko',
    }    
    response3 = requests.get(BASE_URL+path3, params=params3)  
    data3 = response3.json()['results']
    if 'KR' in data3 and 'flatrate' in data3['KR']:
        for d3 in data3['KR']['flatrate']:
            f1 = OTT(pk=d3['provider_id'], name=d3['provider_name'])
            f1.save()
            f1.movies.add(movie)

    path4 = path1 + '/keywords'
    params4 = {
        'api_key': API_KEY,
    }
    response4 = requests.get(BASE_URL+path4, params=params4)
    data4 = response4.json()['keywords']
    for d4 in data4:
        k1 = Keyword(pk=d4['id'], name=d4['name'])
        k1.save()
        k1.movies.add(movie)

    path5 = path1 + '/credits'
    params5 = {
        'api_key': API_KEY,
        'language': 'ko',
    }
    response5 = requests.get(BASE_URL+path5, params=params5)
    data5_cast = response5.json()['cast']
    data5_cast_cut = data5_cast[:5]
    for cast in data5_cast_cut:
        a1 = Actor(pk=cast['id'], name=cast['original_name'])
        a1.profile_path = cast['profile_path'] or ''
        a1.save()
        a1.movies.add(movie)
    data5_crew = response5.json()['crew']
    for crew in data5_crew:
        if crew['job'] == 'Director':
            d1 = Director(pk=crew['id'], name=crew['original_name'])   
            d1.save()
            d1.movies.add(movie)

    return render(request, 'movies/id.html')

def movieids(request):
    lst = [75780, 614917, 198663, 338952, 116745, 286217, 338953, 150540, 177677, 299534, 383498, 299536, 299537, 384018, 482321, 508943, 99861, 508947, 587792, 313369, 166426, 19995, 333339, 449563, 508442, 13855, 537116, 476669, 497698, 585245, 587807, 122917, 508965, 615457, 623135, 631843, 290859, 45612, 526896, 429617, 76338, 100402, 244786, 76341, 351286, 8247, 58, 343611, 11324, 324668, 520763, 491584, 628802, 118340, 27205, 482373, 74, 587, 550988, 77, 431693, 475215, 363088, 594, 603, 604, 605, 138843, 354912, 419430, 385128, 259693, 335983, 602223, 68721, 496243, 343668, 118, 68726, 448119, 157820, 316029, 435841, 227973, 751237, 329865, 210577, 524434, 120467, 495764, 106646, 604822, 157336, 336026, 155, 12444, 12445, 671, 672, 673, 674, 675, 11423, 13475, 252067, 321697, 522402, 64682, 688301, 422576, 460465, 821427, 464052, 617653, 44214, 723640, 414906, 1726, 41154, 505026, 423108, 509635, 512195, 606402, 399566, 83666, 597208, 330457, 624860, 664291, 135397, 1255, 406759, 436969, 1771, 539885, 474350, 661231, 628466, 315635, 259316, 634649, 132344, 346364, 566525, 8960, 771, 772, 271110, 82695, 400650, 581389, 782, 72976, 591120, 87827, 453395, 531219, 280, 301337, 354072, 527641, 11036, 285, 293660, 370172, 400157, 504608, 619803, 763164, 379686, 212778, 568620, 435506, 228150, 206647, 487734, 353081, 776503, 537915, 568124, 77117, 254781, 320, 511809, 30018, 70981, 228165, 1865, 277834, 823625, 576845, 530254, 110415, 454992, 458576, 512340, 424277, 207703, 372058, 283995, 269149, 11104, 72545, 387426, 85350, 1895, 359784, 186729, 438631, 466282, 24428, 517991, 294254, 611179, 54138, 57212, 49026, 577922, 109445, 105864, 580489, 1930, 567690, 278927, 459151, 32657, 435601, 446354, 284052, 284053, 242582, 284054, 369557, 745881, 10138, 763285, 706972, 527774, 260513, 177572, 475557, 845222, 37799, 126889, 335787, 549294, 258480, 116149, 274870, 425909, 503736, 514999, 337339, 27582, 374720, 434119, 636360, 471498, 336843, 420814, 10191, 420817, 420818, 10195, 76757, 10198, 406997, 301528, 615904, 398818, 454626, 696806, 451048, 448491, 752623, 102899, 571891, 337401, 337404, 76285, 72190]

    for l in lst:
        BASE_URL = 'https://api.themoviedb.org/3'
        id = str(l)
        path1 = '/movie/' + id
        params1 = {
            'api_key': API_KEY,
            'language': 'ko',
            'append_to_response': 'releases',
        }
        response1 = requests.get(BASE_URL+path1, params=params1)
        data1 = response1.json()
        movie = Movie()
        movie.pk = id
        movie.title = data1['title']
        movie.original_title = data1['original_title']
        if data1['overview'] == '':
            return
        movie.overview = data1['overview']
        movie.poster_path = data1['poster_path']
        if data1['release_date'] == '':
            return
        movie.release_date = data1['release_date']
        movie.runtime = data1['runtime']
        movie.vote_average = data1['vote_average']
        movie.vote_count = data1['vote_count']
        
        path2 = path1 + '/videos'
        params2 = {
            'api_key': API_KEY,
            'language': 'ko',
        }    
        response2 = requests.get(BASE_URL+path2, params=params2)  
        data2 = response2.json()['results']
        
        for d2 in data2:
            movie.video = ''
            if d2['type'] == 'Trailer' or d2['official'] == True:
                movie.video = d2['key']
                break
        if movie.video == '':
            return
        movie.save()

        genres = data1['genres']
        for genre in genres:
            g1 = Genre(pk=genre['id'], name=genre['name'])
            g1.save()
            g1.movies.add(movie)

        certifi = data1['releases']['countries']
        for cer in certifi:
            if cer['iso_3166_1'] == 'KR' and cer['certification'] != '':
                if cer['certification'] == '전체관람가':
                        cer['certification'] = 'ALL'
                if cer['certification'] == '12세 이상 관람가' or cer['certification'] == '12세 관람가' or cer['certification'] == '12세이상관람가':
                    cer['certification'] = '12'
                if cer['certification'] == '15세 이상 관람가':
                    cer['certification'] = '15'
                if cer['certification'] == '청소년 관람불가' or cer['certification'] == '19':
                    cer['certification'] = '18'
                c1 = Certification(pk=order_certi[cer['certification']], name=cer['certification'])
                c1.save()
                c1.movies.add(movie)
                break
        else:
            movie.delete()
            return
        path3 = path1 + '/watch/providers'
        params3 = {
            'api_key': API_KEY,
            'region' : 'KR',
            'language': 'ko',
        }    
        response3 = requests.get(BASE_URL+path3, params=params3)  
        data3 = response3.json()['results']
        if 'KR' in data3 and 'flatrate' in data3['KR']:
            for d3 in data3['KR']['flatrate']:
                f1 = OTT(pk=d3['provider_id'], name=d3['provider_name'])
                f1.save()
                f1.movies.add(movie)

        path4 = path1 + '/keywords'
        params4 = {
            'api_key': API_KEY,
        }
        response4 = requests.get(BASE_URL+path4, params=params4)
        data4 = response4.json()['keywords']
        for d4 in data4:
            k1 = Keyword(pk=d4['id'], name=d4['name'])
            k1.save()
            k1.movies.add(movie)

        path5 = path1 + '/credits'
        params5 = {
            'api_key': API_KEY,
            'language': 'ko',
        }
        response5 = requests.get(BASE_URL+path5, params=params5)
        data5_cast = response5.json()['cast']
        data5_cast_cut = data5_cast[:5]
        for cast in data5_cast_cut:
            a1 = Actor(pk=cast['id'], name=cast['original_name'])
            a1.profile_path = cast['profile_path'] or ''
            a1.save()
            a1.movies.add(movie)
        data5_crew = response5.json()['crew']
        for crew in data5_crew:
            if crew['job'] == 'Director':
                d1 = Director(pk=crew['id'], name=crew['original_name'])   
                d1.save()
                d1.movies.add(movie)
    return render(request, 'movies/ids.html')


@api_view(['GET'])
def index(request):
    keyword_list = ['2343', '9840', '180547', '18035', '12565','4344']
    keyword = random.choice(keyword_list)
    movies = Movie.objects.filter(keywords=keyword).order_by('?')[:10]    
    serializer = MovieMainListSerializer(movies,many=True)  
    return Response(serializer.data)
    # random으로 뽑힌 keyword id 값 넣어주는거 고민해보기


@api_view(['GET'])
def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)


@api_view(['POST'])
def my_movie(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    user = request.user
    if movie.users_mymovie.filter(pk=user.pk).exists():
        movie.users_mymovie.remove(user)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    else:
        movie.users_mymovie.add(user)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)


@api_view(['POST'])
def wish(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    user = request.user
    if movie.users_wish.filter(pk=user.pk).exists():
        movie.users_wish.remove(user)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    else:
        movie.users_wish.add(user)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)


@api_view(['GET'])
def recommend_otts(request, ott_id):
    movies = Movie.objects.filter(otts=str(ott_id)).order_by('?')[:5]    
    serializer = MovieMainListSerializer(movies,many=True)  
    return Response(serializer.data)


@api_view(['GET'])
def recommend_directors(request, director_id):
    movies = Movie.objects.filter(directors=str(director_id)).order_by('?')[:5]  
    serializer = MovieMainListSerializer(movies,many=True)  
    return Response(serializer.data)


@api_view(['GET'])
def recommend_keywords(request, keyword_id):
    movies = Movie.objects.filter(keywords=str(keyword_id)).order_by('?')[:5]
    serializer = MovieMainListSerializer(movies,many=True)  
    return Response(serializer.data)


@api_view(['POST'])
def create_comment(request, movie_id):
    user = request.user
    movie = get_object_or_404(Movie, pk=movie_id)
    
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie, user=user)
        reviews = movie.reviews.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT', 'DELETE'])
def comment_detail(request, movie_id, review_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    review = get_object_or_404(Review, pk=review_id)

    if request.method == 'PUT':
        if request.user == review.user:
            serializer = ReviewSerializer(instance=review, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                reviews = movie.reviews.all()
                serializer = ReviewSerializer(reviews, many=True)
                return Response(serializer.data)

    elif request.method == 'DELETE':
        if request.user == review.user:
            review.delete()
            reviews = movie.reviews.all()
            serializer = ReviewSerializer(reviews, many=True)
            return Response(serializer.data)