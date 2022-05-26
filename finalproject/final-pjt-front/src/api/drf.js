const HOST = 'http://localhost:8000/api/v1/'

const ACCOUNTS = 'accounts/'
const MOVIES = 'movies/'
const ARTICLES = 'community/'
const COMMENTS = 'comments/'

export default {
  accounts: {
    login: () => HOST + ACCOUNTS + 'login/',
    logout: () => HOST + ACCOUNTS + 'logout/',
    signup: () => HOST + ACCOUNTS + 'signup/',
    // Token 으로 현재 user 판단
    currentUserInfo: () => HOST + ACCOUNTS + 'user/',
    // username으로 프로필 제공
    profile: username => HOST + ACCOUNTS + 'profile/' + username,
  },
  movies: {
    movies: () => HOST + MOVIES,
    movie: movieId => HOST + MOVIES + 'movie/' +`${movieId}/`,
    myMovie: movieId => HOST + MOVIES + `${movieId}/` + 'mymovie/',
    wish: movieId => HOST + MOVIES + `${movieId}/` + 'wish/',
    otts: ottId => HOST + MOVIES + 'recommend/' + 'otts/' + `${ottId}/`,
    directors: directorId => HOST + MOVIES + 'recommend/' + 'directors/' + `${directorId}/`,
    keywords: keywordId => HOST + MOVIES + 'recommend/' + 'keywords/' + `${keywordId}/`,
    reviews: movieId => HOST + MOVIES + `${movieId}/` + 'create_comment/',
    review: (movieId, reviewId) => HOST + MOVIES + `${movieId}/` + 'comment_detail/' + `${reviewId}/`,
  },
  articles: {
    // /articles/
    articles: () => HOST + ARTICLES,
    // /articles/1/
    article: articleId => HOST + ARTICLES + `${articleId}/`,
    likeArticle: articleId => HOST + ARTICLES + `${articleId}/` + 'like/',
    comments: articleId => HOST + ARTICLES + `${articleId}/` + COMMENTS,
    comment: (articleId, commentId) =>
      HOST + ARTICLES + `${articleId}/` + COMMENTS + `${commentId}/`,
  },
}