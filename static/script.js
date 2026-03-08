const btnDesktop = document.getElementById("temabtn");
const btnMobile = document.getElementById("temabtn-mobile");

function alternarTema() {
  document.body.classList.toggle("dark");

  if (document.body.classList.contains("dark")) {
    localStorage.setItem("tema", "dark");
  } else {
    localStorage.setItem("tema", "light");
  }
}

btnDesktop.addEventListener("click", alternarTema);
btnMobile.addEventListener("click", alternarTema);

window.addEventListener("load", () => {
  const temaSalvo = localStorage.getItem("tema");

  if (temaSalvo === "dark") {
    document.body.classList.add("dark");
  }
});
