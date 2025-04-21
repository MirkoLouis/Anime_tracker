This is my final project to a subject.

**Roadmap -The progress-**

* The Database creation
* Updated the database with 5 records per table.
* Started to create the website with my friend who knows about html
* used ai to create website1
* did not undeertsnad most of it
* gave up on website1 but liked the design and decided to follow the same theme
* started creation of website2
* satisfied with the design so i started to connect it to database
* after a day still failed to connect to database
* started creation of 222 with the foundation being database connection
* finally managed to connect html to database
* started to move elements from website2 to 222
* anime table from database can now populate the homepage
* added image_url column to anime table in database to add pictures to animes
* started to implement register and login
* spent 2 days with nothing
* found 7 part video
* finished 6/7 and found that the rest will are on his website
* atleast we finally managed to insert new users to the user table
* transfer resources from 222 to project created from the 7 part video
* transferred anime fetchers to new project
* made scroll bar always visible to avoid the elements to shift towards the left when it is visible
* created spotlight animes section below green header
* only showed one anime in the spotlight section
* after two days and 10 ai queries fixed to loop through all spotlight animes
* fixed new animes section layout in 2 days
* started to implement login authentication system
* its working after a couple of hours
* new problem found - infinite login
* tried to fix, it says that it cant access jwt token
* infinite login fixed
* wanted to start implementing the watchlist on the user dashboard and found new problem
* cannot properly send jwt user data to html that supposedly contains display_name
* display name fixed
* logout button changing the navbar size fixed, also maximized the space used by spotlight animes
* found new annoying layout thing,spotlight animes in dashboard and spotlight animes in home heights are not the same
* added watchlist
* added watchlist adding not dynamic YET
* added watchlist status editing dynamic
* added watchlist removing dynamic
* added search function, redirects user to another route
* remade search function to stay in homepage, hides all anime sections when displaying results
* all that's left now is cleaning up
* finally made adding an anime dynamic by making the watchlist creator into a proper renderwatchlist function
* added a favicon to the site thanks to the people in this thread https://stackoverflow.com/questions/15463199/how-to-set-custom-favicon-in-express
* managed to get the local website deployed using port forwarding
* i got some friends to try out my website first with the 25 animes i directly inserted from the database
* since most of my images were in 4k they werent loading in their devices, website sizing was also an issue
* added compression dependency and immediately halved the loading process
* friend's mentioned a few problems and i live fixed them
* another friend mentioned a text overlapping issue which after a few minutes was fixed thanks to the guys from here https://stackoverflow.com/questions/15909489/text-overflow-ellipsis-on-two-lines
* added search filtering using tag, studio or rating currently works but it should update page numbers and prev/next buttons to remember the filter because what if more than 51 animes were passing the filter they'd need to be on a second page
* fixed the search filtering it now remembers the tags and changes the page numbers accordingly
* researching lazy loading
* implemented lazy loading using library, worked somehow but not for all images so scrapped
* deployed my website online to test native lazy loading, it works for the most part, not all sections show up immediately, new, upcoming and featured sections do work immediately so thats good
* seen the shifting issue first hand damn it looks so obvious, fixed it same day
* deployed with 9765 animes didn't take too long to load, the randomizer was the one that took a hit i think its because it randomizing through the whole 9765 animes
* and now we address the database issue, before one tag to one anime relationship which shouldn't have been
* added anime_tags table to be middle man between anime and its multiple tags
* updated all anime endpoints to work with the new anime table and anime_tags table
* updated search js function to work with the updated endpoint
