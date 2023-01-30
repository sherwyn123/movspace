import streamlit as st

def app():
    st.title('Movie Recommender Lite');

    import streamlit.components.v1 as components  # Import Streamlit

    # Render the h1 block, contained in a frame of size 200x200.
    components.html('''
    <!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Movie App</title>
    
    <style>
 @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@200;400;700&display=swap');

        *{
            box-sizing: border-box;
        }
   
      :root{
        --primary-color:#000000;
        --secondary-color:#b00000;
      }
      body{
          background-color: var(--primary-color);
          font-family: "hoppins","sans-serif";
          margin: 0;
      }
      header{
          padding: 1rem;
          display: flex;
          justify-content: flex-end;
          background-color: var(--secondary-color);
      }
      .search{
          background-color: white;
          border: 2px solid var(--primary-color);
          padding: 0.5rem 1rem;
          border-radius: 50px;
          font-size: 1rem;
          color:#000;
          font-family: inherit;
      }

      .search:focus{
          outline: 0;
          background-color: white;
      }
      .search::placeholder{
          color: #7378c5;
      }
      main{
          display: flex;
          flex-wrap: wrap;
          justify-content: center;

      }
      .movie{
          width:300px;
          margin:1rem;
          border-radius: 3px;
          box-shadow: 0.2px 4px 5px rgba(0,0,0,0.1);
          background-color: var(--secondary-color);
          position: relative;
          overflow: hidden;
      }
      .movie img{
          width: 100%;
      }
      .movie-info{
          color: #eee;
          display: flex;
          align-items: center;
          justify-content: space-between;
          padding: 0.5rem 1rem 1rem;
          letter-spacing: 0.5px;
      }
      .movie-info h3{
          margin-top: 0; 
      }
      .movie-info span{
          background-color: var(--primary-color);
          padding:0.25rem 0.5rem;
          border-radius: 3px;
          font-weight: bold;
      }
      .movie-info span.green{
          color: lightgreen;
      }
      .movie-info span.oragne{
        color: orange;
    }
    .movie-info span.red{
        color: red;
    }
    .overview
    {
        position: absolute;
        left:0;
        right: 0;
        bottom:0;
        background-color: #fff;
        padding: 1rem;
        max-height: 100%;
        transform: translateY(101%);
        transition: transform 0.3s ease-in;
    }

    
.movie:hover .overview{
    transform: translateY(0);
}
#tags{
    width: 80%;
    display: flex;
    flex-wrap: wrap;
    justify-content:center;
    align-items:center;
    margin:10px auto;
}
.tag
{
    color: white;
    padding:10px 20px;
    background-color: orange;
    border-radius: 50px;
    margin:5px;
    display: inline-block;
    cursor:pointer
}
.tag.highlight
{
    background-color: tomato;
}
.no-results
{
   color:white ;
   text-decoration: underline;
}

</style>
</head>

<body>
    <header>
        <form id="form">
            <input type="text" placeholder="search" class="search" id="search">
        </form>
    </header>
    <div id="tags">
        <div class="tag">Action</div>
        <div class="tag">Adventure</div>
        <div class="tag">Drama</div>
        <div class="tag">Comedy</div>
    </div>
    <main id="main">
        <div class="movie">
            <img src="https://images.unsplash.com/photo-1518173835740-f5d14111d76a?ixid=MXwxMjA3fDB8MHxwa690by1wYWd1fHx8fGVufD88fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=877&q=80"
                alt="image">
    
            <div class="movie-info">
                <h3> Movie Title</h3>
                <span class="green">9.8</span>
            </div>
    
            <div class="overview">
                <h3>overview</h3>
                Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quis nam est, consequuntur doloremque quasi
                quaerat vpossimus eius pariatur, iusto numquam? Voluptatum culpa similique, qui debitis
                oluta ratione qui exercitationem blanditiis voluptatum autem voluptate voluptatem ipsam dolor,
                repudiandae illum culpa, excepturi porro deleniti quas, numquam vero odit reiciendis.
            </div>
        </div>
    
        <div class="movie">
            <img src="https://images.unsplash.com/photo-1518173835740-f5d14111d76a?ixid=MXwxMjA3fDB8MHxwa690by1wYWd1fHx8fGVufD88fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=877&q=80"
                alt="image">
    
            <div class="movie-info">
                <h3> Movie Title</h3>
                <span class="green">9.8</span>
            </div>
    
            <div class="overview">
                <h3>overview</h3>
                Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quis nam est, consequuntur doloremque quasi
                quaerat vpossimus eius pariatur, iusto numquam? Voluptatum culpa similique, qui debitis
                oluta ratione qui exercitationem blanditiis voluptatum autem voluptate voluptatem ipsam dolor,
                repudiandae illum culpa, excepturi porro deleniti quas, numquam vero odit reiciendis.
            </div>
        </div>
    

        <div class="movie">
            <img src="https://images.unsplash.com/photo-1518173835740-f5d14111d76a?ixid=MXwxMjA3fDB8MHxwa690by1wYWd1fHx8fGVufD88fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=877&q=80"
                alt="image">
    
            <div class="movie-info">
                <h3> Movie Title</h3>
                <span class="green">9.8</span>
            </div>
    
            <div class="overview">
                <h3>overview</h3>
                Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quis nam est, consequuntur doloremque quasi
                quaerat vpossimus eius pariatur, iusto numquam? Voluptatum culpa similique, qui debitis
                oluta ratione qui exercitationem blanditiis voluptatum autem voluptate voluptatem ipsam dolor,
                repudiandae illum culpa, excepturi porro deleniti quas, numquam vero odit reiciendis.
            </div>
        </div>
    
    </main>
 <script>

        //tmdb api key 
        const API_KEY='api_key=dad7b6ea7c596a86a77f9ce34a954055';
        const BASE_URL='https://api.themoviedb.org/3';
        const API_URL=BASE_URL+'/discover/movie?sort_by=popularity.desc&'+API_KEY;
        const IMG_URL='https://image.tmdb.org/t/p/w500';
        const searchURL=BASE_URL+'/search/movie?'+API_KEY;

        const genres = [
        {
          "id": 28,
          "name": "Action"
        },
        {
          "id": 12,
          "name": "Adventure"
        },
        {
          "id": 16,
          "name": "Animation"
        },
        {
          "id": 35,
          "name": "Comedy"
        },
        {
          "id": 80,
          "name": "Crime"
        },
        {
          "id": 99,
          "name": "Documentary"
        },
        {
          "id": 18,
          "name": "Drama"
        },
        {
          "id": 10751,
          "name": "Family"
        },
        {
          "id": 14,
          "name": "Fantasy"
        },
        {
          "id": 36,
          "name": "History"
        },
        {
          "id": 27,
          "name": "Horror"
        },
        {
          "id": 10402,
          "name": "Music"
        },
        {
          "id": 9648,
          "name": "Mystery"
        },
        {
          "id": 10749,
          "name": "Romance"
        },
        {
          "id": 878,
          "name": "Science Fiction"
        },
        {
          "id": 10770,
          "name": "TV Movie"
        },
        {
          "id": 53,
          "name": "Thriller"
        },
        {
          "id": 10752,
          "name": "War"
        },
        {
          "id": 37,
          "name": "Western"
        }
      ]
       
        const main=document.getElementById("main");
        const form=document.getElementById('form');
        const search=document.getElementById('search');
        const tagE1=document.getElementById('tags');

        var selectedGenre=[];
        setGenre();
        function setGenre()
        {
                tagE1.innerHTML='';
                genres.forEach(genre=>
                {
                        const t=document.createElement('div');
                        t.classList.add('tag');
                        t.id=genre.id;
                        t.innerText=genre.name;
                        t.addEventListener('click', () => {
                            if(selectedGenre.length == 0){
                                selectedGenre.push(genre.id);
                            }else{
                                if(selectedGenre.includes(genre.id)){
                                    selectedGenre.forEach((id, idx) => {
                                        if(id == genre.id){
                                            selectedGenre.splice(idx, 1);
                                        }
                                    })
                                }else{
                                    selectedGenre.push(genre.id);
                                }
                            }
                            console.log(selectedGenre)
                            getMovies(API_URL + '&with_genres='+encodeURI(selectedGenre.join(',')))
                            highlightSelection()
                        })
                        tagE1.append(t);
                })
        }
       function highlightSelection()
        {
            const tags=document.querySelectorAll('.tag');
            tags.forEach(tag=>
            {
                tag.classList.remove('highlight');
            })
            cleatBtn()
            if(selectedGenre.length!=0)
            {
            selectedGenre.forEach(id=>
            {
                    const highlightedTag=document.getElementById(id);
                    highlightedTag.classList.add('highlight');
            })
        }
        }
        function cleatBtn()
        {
            let my_clear_btn=document.getElementById('clear');
            if(my_clear_btn)
            {
                my_clear_btn.classList.add('highlight');
            }
            else
            {
            let btn=document.createElement('div');
            btn.classList.add('tag','highlight');
            btn.id='clear';
            btn.innerText='Clear X';
            btn.addEventListener('click',()=>
            {
                selectedGenre=[];
                setGenre();
                getMovies(API_URL);
            })
            tagE1.append(btn);
            }
        }
        getMovies(API_URL);

        function getMovies(url)
        {
            fetch(url).then(res=>res.json()).then(data=>
            { 
                console.log(data.results);
                if(data.results.length!==0)
                {
                showMovies(data.results);
                }
                else
                {
                    main.innerHTML='<h1 class="no-results">No Results Found</h1>'
                }
            })
        }
        function showMovies(data)
        {
            main.innerHTML = '';
            data.forEach(movie=>
            {
                const {title, poster_path, vote_average, overview} = movie;
                const movieE1=document.createElement('div');
                movieE1.classList.add('movie');
                movieE1.innerHTML= `
                <img src="${poster_path? IMG_URL+poster_path: "http://via.placeholder.com/1080x1580" }" alt="${title}">

            <div class="movie-info">
                <h3>${title}</h3>
                <span class="${getColor(vote_average)}">${vote_average}</span>
            </div>

            <div class="overview">
                <h3>overview</h3>
                ${overview}
                 </div>
`
main.appendChild(movieE1); 
            })
        }
        function getColor(vote)
        {
            if(vote>=8)
            {return "green";}
            else if(vote>=5)
            {return "orange";}
            else
            {return 'red';}
        }
      form.addEventListener('submit', (e)=>
      {
          e.preventDefault();
          const searchTerm=search.value;
          selectedGenre=[];
          highlightSelection();
          if(searchTerm)
          {
              getMovies(searchURL+'&query='+searchTerm);
          }
          else
          {
              getMovies(API_URL);
          }
      })
    </script>
</body>

</html>



'''
, width=1050, height=1900)
