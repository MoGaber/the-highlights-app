const saveBtn = document.getElementById("save-btn")
const downloadBtn = document.getElementById("download-btn")

saveBtn.addEventListener("click", function(){
console.log(window.getSelection().toString())
})
downloadBtn.addEventListener("click", function(){
console.log(window.getSelection().toString())
})