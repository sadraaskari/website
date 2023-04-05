/* global coreui */

/**
 * --------------------------------------------------------------------------
 * CoreUI Free Boostrap Admin Template (v4.2.2): popovers.js
 * Licensed under MIT (https://coreui.io/license)
 * --------------------------------------------------------------------------
 */

var toastTrigger = document.getElementById('liveToastBtn');
var toastLiveExample = document.getElementById('liveToast');
if (toastTrigger) {
  toastTrigger.addEventListener('click', function () {
    var toast = new coreui.Toast(toastLiveExample);
    toast.show();
  });
}
//# sourceMappingURL=toasts.js.map