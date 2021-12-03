function splitByIndex(value, index) {
    let length = value.length
    // let stringLength = length / index
    console.log(length)
    let endSting = '';
    for (var i = 0; i < length; i += index) {
        console.log(i)
        endSting += value.substring(i, index + i) + '\n'
    }
    return endSting
}

let answer = 'вы можете вспомнить substring принимает индексы,' +
    ' как и еще один способ извлечения строк, фрагмент.'

res = splitByIndex(answer, 30)

console.log(res)

