const statusForm = document.getElementById('status-form');
const userStatusButton = document.getElementById('user-status-button');
const userDropdownName = document.getElementById('dropdown-name');
const sendFormButton = document.getElementById('send-form-button');
const statusInput = document.getElementById('status-input')

userDropdownName.addEventListener('click', function () {
    console.log(userStatusButton.textContent)
    status = userStatusButton.textContent.trim()
    if (status === 'Active') {
        userStatusButton.textContent = 'Blocked';
        userDropdownName.textContent = 'Active';
        // statusInput.checked = true;
        statusInput.value = 'True';
        userStatusButton.classList = 'btn btn-danger badge  btn-sm dropdown-toggle'

    } else {
        userStatusButton.textContent = 'Active';
        userDropdownName.textContent = 'Blocked';
        statusInput.value = 'False';
        // statusInput.checked = false;
        userStatusButton.classList = 'btn btn-success badge  btn-sm dropdown-toggle'
    }
    console.log( statusInput.checked)

});

sendFormButton.addEventListener('click', function () {
    statusForm.submit();
})



