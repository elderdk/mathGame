let userBlock = document.querySelectorAll('.userBlock')

userBlock.forEach(block => {
  block.addEventListener("click", b => {
    document.querySelector("#user").value = block.innerHTML
  })
})