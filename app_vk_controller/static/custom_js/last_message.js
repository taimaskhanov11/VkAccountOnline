// $('.form-check-label').click(function () {
//     console.log('click');
//
//     var link = $(this).attr('href');
//
//     $.get(link, function (r) {
//         console.log(r);
//         document.getElementById("pook").innerHTML = "Новый текст!";
//     });
//     return false;
// });
// todo

// document.getElementById("pook_send").onclick = function () {
//     document.getElementById("my_form").submit();
// }

// window.onload = function () {
//
//     var link = $(this).attr('href');
//
//     $.get(link, function (r) {
//         let myForm = document.getElementById("my_form").submit()
//         console.log(r);
//         console.log(myForm);
//
//         document.getElementById("account-data").innerHTML = myForm;
//     });
//     return false;
// }


// window.onload = function () {
//     while (true) {
//         setTimeout(() => {
//             $.ajax({
//                 type: "GET",
//                 url: '/account-data',
//                 success: function (response) {
//                     console.log(response)
//                     $('#account-data').html(response);
//                 },
//             });
//         }, 2000);
//
//     }
// }

// function sleep2(ms) {
//     return new Promise(resolve => setTimeout(resolve, ms));
// }
//
// function sleep(ms) {
//     ms += new Date().getTime();
//     while (new Date() < ms) {
//     }
// }


// Пауза в течение 3 секунд

// Код для запуска после паузы


// const t = window.setInterval(function () {
//     if (!isPaused) {
//
//     }
// }, 1000);

// function start() {
//     // started = setInterval(doStuff, 1000);
//     // clearInterval(started);
//     // return
//
//     if (!isPaused) {
//         var started = setInterval(doStuff, 1000);
//
//     } else {
//         clearInterval(started);
//         isPaused = false;
//         isPaused = true;
//     }

// let second = 1000;
// setTimeout(() => doStuff(), 1000);
// second += 2000
// requestAnimationFrame(doStuff);

// }

// function pauseBrowser(millis) {
//     var date = Date.now();
//     var curDate = null;
//     do {
//         curDate = Date.now();
//     } while (curDate - date < millis);
// }


// $('#my_form3').click(
//     function () {
//         isPaused = !isPaused;
//         // let my_interval = 1000
//         while (true) {
//             pauseBrowser(2000)
//             if (!isPaused) {
//                 doStuff()
//             }
//         }
//     }
// );

let isPaused = true;

const $account = $('#account-data');
// const $loadingButton = $('#loading-status')
const $loadingButton = $('#my_form')

$account.onload = doStuff;
// $account.ready(function () {
//     doStuff();
// });

// $(window).load(doStuff);


function getAccount(url) {
    $.getJSON(url, function (data) {
        console.log(url)
        }
    )
}


function doStuff() {
    // Код для запуска перед паузой

    $.ajax({
        type: "GET",
        url: '/api/messages',
        // cache: false,
        dataType: 'json',

        success: function (response) {
            console.log(response)
            let data = response['results']
            // let obj = JSON.parse(response);
            // console.log(data['messages'])
            let result = [];
            // let $account = document.getElementById('account-data')
            $account.empty()
            // sleep(2000)
            let second = 0;
            // for (let account in data) {
            data.forEach(function (message) {
                getAccount(message)
                console.log(message, 'message')
                message['messages'].forEach(function (message) {
                    console.log(message)
                    let tr = document.createElement('tr')
                    let td1 = document.createElement('td')
                    let txt2 = document.createTextNode(message['account']);
                    td1.appendChild(txt2)
                    tr.appendChild(td1)
                    // await new Promise(r => setTimeout(r, 1000));
                    // sleep(2000)

                    let td2 = document.createElement('td')
                    let txt3 = document.createTextNode(message['user']);
                    td2.appendChild(txt3)
                    tr.appendChild(td2)
                    // await new Promise(r => setTimeout(r, 1000));
                    // sleep(2000)


                    let td3 = document.createElement('td')
                    let txt4 = document.createTextNode(message['text']);
                    td3.appendChild(txt4)
                    tr.appendChild(td3)
                    // await new Promise(r => setTimeout(r, 1000));
                    // sleep(2000)

                    let td4 = document.createElement('td')
                    let txt5 = document.createTextNode(message['answer_question']);
                    td4.appendChild(txt5)
                    tr.appendChild(td4)
                    // await new Promise(r => setTimeout(r, 1000));

                    let td5 = document.createElement('td')
                    let txt6 = document.createTextNode(message['answer_template']);
                    td5.appendChild(txt6)
                    tr.appendChild(td5)
                    // await new Promise(r => setTimeout(r, 1000));

                    let td6 = document.createElement('td');
                    let lab = document.createElement('label');
                    lab.classList.add('badge', 'badge-danger')
                    let txt7 = document.createTextNode('Pending');
                    lab.appendChild(txt7)
                    td6.appendChild(lab)
                    tr.appendChild(td6)
                    // await new Promise(r => setTimeout(r, 1000));

                    // setTimeout(() => {  console.log("World!"); }, 2000);
                    // sleep(2000).then(() => { console.log("мир"); });
                    // await new Promise(r => setTimeout(r, second));
                    // setTimeout(() => {$account.append(tr); }, second);
                    setTimeout(() => {
                        if (!isPaused) {
                            $account.prepend(tr);
                        }
                    }, second);
                    second += 500
                    console.log('запись')
                    // $account.append(tr);

                })
            })

        },
    })
}

// <button type="submit" className="btn btn-primary mb-2">Submit</button>

function loadingButton() {
    let loadButton = document.createElement('button');
    loadButton.classList.add('btn', 'btn-primary', 'mb-2');
    let text = document.createTextNode('Submit');
    loadButton.appendChild(text);
    loadButton.setAttribute('type', 'submit');
    loadButton.setAttribute('id', 'loading-status');
    $('#loading-status').replaceWith(loadButton)
    return loadButton;
}

function loadingIcon() {
    // let data = '<object type="text/html" data="../../../templates/_inc/_loading_icons/_style1.html" ></object>'

    $loadingButton.load("/static/custom_html/_style1.html")
    console.log('LOADING')
    // document.getElementById("loading-status").innerHTML=data;
    // document.getElementById("content").innerHTML =
    //     '<object type="text/html" data="../../../templates/_inc/_loading_icons/_style1.html" ></object>';
}


let intR;
// clearInterval(myInterval);
$loadingButton.click(
    function () {
        isPaused = !isPaused;
        let my_interval = 6000

        loadingIcon()
        // return //todo
        if (!isPaused) {
            clearInterval(intR)
            intR = setInterval(function () {
                // my_interval += 1000
                loadingButton()
                if (!isPaused) {
                    loadingButton()
                    doStuff()
                } else {
                    console.log('уничтожение')
                    clearInterval(intR)
                }
            }, my_interval)
        }


    }
);


// setInterval(function() {
//     $.ajax({
//         url: '/path_to/ls.php',
//         type: 'POST',
//         dataType: 'json',
//         data: {userPrivMess: uid}, // Если личные данные вытаскиваются для определенного юзверя
//         success: function(data){
//             // data - сформированный ответ на стороне сервера
//             $("#update_ls").text('Обновление: ' + data);
//         }
//     });
// }, 1000);