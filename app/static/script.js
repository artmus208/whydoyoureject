const menuLinks = document.querySelectorAll('.menu .menu__list-link')
const pathname = document.location.pathname

if (menuLinks && pathname != '/') {
  menuLinks.forEach(item => {
    const href = item.getAttribute('href')
    if (href.includes(pathname)) item.classList.add('active')
  })
}

const notification = document.querySelector('.notification')
const notificationImg = document.querySelector('.notification img')
if (notification && notification.classList.contains('have-notification')) {
  notification.setAttribute('href', '/reject-form')
  notificationImg.setAttribute('src', '/static/icon_message.svg')
}

