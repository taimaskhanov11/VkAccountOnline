// for (let i = 1; i < 18; i++) {
//     let cat = `#cat-${i}`
//     let child = `#cat-${i}-child`
//     $(cat).click(function () {
//         $(child).toggle()
//     })
// }


const categoryList = []


$.getJSON(`/api/categorys/`, function (data) {

    let answer = data;
    categoryList.push(data.results)
    console.log(data.next)

})
console.log(categoryList)


// const categoryList =
//     $.ajax({
//         type: "GET",
//         url: '/api/categorys/',
//         // cache: false,
//         dataType: 'json',
//         success: function (response) {
//             console.log(response[0])
//         }})


// for (let category_pk = 1; category_pk <= {{ category_list.count }}; category_pk++) {
//     let but = `btn-input-{{ category_pk }}-{{ input_pk }}`
//     let inp = `form-input-{{ category_pk }}-{{ input_pk }}`
//     console.log(child)
//     //$(but).click(function () {
//      //   $(child).toggle()
//     //})
// }

