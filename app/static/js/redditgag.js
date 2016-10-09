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
		response_data['posts'].forEach(function(post) {
			var content = '<div class="post ' + (post['hidden']? 'post-hidden' : '') + ' well">' +
							'<h2 class="title">';
			if(post['hidden']) {
				content += '<span class="hidden-marker">' +
								'[' + post['hidden'] + '] (hover to view)' +
								'</span>';
			}
			content += post['title'] +
						'</h2>' +
						'<div class="post-content">';
			if(post['kind'] == 'IMAGE') {
				content += '<img src="' + post['url'] +'" class="post-image" />';
			} else if(post['kind'] == 'VIDEO') {
				content += '<video autoplay loop muted controls>';
				post['sources'].forEach(function(source) {
					content += '<source type="' + source['mime'] + '" src="' + source['url'] + '" />';
				});
				content += '</video>';
			} else if(post['kind'] == 'IFRAME') {
				content += '<div class="aspect-ratio">' +
								'<iframe src="' + post['url'] + '" frameborder="0" allowfullscreen>' +
								'</iframe>' +
							'</div>';
			} else if(post['kind'] == 'TEXT') {
				content += '<div class="selftext">' +
								post['selftext'] + // | safe
								'</div>';
			} else if(post['kind'] == 'SORRY') {
				content += '<div class="sorry row">' +
								'<div class="sorry-image col-sm-12 col-md-3">' +
									'<img src="/static/img/sorry.svg" />' +
								'</div>' +
								'<div class="sorry-text col-sm-12 col-md-9">' +
									'<h6>Sorry</h6>' +
									'<p>' +
										post['sorrytext'] +
									'</p>' +
							'</div>' +
						'</div>';
			}
			content += '</div>' +
						'<div class="row things">' +
							'<small class="col-md-6">' +
							'submitted by <b>/u/' + post['author'] + '</b>' +
							(response_data['print_subreddit']? 'to <b>/r/' +  post['subreddit'] + '</b>' : '') +
							'</small>' +
							'<div class="col-md-6 text-right">' +
							'<a href="' + post['permalink'] + '">' +
								'<button type="button" class="btn btn-default">' +
									'<span class="glyphicon glyphicon-comment" aria-hidden="true"></span> ' + post['num_comments'] +
								'</button>' +
							'</a>' +
							'<a href="' + post['original_url'] + '">' +
								'<button type="button" class="btn btn-default">' +
									'<span class="glyphicon glyphicon-link" aria-hidden="true"></span> Source' +
								'</button>' +
							'</a>' +
							'</div>' +
						'</div>' +
					'</div>';
			$(".post-container").append(content);
		});

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
