




for (let i = 1; i < 18; i++) {
    let cat = `#cat-${i}`
    let child = `#cat-${i}-child`
    // console.log($(cat).toggle())
    // console.log($(cat).style.display)

    $(cat).click(function () {
        // $(cat).style.display = ($(cat).style.display === null ) ? 'show' : 'hide';
        $(child).toggle()
    })

}

