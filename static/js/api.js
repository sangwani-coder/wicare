function updateProgressBars() {
    // Get all progress bars
    var progressBars = document.querySelectorAll('.progress-bar');
  
    // Update each progress bar
    progressBars.forEach(function(progressBar) {
      var progressValue = 0;
      var progressBarId = progressBar.getAttribute('id');
      
      switch(progressBarId) {
        case 'noPovertyProgress':
          progressValue = 80;
          break;
        case 'zeroHungerProgress':
          progressValue = 67;
          break;
        case 'healthProgress':
          progressValue = 70;
          break;
        case 'educationProgress':
          progressValue = 90;
          break;
        case 'cleanWaterProgress':
          progressValue = 98;
          break;
      }
      
      // Set progress bar values
      progressBar.style.width = progressValue + '%';
      progressBar.setAttribute('aria-valuenow', progressValue);
      progressBar.innerHTML = progressValue + '% Funded';
    });
  }
  