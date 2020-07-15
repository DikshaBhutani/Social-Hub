var profile = document.querySelector(".profile");
var menu = document.querySelector(".menu");

$(".profile-pic , .username , .profile").click(function(event){
    event.stopPropagation();
    menu.style.display = "block";
})

$(document).click(function(event){
  if(event.target == profile || event.target == menu){
  } else {
    menu.style.display = "none";
  }
});

function addbio(){
  $(".name-and-bio form").css({"display":"block"});
  $(".add-bio").css({"display":"none"});
}
function nobio(){
  $(".name-and-bio form").css({"display":"none"});
  $(".add-bio").css({"display":"block"});
}

$("#cover_picture").change(function(){
  document.getElementById('cover_pic_form').submit()
});
$("#profile_img").change(function(){
  document.getElementById('profile_pic_form').submit()
});
