// background.js

let color = '#3aa757';

chrome.runtime.onInstalled.addListener(() => {
  chrome.storage.sync.set({ color });
  console.log('Default background color set to %cgreen', `color: ${color}`);
});

let value = ''

chrome.storage.local.set({'selections': value}, function() {
  console.log('Value is set to ' + value);
  console.log(selections);
});

// var br = document.createElement("br"); 

// chrome.storage.local.set({'display': br}, function() {
//   console.log('Value is set to ' + br);
//   console.log(br);
// });