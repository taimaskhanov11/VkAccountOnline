const fieldsCount = document.getElementById('fields-count')
const buttonText = document.getElementById('button-text')
const searchingType = document.getElementById('searching-text')

const searchButton = document.getElementById('search-button')
const searchForm = document.getElementById('search-form')

// console.log(searchFields)
let fieldsNames = []


// const searchInput = document.getElementById('search-input')
// searchInput.addEventListener('keydown', function (event) {
//     console.log(event)
//     if (event.key === 'Enter') {
//         searchForm.submit();
//     }
// })


// searchButton.addEventListener('click', function () {
//     searchForm.submit();
// })


for (let i = 1; i <= fieldsCount.textContent; i++) {
    let field = document.getElementById(String(i))
    fieldsNames.push(field.textContent)

    field.addEventListener('click', function () {
        console.log(i)
        buttonText.textContent = field.textContent
        searchingType.value = i
    })
    // searchFields[i] = searchFields[i].length;
    // console.log(searchFields[i])
}


// searchFields.forEach(function (item) {
//     item.addEventListener('click', function () {
//         console.log(item)
//
//         })
//
// })


//
//
// searchField.addEventListener('click', function () {
//     console.log(searchField.textContent)
// })
