//Requires JQuery to be loaded before this

//function to provide modular add-ons to onload event of every page
//Idea comes from https://errorsandanswers.com/add-multiple-window-onload-events/
//JQuery does not easily support event handler storage, so this hack with array

var onLoadFunctions = []
function executeOnLoad(fn_to_execute) {
    onLoadFunctions.push(fn_to_execute);   
}

$(function() {
    for(idx in onLoadFunctions) {
        onLoadFunctions[idx]()
    }
})


//General utility functions
function readCookie(name) {
    var nameEQ = name + "=";
    var ca = document.cookie.split(';');
    for (var i = 0; i < ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') c = c.substring(1, c.length);
        if (c.indexOf(nameEQ) == 0) {
            ret_str = c.substring(nameEQ.length, c.length);
            // console.log(ret_str);
            return ret_str;
        }
            
    }
    return null;
}


//This requires date.js
function formatDateForPostPreview(dta) {
    date_created = dayjs(dta);
    // console.log("Have date:")
    // console.log(date_created.format('DD-MMM-YYYY'))
    diff_date = dayjs().subtract(date_created)
    // console.log(diff_date.format('DD-MMM-YYYY'))
    // console.log(date_created.fromNow(true))

    return [
        date_created.format('DD-MMM-YYYY HH:MM (UTCZ)'),
        date_created.fromNow(true)
    ]
    // TODO: Move to joda.js for difference in datas
                    // https://js-joda.github.io/js-joda/manual/formatting.html
}//function formatDate(date) {


//Utility functions for comments

function addCommentHTML(parent_id, comment_text, 
        usr_photo_url, comment_date) {
    template = "Hello {{ name }}";

    old_html = $("#"+parent_id).html();
    // console.log(old_html)
    new_html = '<div class="col-1 align-self-end" style="text-align: center;">'+
                    '<img src="' + usr_photo_url + '" class="float-end rounded-circle" width="50px" heigth="40px" style="padding:5px">'+
                    '<small class="muted" style="font-size:9px; padding: 5px; margin: 2px;">'+ 
                        comment_date + 
                    '</small>'+
                '</div>'+
                '<div class="col-11" style="text-align: justify;">'+
                    comment_text + 
                '</div>';

    new_html = old_html+new_html;

    $("#"+parent_id).html(
        new_html
    );
};//function addCommentHTML(parent_id, comment_text, add_before = false) {

function registerPostCommentHandler(requestURL, 
            usr_photo_url, post_type, csrf_tok="EMPTY TOKEN!!") {
    $("#post_comment").click(
        
        function() {
            // console.log("CSRF token:"+csrf_tok);
            $.ajax({
                type: "POST",
                url: requestURL,
                data : {
                    comment_text : $("#post_comment_text").val(),
                    post_type : post_type, 
                    csrfmiddlewaretoken: csrf_tok,

                },
                datatype: 'json',
                success : function(data) {
                    addCommentHTML(
                        parent_id = "old-comments-row", 
                        comment_text = $("#post_comment_text").val(),
                        usr_photo_url = usr_photo_url,
                        comment_date = (new Date()).toLocaleDateString(
                            'en-us', 
                            {   weekday:"long", 
                                year:"numeric", 
                                month:"short", 
                                day:"numeric"
                            }
                        ) //comment_date = 
                    );
                    $("#post_comment_text").val("")
                    // console.log(data)
                },//success : function(data) {
                error : function(xhr,status,error) {
                    // console.log("AJAX error occurred");
                    let notifier = new AWN() 
                    notifier.alert('Comment post failed.<br>Please login to post comments.');
                }
            });//$.ajax({
        }//function() {
    )//$("#post_comment").click(


}//function registerPostCommentHandler(requestURL) {

function getComments(requestURL, post_type) {
    // console.log("Have token:"+readCookie('csrftoken'))
    $.ajax({
        type: "GET",
        url: requestURL,
        data : {
            post_type : post_type, 
            csrfmiddlewaretoken: cross_fit_env.csrftoken,
            // csrfmiddlewaretoken : readCookie('csrftoken'),
        },
        success : function(data) {
            // console.log("Have comments:")
            // console.log(data)
            $("#old-comments-row").html("")
            for(comment in data) {
                // console.log(data[comment])

                img = "No photo"
                if( data[comment].author) {
                    img = data[comment].author.photo
                }

                addCommentHTML(
                    parent_id = "old-comments-row", 
                    comment_text = data[comment].comment_text,
                    usr_photo_url = img,
                    comment_date = (new Date(data[comment].date_created)).toLocaleDateString(
                                        'en-us', 
                                        {   weekday:"long", 
                                            year:"numeric", 
                                            month:"short", 
                                            day:"numeric"}
                                    ) //comment_date = 
                )
            }
        }//success : function(data) {
    });//$.ajax({
}//function getComments(requestURL) {
