document.addEventListener('DOMContentLoaded', function(){

    // BUTTON LOGIN
    const send = document.getElementById('send');
    send.onclick = function() {
        if (this.value !== 'login') {
           return;
        }
        const email = document.getElementById('email');
        const password = document.getElementById('password');
        const entry = {
            email: email.value,
            password: password.value,
        }
        login(entry);
    };
});


// API FOR USER LOGIN
function login(entry) {
    fetch(`${window.origin}/api/login`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            },
        body: JSON.stringify(entry)
    })
    .then((response) => response.json())
    .then(response => {
        if (response.hasOwnProperty('template')) {

            // Populate task list
            document.getElementById('wrapper').innerHTML = response.template;

            // Add logout button
            const header = document.querySelector('header');
            header.innerHTML = '<a href="/logout" class="black-btn">Log out</a>'

            // Add onclick event to li
            const tasks = document.getElementsByClassName('task-id');
            let tasksLength = tasks.length;
            for (let i = 0; i < tasksLength; i++) {
                tasks[i].onclick = function() {
                    showTask(this.dataset.id)
                }
            }
        }
        else {

            // Return error message to the user
            const myForm = document.getElementById('form-cnt');
            let cssClass = 'error-message';
            const errorMessage = createMessage(response.message, cssClass)
            myForm.appendChild(errorMessage)
        } 
    })
    .catch(err => console.log(err))
}

// Show single task
function showTask(entry) {
    fetch(`${window.origin}/api/task`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            },
        body: JSON.stringify(entry)
    })
    .then((response) => response.json())
    .then(response => {

        // Selct body and append div with single note
        const body = document.querySelector('body');
        const noteWrapper = document.createElement('div')
        
        noteWrapper.classList.add('note-wrapper')
        noteWrapper.innerHTML = response.template;
        body.appendChild(noteWrapper);

        let closeBtn = document.getElementById('close');
        closeBtn.onclick = function() {
            noteWrapper.remove();
        }

    })
    .catch(err => console.log(err))
}


//Create messages
function createMessage(text, cssClass) {
    const messageContainer = document.createElement('div');
    const message = document.createElement('p');
    messageContainer.appendChild(message);
    
    messageContainer.classList.add(cssClass);

    message.innerHTML = text;
    return messageContainer;
}