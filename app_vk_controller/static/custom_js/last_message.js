let isPaused = true;

const $message = $('#message-data');
// const $loadingButton = $('#loading-status')
const $loadingButton = $('#my_form')

// $account.onload = doStuff;
// $account.ready(function () {
//     doStuff();
// });

// $(window).load(doStuff);


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
            // let obj = JSON.parse(response);
            // console.log(data['messages'])
            let result = [];
            // let $account = document.getElementById('account-data')
            // $message.empty()
            // sleep(2000)
            let second = 0;
            // for (let account in data) {
            data.forEach(function (message) {

                if (nowMessages.includes(message['id'])) {
                    return
                }


                // let user_data = getUser(message['user'])
                // // user_data = user_data['responseJSON'];
                // console.log('USER DATA', user_data);
                // user_data.done(function (user_data) {
                //     console.log('USER DATA', user_data['responseJSON']);
                // })

                $.getJSON(`/api/users/${message['user']}/`, function (user_data) {
                    console.log('USER DATA', user_data);
                    nowMessages.push(message['id']);
                    // getAccount(message);

                    console.log(message, 'message');

                    let tr = document.createElement('tr');
                    let td1 = document.createElement('td');
                    let txt2 = document.createTextNode(message['account']);
                    td1.appendChild(txt2);
                    tr.appendChild(td1);
                    // await new Promise(r => setTimeout(r, 1000));
                    // sleep(2000)

                    // user
                    let td2 = document.createElement('td');
                    let txt3 = document.createTextNode(user_data['name']);
                    td2.appendChild(txt3);
                    tr.appendChild(td2);

                    // await new Promise(r => setTimeout(r, 1000));
                    // sleep(2000)


                    let td3 = document.createElement('td');
                    let txt4 = document.createTextNode(message['text']);
                    td3.appendChild(txt4);
                    tr.appendChild(td3);
                    // await new Promise(r => setTimeout(r, 1000));
                    // sleep(2000)

                    let td4 = document.createElement('td');
                    let txt5 = document.createTextNode(message['answer_question']);
                    td4.appendChild(txt5);
                    tr.appendChild(td4);
                    // await new Promise(r => setTimeout(r, 1000));

                    let td5 = document.createElement('td');
                    let txt6 = document.createTextNode(message['answer_template']);
                    td5.appendChild(txt6);
                    tr.appendChild(td5);
                    // await new Promise(r => setTimeout(r, 1000));

                    let td6 = document.createElement('td');
                    let lab = document.createElement('label');
                    lab.classList.add('badge', 'badge-danger')
                    let txt7 = document.createTextNode('Pending');
                    lab.appendChild(txt7);
                    td6.appendChild(lab);
                    tr.appendChild(td6);
                    // await new Promise(r => setTimeout(r, 1000));

                    // setTimeout(() => {  console.log("World!"); }, 2000);
                    // sleep(2000).then(() => { console.log("мир"); });
                    // await new Promise(r => setTimeout(r, second));
                    // setTimeout(() => {$account.append(tr); }, second);

                    setTimeout(() => {
                        if (!isPaused) {
                            $message.prepend(tr);
                        }
                    }, second);
                    second += 500;
                    console.log('запись');
                    // $account.append(tr);

                })


            })

        },
    })
}

// <button type="submit" className="btn btn-primary mb-2">Submit</button>

function loadingButton(mini_text = null) {
    console.log('LOADING Button')
    let button_text = mini_text
    if (!mini_text) {
        button_text = (isPaused) ? 'Start' : 'Stop';
    }

    let loadButton = document.createElement('button');
    loadButton.classList.add('btn', 'btn-primary', 'mb-2');

    let text = document.createTextNode(button_text);
    loadButton.appendChild(text);
    loadButton.setAttribute('type', 'submit');
    loadButton.setAttribute('id', 'loading-status');
    $('#loading-status').replaceWith(loadButton)
    return loadButton;
}

function loadingIcon() {
    // let data = '<object type="text/html" data="../../../templates/_inc/_loading_icons/_style1.html" ></object>'

    $loadingButton.load("/static/custom_html/_style1.html")
    console.log('LOADING Icon')
    // document.getElementById("loading-status").innerHTML=data;
    // document.getElementById("content").innerHTML =
    //     '<object type="text/html" data="../../../templates/_inc/_loading_icons/_style1.html" ></object>';
}


// window.onload(setTimeout(function () {
//         doStuff()
//     }, 2000)
// );
document.addEventListener('DOMContentLoaded', function () {
    loadingButton()
})

let intR;

function startLoadMessage() {
    let my_interval = 6000

    loadingButton()
    if (!isPaused) {
        clearInterval(intR)
        intR = setInterval(function () {
            if (!isPaused) {
                doStuff()
            } else {
                console.log('уничтожение')
                clearInterval(intR)
            }
        }, my_interval)
    }
}

$loadingButton.click(
    function () {
        isPaused = !isPaused;
        loadingIcon()
        // return //todo
        setTimeout(startLoadMessage, 1000);

    }
);

