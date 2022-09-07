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