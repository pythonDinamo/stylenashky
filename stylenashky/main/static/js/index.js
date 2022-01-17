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

function phoneNumberFormatter() {
    let target = event.target;
    const formattedInputValue = formatPhoneNumber(target.value);
    target.value = formattedInputValue;
}


const phoneInputName = 'user_tel';
var phoneInputFields = document.getElementsByName(phoneInputName);

for(var i = 0; i < phoneInputFields.length; i++) {
    phoneInputFields[i].addEventListener('keydown', function() {phoneNumberFormatter()});
    phoneInputFields[i].addEventListener('keyup', function() {phoneNumberFormatter()});
}
