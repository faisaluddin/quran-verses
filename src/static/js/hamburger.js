const hamburger = document.querySelector("#menu");
const hamburgerContent = document.querySelector(".sidenav");
const closeNavButton = document.querySelector("#closeNav");
const modal = document.querySelector(".modal");
const subscribe = document.querySelector(".subscribe");
const registerButton = document.querySelector("#register-btn");
const modalForm = document.querySelector("#modal-form");
const subscribeMessage = document.querySelector(".subscribe-strip");
const failedMessage = document.querySelector(".failed-message");
const sendEmail = document.querySelector(".submit-email");
const feedbackForm = document.querySelector(".feedback-form");
const closeModal = document.querySelector("#close");

function loadHamburgerEvents() {
  hamburger.addEventListener("click", toggleMenu);
  subscribe.addEventListener("click", subscribeModal);
  closeNavButton.addEventListener("click", toggleMenu);
  modalForm.addEventListener("submit", registerUser);
  closeModal.addEventListener("click", hide);
  document.addEventListener("keyup", closeModalOnEscape);
  if (feedbackForm) feedbackForm.addEventListener("submit", sendFeedback);
}

function toggleMenu() {
  document.querySelector("#menu").classList.toggle("change");
  document.querySelector(".sidenav").classList.toggle("change");
}

function closeModalOnEscape(e) {
  if (e.key === "Escape") hide();
}

function subscribeModal() {
  show(modal);
}

function show(elem) {
  elem.classList.add("is-visible");
  document.body.style.overflow = "hidden";
}

function hide() {
  modal.classList.remove("is-visible");
  document.body.removeAttribute("style");
}

function registerUser(e) {
  e.preventDefault();
  let formdata = new FormData(modalForm);
  let csrftoken = document.querySelector("[name=csrfmiddlewaretoken]").value;
  fetch("/subscribe/", {
    method: "POST",
    headers: { "X-CSRFToken": csrftoken },
    body: formdata,
  }).then(response => {
    if (response.ok) {
      subscribeMessage.style.display = "block";
      setTimeout(() => {
        hide();
        subscribeMessage.style.display = "none";
        modalForm.reset();
      }, 3000);
    } else {
      failedMessage.style.display = "block";
      setTimeout(() => {
        failedMessage.style.display = "none";
        modalForm.reset();
      }, 3000);
    }
  });
}

function sendFeedback(e) {
  e.preventDefault();
  let formdata = new FormData(feedbackForm);
  let csrftoken = document.querySelector("[name=csrfmiddlewaretoken]").value;
  fetch("/sendfeedback/", {
    method: "POST",
    headers: { "X-CSRFToken": csrftoken },
    body: formdata,
  }).then(response => {
    if (response.ok) {
      setTimeout(() => {
        feedbackForm.reset();
      }, 3000);
    } else {
      setTimeout(() => {
        feedbackForm.reset();
      }, 3000);
    }
  });
}

loadHamburgerEvents();
