$(document).ready(function () {
	var form = $('#gallery-comment-form');
	var url = form.attr('action');
	if (form) {
		var formchanged = false;
		var statustext = $('<span id="ajax-status" class="status"></span>');
		statustext.clear = function () {
			statustext.text('').removeClass('success').removeClass('error');
		}
		statustext.success = function () {
			statustext.text('Saved.').addClass('success').removeClass('error');
		}
		statustext.error = function () {
			statustext.text('Failed to save.').addClass('error').removeClass('success');
		}
		form.append(statustext);
		form.append('<input type="hidden" name="ajax" value="true" />');
		form.find('.submit-button').hide();

		var commentbox = form.find('#comment-box');
		var minHeight = commentbox.prop('clientHeight');
		var resizeCommentBox = function () {
			commentbox.height(''); // reset the height so we can get the correct scroll height
			commentbox.height(Math.max(minHeight, commentbox.prop('scrollHeight')))
		}
		resizeCommentBox();

		form.keydown(function (event) {
			statustext.clear();
			formchanged = true;
			resizeCommentBox();
		});
		form.submit(function (event) {
			event.preventDefault();
			var formchanged = false;
			statustext.clear();
			$.ajax(url, {
				method: "POST",
				data: form.serialize(),
				success: function () { statustext.success(); },
				error: function () { statustext.error(); formchanged = true; }
			});
		});
		jQuery(window).bind('beforeunload', function(e) {
			statustext.clear();
			if (formchanged) {
				$.ajax(url, {
					method: "POST",
					data: form.serialize(),
					async: false // wait for the response before continuing (we don't actually care about the response, but this seems necessary to even send it in Firefox)
				});
			}
		});
	}
});