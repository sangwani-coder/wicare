function calculateDonationProgress(donation, donee) {
  const progress = (donation.amount_donated / donee.amount_needed) * 100;
  return `The ${donation.cause} cause has received ${progress}% of the required funding.`;
}


async function getDonee() {
  const response = await fetch('https://wicare.sangwani-coder.repl.co/api/donees/');
  const data = await response.json();
  return data;
}

async function getDonation() {
  const response = await fetch('https://wicare.sangwani-coder.repl.co/api/donations/');
  const data = await response.json();
  return data;
}

async function displayDonee() {
  const data = await getDonee();
  // assuming 'data' contains the array of objects
  let neededAmounts = {};
  let causes = [];
  let amounts = [];

  for (let i = 0; i < data.results.length; i++) {
    causes.push(data.results[i].cause);
    amounts.push(data.results[i].amount_needed);
  }
  console.log(causes);
  console.log(amounts);
}

async function displayDonation() {
  const data = await getDonation();
  // assuming 'data' contains the array of objects
  let causes = [];
  let amounts = [];

  for (let i = 0; i < data.results.length; i++) {
    causes.push(data.results[i].cause);
    amounts.push(data.results[i].amount_donated);
  }

  console.log(causes);
  console.log(amounts);

}

async function calculateTotalAmount(cause) {
  let doneeData = await getDonee();
  let doneeProperties = doneeData.results;

  let donationData = await getDonation();
  let donationProperties = donationData.results;

  const donatedAmounts = {};
  let donationTotal = 0;

  const neededAmounts = {};
  let neededTotal = 0;

  doneeProperties.forEach((property) => {
    const donee_cause = property.cause;
    const amount_needed = property.amount_needed;

    if (neededAmounts[donee_cause]) {
      neededAmounts[donee_cause] += amount_needed;
    } else {
      neededAmounts[donee_cause] = amount_needed;
    }

    neededTotal += amount_needed;
  });

  donationProperties.forEach((property) => {
    const donation_cause = property.cause;
    const amount_donated = property.amount_donated;

    if (donatedAmounts[donation_cause]) {
      donatedAmounts[donation_cause] += amount_donated;
    } else {
      donatedAmounts[donation_cause] = amount_donated;
    }

    donationTotal += amount_donated;
  });

  // console.log(neededAmounts); // Log the cause amounts for debugging
  // console.log(donatedAmounts); // Log the cause amounts for debugging


  return Math.round((donatedAmounts[cause] / neededAmounts[cause]) * 100);
}


function updateProgressBars() {
    // Get all progress bars
    var progressBars = document.querySelectorAll('.progress-bar');
  
    // Update each progress bar
    progressBars.forEach(async function(progressBar) {
      var totalAmount = 0;
      var progressValue = 0;
      var progressBarId = progressBar.getAttribute('id');
      
      switch(progressBarId) {
        case 'noPovertyProgress':
          totalAmount = await calculateTotalAmount('no poverty');
          if (isNaN(totalAmount)){
            progressValue = 0;
          }else {
            progressValue = totalAmount;
          }
          break;
        case 'zeroHungerProgress':
          totalAmount= await calculateTotalAmount('zero hunger');
          if (isNaN(totalAmount)){
            progressValue = 0;
          }else {
            progressValue = totalAmount;
          }
          break;
        case 'healthProgress':
          totalAmount = await calculateTotalAmount('health and well-being');
          if (isNaN(totalAmount)){
            progressValue = 0;
          }else {
            progressValue = totalAmount;
          }
          break;
        case 'educationProgress':
          totalAmount = await calculateTotalAmount('quality education for all');
          if (isNaN(totalAmount)){
            progressValue = 0;
          }else {
            progressValue = totalAmount;
          }
          break;
        case 'cleanWaterProgress':
          totalAmount = await calculateTotalAmount('clean water and sanitation');
          if (isNaN(totalAmount)){
            progressValue = 0;
          }else {
            progressValue = totalAmount;
          }
          break;
      }
      
      // Set progress bar values
      progressBar.style.width = progressValue + '%';
      progressBar.setAttribute('aria-valuenow', progressValue);
      progressBar.innerHTML = progressValue + '% Funded';
    });
  }