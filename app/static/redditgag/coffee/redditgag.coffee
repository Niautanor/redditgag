blocking = false
done = false
last = null

requestJSON = () ->
  # only once.
  if blocking or done
    return

  blocking = true

  # add loading animation
  $("#loading-animation").addClass "jawn"

  # generate the JSON request
  query = "?#{if last? then "after=#{last}&" else ''}content_type=json"
  response = $.getJSON query
  .done (data) ->
    last = data.last
    @response =
      posts : data.posts
      print_subreddit : data.print_subreddit
    console.log "success"
  .fail (jqxhr, textStatus, error) ->
    reload_href = "javascript:location.reload()"
    @response =
      posts : [{
        kind : 'SORRY',
        sorrytext : "There was an error when accessing the redditgag API (Error #{error} with status #{textStatus}). You could try <a href=\"#{reload_href}\">reloading</a> the page.",
        author : 'redditgag',
        subreddit : 'redditgag',
        title : 'Something went wrong',
        original_url : reload_href,
        num_comments : 0,
        permalink : reload_href,
        hidden : null,
        provider_icon : false,
        provider_name : 'Error',
      }]
      print_subreddit : true

    done = true
    console.log "error"
  .always () ->
    console.log "thingamajig"
    content = Handlebars.templates.posts @response

    $(".post-container").append content

    # cleanup
    # remove loading animation
    $("#loading-animation").removeClass "jawn"

    blocking = false


$(window).scroll () ->
  if $(window).scrollTop() >= $(document).height()- $(window).height()
    # set api request and load more content
    do requestJSON

# init page
$(document).ready requestJSON
