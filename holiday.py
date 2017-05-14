def holiday(work):
    html_header = """
    <!doctype html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <!-- SEO -->
        <title>{}</title>
        <meta name="description" content="{}, by {}">

        <!-- URL CANONICAL -->
        <!-- <link rel="canonical" href="http://your-url.com/"> -->

        <!-- Google Fonts -->
        <link href="https://fonts.googleapis.com/css?family=Roboto:100,100i,300,300i,400,400i,700,700i%7CMaitree:200,300,400,600,700&amp;subset=latin-ext" rel="stylesheet">

        <!-- CSS Base -->
        <link rel="stylesheet" type='text/css' media='all' href="static/css/base.css">

        <!-- CSS Colors -->
        <link rel="stylesheet" type='text/css' media='all' href="static/css/colors.css">

        <!-- Optional - CSS SVG Icons (Font Awesome) -->
        <link rel="stylesheet" type='text/css' media='all' href="static/css/svg-icons.css">

        <!-- SOCIAL CARDS (ADD YOUR INFO) -->

        <!-- FAVICONS -->
        <link rel="shortcut icon" sizes="16x16" href="static/images/favicons/unisworks.png">

        <!-- Android -->
        <meta name="mobile-web-app-capable" content="yes">
        <meta name="theme-color" content="#333333">

        <!--<style>-->
        <!--  @import url('https://fonts.googleapis.com/css?family=Nothing+You+Could+Do');-->
        <!--</style>-->
        <link href="https://fonts.googleapis.com/css?family=Inconsolata" rel="stylesheet">
        <link href="https://fonts.googleapis.com/css?family=Nothing+You+Could+Do" rel="stylesheet">
        <link href="https://fonts.googleapis.com/css?family=Roboto+Condensed" rel="stylesheet">
        <link href="https://fonts.googleapis.com/css?family=Maitree" rel="stylesheet">

      </head>
      <body>

        <main role="main">
          <article id="webslides" class="">
            <!-- Quick Guide
              - Each parent <section> in the <article id="webslides"> element is an individual slide.
              - Vertical sliding = <article id="webslides" class="vertical">
              - <div class="wrap"> = container 1200px / <div class="wrap size-50"> = 600px;
            -->

    """
    header = html_header.format(work['title'], work['title'], work['author'])
    #header = html_header % (work['title'], work['title'])
    
    html_quote = """
            <section class="bg-black-blue">
              <span class="background dark" style="background-image:url('{}')"></span>
              <!--.wrap = container 1200px -->
              <div class="wrap">
                <blockquote class="wall">
                  <p class="fadeIn slow">{}
                  </p>
                  <p class="fadeInUp slow"><cite>{}</cite></p>
                </blockquote>
              </div>
              <!-- .end .wrap -->
            </section>
            
    """
    if work['quoteImage'].startswith('http') or work['quoteImage'].startswith('static'):
      img_url = work['quoteImage']
    else: # use unsplash otherwise
      img_url = "https://source.unsplash.com/" + work['quoteImage'] + '/'
    
    quote = html_quote.format(img_url, work['quote'], work['quoteAuthor'])
    #quote = html_quote % (work['quoteImage'], work['quote'], work['quoteAuthor'])
    
    html_title = """
            <section class="bg-white fullscreen">
              <div class="card-50">
                <figure>
                  <img src="{}" alt="stars">
                </figure>
                <!-- end figure-->
                <div class="flex-content aligncenter">
                  <img class="aligncenter img.size-30 zoomIn" src="{}" alt="author" width="100">
                  <br/>
                  <br/>
                  <br/>
                  <h4 class="fadeIn"><strong>{}</strong>
                  </h4>
                  <p class="text-intro fadeIn">{}
                  </p>
                  <h5 class="fadeInUp slow"><br/><b>{}</b></h5>
                </div>
                <!-- end .flex-content-->
              </div>
            </section>
            
    """
    if work['titleImage'].startswith('http') or work['titleImage'].startswith('static'):
      img_url = work['titleImage']
    else: # use unsplash otherwise
      img_url = "https://source.unsplash.com/" + work['titleImage'] + '/'
    
    title = html_title.format(img_url, work['authorPhoto'], work['title'], work['date'], work['author'])
    #title = html_title % (work['titleImage'], work['authorPhoto'], work['title'], work['date'], work['author'], work['patreon'])

    
    #html_text = """
    #        <section class="bg-black-blue">
    #          <span class="background dark" style="background-image:url('{}')"></span>
    #          <div class="wrap content-center">
    #                <h3 class="fadeInUp slow">
    #                  {}
    #                </h3>
    #          </div>
    #        </section>
    #"""
    
    html_text = """
            <section class="bg-white fullscreen">
              <div class="card-50">
                <figure>
                  <img src="{}" alt="stars">
                </figure>
                <!-- end figure-->
                <div class="flex-content aligncenter">
                  {}
                </div>
                <!-- end .flex-content-->
              </div>
            </section>
    """
    if work['textImage'].startswith('http') or work['textImage'].startswith('static'):
      img_url = work['textImage']
    else: # use unsplash otherwise
      img_url = "https://source.unsplash.com/" + work['textImage'] + '/'
      
    # create a new slide for every paragraph
    text = ""
    for p in work['text']:
      text += html_text.format(img_url, p)
      
    #text = html_text.format(work['text'])
    #text = html_text % (work['text'])
    
    html_thanks = """
            <section class="slide-middle">
              <span class="background-left-top dark" style="background-image:url('')"></span>
              <div class="wrap">
                <div class="content-right text-serif">
                  <h2  class="fadeIn slow">
                    <strong>Thanks </strong>
                    <svg class="fa-heart-o" style="color:red">
                        <use xlink:href="#fa-heart-o"></use>
                    </svg>
                  </h2>
                  <p>
                    Please contact me!</p>
                  <p style="font-family:'Nothing You Could Do', cursive;" class="fadeInUp slow">
                    <a href="mailto:{}">
                    <svg class="fa-reply-all" style="color:red">
                        <use xlink:href="#fa-reply-all"></use>
                    </svg>
                    {}
                    </a>
                  </p>
                </div>
                <!-- .end .content-right -->
              </div>
              <!-- .end .wrap -->
            </section>
    """
    #thanks = html_thanks.format(work['email'], work['author'])
    thanks = ""
    
    html_end = """
            </article>
          <!-- end article -->
        </main>
        <!-- end main -->

        <script src="static/js/svg-icons.js"></script>
        <script src="static/js/webslides.js"></script>
        <script>
          window.ws = new WebSlides({ changeOnClick: true });
        </script>

        <!-- OPTIONAL - svg-icons.js (fontastic.me - Font Awesome as svg icons) -->
        <script defer src="static/js/svg-icons.js"></script>

      </body>
    </html>
    """
    end = html_end
    
    #html_final_work = html_header + html_title + html_quote + html_text + \
    #                  html_thanks + html_end
    final_work = header + title + quote + text + thanks + end
    
    return final_work
    
    
