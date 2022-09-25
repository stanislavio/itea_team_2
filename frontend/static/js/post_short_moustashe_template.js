var short_post_html_template = `
        <div class="row text-start " style="margin:15px">
              <div class="col-1"></div>
              <div class="col-1 border-bottom text-center">
                <img src="{{imageURL}}" class="rounded-circle" alt="..." width="80px" heigth="60px">
                <p><a href="#" class="link-secondary">
                    {{userName}}
                  </a><br>
                  <small class="muted" style="font-size:9px;">
                    {{date_created}}
                  </small>
                </p>
              </div>
              <div class="col-9 border-bottom text-start">
                <a href="{{post_viewURL}}" class="link-dark">
                  <p class="lead">
                    {{post_title}}
                  </p>
                </a>
                <p class="text-start">
                  {{ post_text }}
                </p>
              </div>
            </div>
        </div>
    `;//short_post_html_template =

var short_running_post_html_template = `
    <div class="row text-start " style="margin:15px">
          <! -- Image and user name -->
          <div class="col-1"></div>
          <div class="col-1 border-bottom text-center me-3">
            <img src="{{imageURL}}" class="rounded-circle " alt="..." width="80px" heigth="60px">
            <p><a href="#" class="link-secondary">
                {{userName}}
              </a><br>
              <small class="muted" style="font-size:9px;" data-bs-toggle="tooltip" data-bs-placement="top" title="{{date_created_tooltip}}">>
                {{date_created}}
              </small>
            </p>
          </div>
          <! -- Title and post text -->
          <div class="col-9 border-bottom text-start">
            <div class="row">
              <div class="col-9">
                <a href="{{post_viewURL}}" class="link-dark">
                  {{post_title}}
                </a>
              </div>
              <div class="col-1">
                <img src="http://localhost:8000/frontend/static/img/template_types/running_post.png" width="32px" height="32px" />
                <!-- TODO: make image for running generation non textula - static URL -->
              </div>
              <div class="col-2">
                <small>Distance:{{total_km_ran}}</small>
              </div>
            </div>
            
            <p class="text-start">
              {{ post_text }}
            </p>
          </div>
        </div>
    </div>
`;//var short_running_post_html_template = `

var short_hiking_post_html_template = `
    <div class="row text-start " style="margin:15px">
          <! -- Image and user name -->
          <div class="col-1"></div>
          <div class="col-1 border-bottom text-center me-1">
            <img src="{{imageURL}}" class="rounded-circle " alt="..." width="80px" heigth="60px">
            <p><a href="#" class="link-secondary">
                {{userName}}
              </a><br>
              <small class="muted" style="font-size:9px;" data-bs-toggle="tooltip" data-bs-placement="top" title="{{date_created_tooltip}}">>
                {{date_created}}
              </small>
            </p>
          </div>
          <! -- Title and post text -->
          <div class="col-9 border-bottom text-start">
            <div class="row">
              <div class="col-7">
                <a href="{{post_viewURL}}" class="link-dark">
                  {{post_title}}
                </a>
              </div>
              <div class="col-1">
                <img src="http://localhost:8000/frontend/static/img/template_types/hiking_post.png" width="32px" height="32px" />
              </div>
              <div class="col-2">
                <small style="font-size:10px;" >Max. elevation:{{max_elevation}}</small>
              </div>
              <div class="col-2">
                <small style="font-size:10px;" >Distance:{{total_km_walked}}</small>
              </div>
            </div>
            <!-- Location -->
            <div class="row">
              <div class="col-12">
                Location: {{hike_location}}
              </div>
            </div>

            <div class="row">
              {{ post_text }}
            </div>
            
          </div>
        </div>
    </div>
`;//var short_running_post_html_template = `


function renderPostPreview(post) {
  img = post.author.photo;
  if(post.author.photo == null) {
      img = cross_fit_env.serviceImagesURLs.genericUser;
  }

  //post_view_URL = post_view_base_URL+post.id
  
  //TODO: add absolute creation date as tooltip to the date https://getbootstrap.com/docs/4.0/components/tooltips/
  
  post_view_URL = cross_fit_env.urls.createSocialPostURL+post.id

  if(post.post_type == 'training' | post.post_type == 'running') {
      post_view_URL = cross_fit_env.urls.createTrainingPostURL+post.id  
  }

  formatted_created_dates = formatDateForPostPreview(post.date_created);
  
  params = {
      imageURL : img,
      date_created : formatted_created_dates[1]+' ago',
      date_created_tooltip : formatted_created_dates[0],
      userName : post.author.username,
      post_title : post.post_title.slice(0, 70),
      post_text : post.post_text.slice(0, 300),
      post_viewURL : post_view_URL,
  };
  new_html = "Error in rendering mustashe"
  if(post.post_type == 'running') {
    params.total_km_ran = "NA"
    if(post.total_km_ran)
        params.total_km_ran = post.total_km_ran+" km";
    new_html = Mustache.render(short_running_post_html_template, params);
  }
  
  if(post.post_type == "hiking") {
    params.total_km_walked = post.total_km_walked+' km'
    params.hike_location = post.hike_location
    params.max_elevation = post.max_elevation+' m'
    
    new_html = Mustache.render(short_hiking_post_html_template, params);

  };
  if(post.post_type == "social" | post.post_type == "training") {
      new_html = Mustache.render(short_post_html_template, params);
  };
  return new_html
}//function renderPostPreview(post) {