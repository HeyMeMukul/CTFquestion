
document.addEventListener('DOMContentLoaded', function() {
    var flagElement = document.getElementById('flag');
  ;
  });
  
// _cl053_t0_th3_fl4g} 
  // Disable button click while it's being hovered over
const button = document.getElementById('click-me');

button.addEventListener('mouseover', function() {
  button.disabled = true;
});

button.addEventListener('mouseleave', function() {
  button.disabled = false;
});
