- front end issues (javascript)
  - medium priority
    - [ ] lazy loading (loading embeddables only when the user scrolls to them)
    - [ ] make videos autoplay (and loop) when the user scrolls to them
      the page)
  - low priority
    - [ ] add a javascript guided tour of the site
  - fixed
    - [x] auto loading (load new content when the user scrolls to the bottom of
- front end issues (template)
  - high priority
    - [ ] add an original-link button that contains the original url
  - medium priority
    - [ ] empty self posts currently display "None" in the text area. Ideally, they
      would indicate that there is no text there.
    - [ ] general prettiness
  - low priority
    - [ ] add subreddit selector to navbar (allow selecting show\_nsfw there)
      - make sure that the url is nsfw=<eggplant emoji>
  - fixed
    - [x] allow toggling the show\_nsfw parameter
    - [x] mark or hide nsfw posts
    - [x] put the navbar into its own template and include it on all pages
    - [x] figure out if django supports template inheritance and maybe use that too
- providers
  - medium priority
    - [ ] proper parameter support for youtube (timestamps, playlists)
    - [ ] imgur album support
- general back end
  - low priority
    - [ ] gather run time statistics of unembeddable things and display them on
      the about page.
      - this can be implemented very easily with a dictionary in providers.sorry
        since I already extract the domain name from the url
    - [ ] reddit login to up and downvote and have personalized front page
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
  - fixed
    - [x] finish imgur and gfycat providers
    - [x] pagination (currently we can only display the top 25 results)
    - [x] just generally more info from the post like name of OP and subreddit
