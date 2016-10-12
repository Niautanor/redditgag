var blocking = false;
var last = null;

function requestJSON() {
	// only once.
	if(blocking) {
		return;
	}
	blocking = true;

	// add loading animation
	$("#loading-animation").addClass("jawn");

	// generate the JSON request
	var response = $.getJSON('?' + ((last != null)? 'after=' + last + '&': '') + 'content_type=json', function() {
		console.log("success");
	})
	.fail(function() {
		console.log("error");
	})
	.done(function() {
		var response_data = response.responseJSON;
		last = response_data['last'];
    content = Handlebars.templates.posts({
      posts : response_data.posts,
      print_subreddit : response_data.print_subreddit,
    });
    $(".post-container").append(content);

		//cleanup
		// remove loading animation
		$("#loading-animation").removeClass("jawn");

		blocking = false;
	});
}


$(window).scroll(function () {
	console.log($(window).scrollTop() + " " + $(document).height()- $(window).height())
	if($(window).scrollTop() >= $(document).height()- $(window).height()) {
		// set api request and load more content
		requestJSON();
	}
});

// init page
$(document).ready(requestJSON());
