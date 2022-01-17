let headerburger = document.querySelector('.header__burger');
    headerburger.addEventListener('click', showMenu);

function showMenu(){
    let menuNav = document.querySelector('.header__menu');

    headerburger.classList.toggle('active');
    menuNav.classList.toggle('active');
}


function formatPhoneNumber(value) {
    if (!value) return value;
    const phoneNumber = value.replace(/[^\d\+]/g, '');
    const phoneNumberLength = phoneNumber.length;
    if (phoneNumberLength < 7) return phoneNumber;
    if (phoneNumberLength < 12) {
      return `${phoneNumber.slice(0, 4)}(${phoneNumber.slice(4, 6)})${phoneNumber.slice(6)}`;
    }
   return `${phoneNumber.slice(0, 4)}(${phoneNumber.slice(4, 6)})${phoneNumber.slice(6, 9)}-${phoneNumber.slice(9, 11)}-${phoneNumber.slice(11, 13)}`;
}

function phoneNumberFormatter(elementId) {
    const inputField = document.getElementById(elementId);
    const formattedInputValue = formatPhoneNumber(inputField.value);
    inputField.value = formattedInputValue;
}

const phoneInputId = 'id_user_tel';
const phoneInputField = document.getElementById(phoneInputId);
phoneInputField.addEventListener('keydown', function() {phoneNumberFormatter(phoneInputId)});
phoneInputField.addEventListener('keyup', function() {phoneNumberFormatter(phoneInputId)});