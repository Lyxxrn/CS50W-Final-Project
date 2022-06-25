var site = 'title';
function closeall() {
    var divs = document.getElementsByTagName('div')
    var elements = divs.length
    for(var i = 0;i < elements;i++){
       var divStyle = divs.item(i)
       if (!(divs.item(i) == document.getElementById('menu')))
       divStyle.style.display = 'none';
    }
    return;
}
function showOne(showme) {
    

    site = showme;
    var element = document.getElementById(showme)
    closeall()

    element.style.display = 'block';
    document.getElementById(showme).className = 'show';
}


function news() {

    showOne('news')

    let i = 0;
    fetch('/get_news')
    .then(response => response.json())
    .then(news => {
        let i = 0;
        const container = document.getElementById('news');

      news.forEach(function(news){

        //create new divs
        i++;
        let newDiv = document.createElement('div');

        //set attributes
        newDiv.className = 'news'
            newDiv.innerHTML = 
            `
            <a href="news_view/${news.title}">
                <h2>${news.title}</h2>
                <a>
                    Veröffentlicht: ${news.time}
                </a>
            </a>
            `;

            container.appendChild(newDiv);
        })
    })
}

function events() {

    showOne('events')

    let i = 0;
    fetch('/get_events')
    .then(response => response.json())
    .then(events => {
        let i = 0;
        const container = document.getElementById('events');

      events.forEach(function(events){

        //create new divs
        i++;
        let newDiv = document.createElement('div');

        //set attributes
        newDiv.className = 'events'
            newDiv.innerHTML = 
            `
            <h2>${events.title}</h2>
            <a>
                Am: ${events.date} <br>
            </a>
            <a>
                ${events.describtion}
            </a>
            `;

            container.appendChild(newDiv);
        })
    })
}

//same functions but for editing objects

function edit_news() {

    showOne('news')

    let i = 0;
    fetch('/get_news')
    .then(response => response.json())
    .then(news => {
        let i = 0;
        const container = document.getElementById('news');

      news.forEach(function(news){

        //create new divs
        i++;
        let newDiv = document.createElement('div');

        //set attributes
        newDiv.className = 'news'
            newDiv.innerHTML = 
            `
            <a href="news_edit/${news.title}">
                <h2>${news.title}</h2>
                <a>
                    Veröffentlicht: ${news.time}
                </a>
            </a>
            `;

            container.appendChild(newDiv);
        })
    })
}

function edit_events() {

    showOne('events')

    let i = 0;
    fetch('/get_events')
    .then(response => response.json())
    .then(events => {
        let i = 0;
        const container = document.getElementById('events');

      events.forEach(function(events){

        //create new divs
        i++;
        let newDiv = document.createElement('div');

        //set attributes
        newDiv.className = 'events'
            newDiv.innerHTML = 
            `
            <a href="event_edit/${events.title}">
                <h2>${events.title}</h2>
                <a>
                    Am: ${events.date} <br>
                </a>
                <a>
                    ${events.describtion}
                </a>
            </a>
            `;

            container.appendChild(newDiv);
        })
    })
}