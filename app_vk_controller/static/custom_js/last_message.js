let isPaused = true;

const $message = $('#message-data');
const $loadingButton = $('#my_form')
const nowMessages = []


function getAccount(id) {
    $.getJSON(`/api/accounts/${id}/`, function (data) {
            console.log(id)
        }
    )
}

function getUser(id) {
    return $.getJSON(`/api/users/${id}/`)
}

function splitByIndex(value, index) {
    let length = value.length
    // let stringLength = length / index
    // console.log(length)
    let endSting = '';
    for (var i = 0; i < length; i += index) {
        // console.log(i)
        // let preEnd = index + i
        // if (preEnd < length) {
        //     endSting += value.substring(i, index + i) + '<br>'
        // } else {
        //     endSting += value.substring(i, index + i)
        //
        // }
        endSting += value.substring(i, index + i) + '<br>'

    }
    return endSting
}


const accounts = {}
const users = {}


function getName(type, id) {
    $.getJSON(`/api/${type}/${id}/`, function (data) {
        if (type === 'users') {
            users[id] = data['first_name']
        } else {
            accounts[id] = data['first_name']
            console.log('ПОЛУЧЕН')
        }

    })
}


function createMessageElement(message_data) {
    let tr = document.createElement('tr');
    // tr.classList.add("my-class");
    let td1 = document.createElement('td');
    let p1 = document.createElement('p')

    let account = message_data['account']
    let user = message_data['user']
    // console.log(typeof account_id)

    console.log('POOOK')
    // let txt2 = document.createTextNode(account_id);
    let txt2 = document.createTextNode(account['first_name']);
    let a2 = document.createElement('a')
    a2.setAttribute('href', `/vk-accs/${account['id']}`)
    a2.appendChild(txt2)

    p1.appendChild(a2);
    td1.appendChild(p1);
    tr.appendChild(td1);


    // user
    let td2 = document.createElement('td');
    let txt3 = document.createTextNode(user['first_name']);
    // td2.appendChild(txt3);
    let a3 = document.createElement('a')
    a3.setAttribute('href', `/vk-users/${user['id']}`)
    a3.appendChild(txt3)
    td2.appendChild(a3)
    tr.appendChild(td2);


    let x = 0,
        y = 16;


    //text
    let td3 = document.createElement('td');
    let span3 = document.createElement('span');
    span3.classList.add('span-text');
    // let txt4 = document.createTextNode(messageText);
    let txt4 = document.createTextNode(message_data['text'].substring(x, y) + '...');
    // span3.innerHTML = splitByIndex(message['text'], 40);
    // span3.innerHTML= message['text']
    let a4 = document.createElement('a')
    span3.appendChild(txt4);

    a4.setAttribute('href', `/messages/${message_data['id']}`)
    a4.appendChild(span3)
    td3.appendChild(a4);
    tr.appendChild(td3);


    //answer
    let td4 = document.createElement('td');
    let txt5 = document.createTextNode(message_data['answer_question'].substring(x, y) + '...');
    // let txt5 = document.createTextNode(message['answer_question']);
    td4.appendChild(txt5);

    // td4.innerHTML = splitByIndex(message['answer_question'], 40)

    tr.appendChild(td4);
    // await new Promise(r => setTimeout(r, 1000));


    //template
    let td5 = document.createElement('td');
    // let txt6 = document.createTextNode(message['answer_template']);
    let txt6 = document.createTextNode(message_data['answer_template'].substring(x, y) + '...');
    td5.appendChild(txt6);

    // td5.innerHTML = splitByIndex(message['answer_template'], 40)

    tr.appendChild(td5);
    // await new Promise(r => setTimeout(r, 1000));


    //status
    let td6 = document.createElement('td');
    let lab = document.createElement('label');
    console.log(user)
    let blocking = !user['blocked'] ? ['success', 'Активен'] : ['danger', 'Заблокирован'];
    lab.classList.add('badge', `badge-${blocking[0]}`)
    // lab.classList.add('badge', 'badge-danger')
    let txt7 = document.createTextNode(blocking[1]);
    lab.appendChild(txt7);
    td6.appendChild(lab);
    tr.appendChild(td6);


    //time
    let td7 = document.createElement('td');
    // let txt8 = document.createTextNode(message['sent_at']);
    let date = new Date(message_data['sent_at']);
    let txt8 = document.createTextNode(date.toLocaleString());
    let span8 = document.createElement('span')
    span8.classList.add('date-time')
    span8.appendChild(txt8)
    td7.appendChild(span8)
    tr.appendChild(td7);


    return tr
}


function doStuff() {
    // Код для запуска перед паузой

    $.ajax({
        type: "GET",
        url: '/api/messages/',
        // cache: false,
        dataType: 'json',

        success: function (response) {
            console.log(response)
            let data = response['results']
            data.reverse()
            let result = [];
            let second = 0;
            // for (let account in data) {
            data.forEach(function (message_data) {

                if (nowMessages.includes(message_data['id'])) {
                    return
                }
                nowMessages.push(message_data['id'])
                let tr = createMessageElement(message_data);
                second += 500;
                $message.prepend(tr);
                console.log('запись2');

            })
        }
    })
}

// <button type="submit" className="btn btn-primary mb-2">Submit</button>
const $helpMessage = $('#help-message');
const aMessage = 'Для обновления в реальном времени нажмите Start.';
const bMessage = 'Автообновление включено. Для остановки нажмите Stop.';

function loadingButton(mini_text = null) {
    console.log('LOADING Button');
    let button_text = mini_text;
    let color = (isPaused) ? 'success' : 'danger';
    let true_sign = (isPaused) ? 'mdi-play' : 'mdi-stop';
    let helpMessage = (isPaused) ? aMessage : bMessage;
    if (!mini_text) {
        button_text = (isPaused) ? 'Start' : 'Stop';
    }

    let loadButton = document.createElement('button');
    // loadButton.classList.add('btn', 'btn-primary', 'mb-2');
    loadButton.classList.add('btn', `btn-outline-${color}`, 'btn-icon-text');

    //sign
    let i = document.createElement('i');
    // sign.classList.add('ti-reload', 'btn-icon-prepend')
    i.classList.add('mdi', true_sign, 'menu-icon');


    let text = document.createTextNode(button_text);
    loadButton.appendChild(i);
    loadButton.appendChild(text);
    loadButton.setAttribute('type', 'submit');
    loadButton.setAttribute('id', 'loading-status');
    $('#loading-status').replaceWith(loadButton);

    $helpMessage.text(helpMessage);
    return loadButton;
}

function loadingIcon() {
    // let data = '<object type="text/html" data="../../../templates/_inc/_loading_icons/_style1.html" ></object>'

    $loadingButton.load("/static/custom_html/_style1.html");
    console.log('LOADING Icon');
    // document.getElementById("loading-status").innerHTML=data;
    // document.getElementById("content").innerHTML =
    //     '<object type="text/html" data="../../../templates/_inc/_loading_icons/_style1.html" ></object>';
}


document.addEventListener('DOMContentLoaded', function () {
    loadingButton();
    doStuff();

})

let intR;

function startLoadMessage() {
    let my_interval = 6000;

    loadingButton();
    if (!isPaused) {
        doStuff();
        clearInterval(intR);
        intR = setInterval(function () {
            if (!isPaused) {
                doStuff();
            } else {
                console.log('уничтожение');
                clearInterval(intR);
            }
        }, my_interval);
    }
}

$loadingButton.click(
    function () {
        isPaused = !isPaused;
        loadingIcon();
        // return //todo
        setTimeout(startLoadMessage, 1000);

    }
);

