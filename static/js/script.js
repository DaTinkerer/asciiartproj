const input = document.querySelector("#input");
const fonts = document.querySelector("#fonts");
const art = document.querySelector("#art");
const copyBtn = document.querySelector("#copy-btn");
let debounce = (cb, delay = 1000) => {
  let timeout;
  return (...args) => {
    clearTimeout(timeout);
    timeout = setTimeout(() => {
      cb(...args);
    }, delay);
  };
};

let sendInput = debounce(() => {
  const userInput = document.querySelector("[name=user-input]").value;
  const font = document.querySelector("[name=fonts").value;
  const csrf_token = document.querySelector("[name=csrf_token]").value;
  axios({
    method: "POST",
    url: "http://localhost:5000",
    headers: { "X-CSRFToken": csrf_token, "Content-Type": "application/json" },
    data: { userInput: userInput, font: font },
  })
    .then((response) => {
      res = response.data["art"];
      document.querySelector("#art").textContent = res;
    })
    .catch((err) => {
      console.log(err);
    });
}, 300);

let copyArt = () => {
  navigator.clipboard.writeText(art.textContent);
  copyBtn.textContent = "Copied!";
  setTimeout(() => {
    copyBtn.textContent = "Copy Art";
  }, 1500);
};
input.addEventListener("input", sendInput, true);
fonts.addEventListener("change", sendInput, true);
copyBtn.addEventListener("click", copyArt);
