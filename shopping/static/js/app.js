eventListeners = {
  init: function() {
    // Ensure all flash messages fadeout after three seconds
    setTimeout(function () {
      $('#flash-message').fadeOut();
    }, 3000);
  }
};

$(document).ready(function () {
  eventListeners.init();
});
