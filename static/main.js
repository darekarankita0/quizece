//Login via ajax request. Rather than loading a whole new page a small template will be sent back if it passes authentication. 
// That is what is generally happening in all of these functions. They are turning a multi-page
// app into a single page app with nice animations. 
$(document).ready(function() {
    $(document).on("click", "#login_btn", function(e) {
        e.preventDefault();
        var url = "js_login";
        $.ajax({
            type: "POST",
            url: url,
            data: $("#login_form").serialize(), // serializes the form"s elements.
            //The animation is set for a smooth transition.
            success: function(response) {
                $("#results").fadeOut(400);
                setTimeout(function() { $("#results").html(response); }, 300);
                $("#results").fadeIn(400);
            },
            error: function(error) {
                console.log("Not Working");
            }
        });
    });
    // Function for submitting an answer to a quiz question. 
    $(document).on("click", "#submit_btn", function(e) {
        e.preventDefault();
        var url = "js_submit_answer";
        $.ajax({
            type: "POST",
            url: url,
            data: $("#submit_answer_form").serialize(), // serializes the form"s elements.
            //The animation is set for a smooth transition to the next question or error message.
            success: function(response) {
                $("#results").fadeOut(400);
                setTimeout(function() { $("#results").html(response); }, 300);
                $("#results").fadeIn(400);
            },
            error: function(error) {
                console.log("Not Working");
            }
        });
    });
    // Function for skipping a quiz question. 
    $(document).on("click", "#skip_btn", function(e) {
        e.preventDefault();
        var url = "js_skip_question";
        $.ajax({
            type: "POST",
            url: url,
            //The animation is set for a smooth transition to the next question 
            success: function(response) {
                $("#results").fadeOut(400);
                setTimeout(function() { $("#results").html(response); }, 300);
                $("#results").fadeIn(400);
            },
            error: function(error) {
                console.log("Not Working");
            }
        });
    });
    // Function for loading the leaderboard when user is not logged in.
    $(document).on("click", "a#leaderboard", function(e) {
        e.preventDefault();
        var url = "js_leaderboard_no_login";
        $.ajax({
            type: "GET",
            url: url,
            //The animation is set for a smooth transition.
            success: function(response) {
                $("#results").fadeOut(400);
                setTimeout(function() { $("#results").html(response); }, 300);
                $("#results").fadeIn(400);
            },
            error: function(error) {
                console.log("Not Working");
            }
        });
    });
});
