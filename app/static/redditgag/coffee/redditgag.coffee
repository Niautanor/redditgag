blocking = false
last = null

requestJSON = () ->
  # only once.
  if blocking
    return

  blocking = true

  # add loading animation
  $("#loading-animation").addClass "jawn"

  # generate the JSON request
  query = "?#{if last? then "after=#{last}&" else ''}content_type=json"
  response = $.getJSON query, () ->
    console.log("success")
  .fail () ->
    console.log("error")
  .done () ->
    response_data = response.responseJSON
    last = response_data['last']
    content = Handlebars.templates.posts {
      posts : response_data.posts,
      print_subreddit : response_data.print_subreddit,
    }
    $(".post-container").append content

    # cleanup
    # remove loading animation
    $("#loading-animation").removeClass "jawn"

    blocking = false


$(window).scroll () ->
  if $(window).scrollTop() >= $(document).height()- $(window).height()
    # set api request and load more content
    requestJSON()

# init page
$(document).ready requestJSON
