## For the near future

- [ ] add an original-link button that contains the original url
- [x] just generally more info from the post like name of OP and subreddit
- [ ] finish imgur and gfycat providers
  - [x] since imgur and gfycat both require api's to get all the information, I
    first have to implement some kind of caching system

## For the not quite so near future

- [x] ~~find a markdown renderer and add support for self posts~~
  - This was unneccessary because the reddit api already provides rendered html
- [ ] propper parameter support for youtube (timestamps, playlists)
- [ ] add a javascript guided tour of the site
- [ ] pagination (currently we can only display the top 25 results)
- [ ] lazy loading (loading embeddables only when the user scrolls to them)

## For the really not anywhere near near future

- [ ] reddit login to up and downvote and have personalized frontpage
- [ ] support other sorting methods beside best (e.g. new, top)
- [ ] rethink the caching thing
  - The background here is that most of the providers will work with the same
    schema:
    1. use a regex to extract an id from a given url and to remove unneeded
       stuff (like extra parameters, file extensions, etc)
    2. use an external api to retrieve the object with the extracted id
    3. use the retrieved object to get embeddable info
  - Since more than one link can link to a certain object, it might make sense
    to cache the results of the api accesses (instead of the whole url ->
    embeddable conversion like it is now)
