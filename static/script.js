const form = document.querySelector("#form");
const input = document.querySelector("#input");
const fonts = document.querySelector("#fonts");
let sendInput = () => {
  const userInput = document.querySelector("[name=user-input]").value;
  const font = document.querySelector("[name=fonts").value;
  const csrf_token = document.querySelector("[name=csrf_token]").value;
  axios({
    method: "POST",
    url: "http://localhost:5000/",
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
};
input.addEventListener("input", sendInput, true);
fonts.addEventListener("change", sendInput, true);
