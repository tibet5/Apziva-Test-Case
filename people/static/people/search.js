

const url = window.location.href
const searchForm = document.getElementById('search-form')
const searchInput = document.getElementById('search-input')
const results = document.getElementById('results')

const csrf = document.getElementsByName('csrfmiddlewaretoken')[0].value

sendSearchData = function(title) {
    console.log(title)
    params = title
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            // console.log(JSON.parse(this.response))
            res = JSON.parse(this.response)
            data = res.data
            console.log(data)
            results.innerHTML = ``
            data.forEach(people => {

                if (people.hireable == true){
                    hireable = `<i class="fas fa-check hireable">&nbsp;<span>Hireable</span></i>`
                }else if (people.hireable == false){
                    hireable = `<i class="fas fa-times not-hireable">&nbsp;<span>Not Hireable</span></i>`
                }else {
                    hireable = `<i class="fas fa-question null-hireable">&nbsp;<span>No Info About Hiring</span></i>`
                }
                
                results.innerHTML += 
                `
                <div class="card">
                <a class="card-title" data-toggle="collapse" href="#people_${people.pk}" role="button" aria-expanded="false" aria-controls="collapseExample">
                    <div class="card-body">
                        <div class="flex-card-inner">
                            <img class="avatar-image" src="${people.avatar_url}" alt="Avatar">
                            <div class="flex-title">
                                <h4>${people.name}</h4>
                                <p>${people.bio}</p>  
                            </div>   
                        </div>
                    </div>
                </a>
                    <div class="collapse" id="people_${people.pk}">
                        <div class="collapse-inner">
                                <a href="${people.user_url}">
                                    <img class="inner-logo-icon" src="/static/people/GitHub_Logo.png">
                                </a>
                                <a href="mailto:${people.e_mail}"><i class="fas fa-envelope"></i></a>
                                <i class="fas fa-map-marker-alt">&nbsp;<span>${people.location}</span></i>
                                ${hireable}
                        </div>
                    </div>
                </div>
                `
            });
            
        }
    }
    xhttp.open("POST", "res/", true);
    xhttp.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
    xhttp.setRequestHeader('X-CSRFToken', csrf);
    xhttp.send(params)
}


searchInput.addEventListener('keyup', e =>{
    sendSearchData(e.target.value)
})