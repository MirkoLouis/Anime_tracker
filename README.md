This is my final project to a subject.

Data Flow Works like this:

Database contains:
User Table
Anime Table
Watchlist Table
Tags Table
Anime Tags Table
Studio Table

app.js contacts Database using the library mysql2 (at first I used mysql) for:
Animes:
  Each of these have their own endpoint (idk specifically but its where they end up in the website, it is possible to go to visit this endpoint and see raw data)
    spotlight animes
    new and upcoming animes
    most watchlist animes
    featured animes
    random animes
User Specific Watchlist:
  Each of these have their own endpoint
    User specific Watchlist anime with status 'Watching' or 'Plan to Watch'
    User specific Watchlist anime with status 'Completed'
Search Query:
  When query is empty get all animes
  When query has a value find it according to the anime title

animefetcher javascript fetches the data from the endpoint to create:
  function Spotlights
  function NewAnimes
  function UpcomingAnimes
  function MostWatchlistAnimes
  function RecommendedAnimes
  function Random Animes

since the html is connected to the animefetcher javascript it gets dynamicaly populated by the functions and uses specified containers inside the html

When html receives the data expected it renders the anime cards.

That's the basic data flow.
