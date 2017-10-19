"use strict";
{
  chrome.webRequest.onHeadersReceived.addListener( 
    details => ({
      responseHeaders: Array.from( details.responseHeaders ).filter(
        header => header.name.toLowerCase() !== 'x-frame-options' 
      )
    }),
    {
      urls: ["<all_urls>"]
    }, 
    [
      "blocking", "responseHeaders"
    ]);
  /**
  chrome.webRequest.onBeforeRequest.addListener( 
    details => details.url.includes('stub') ? {cancel:true} : {cancel:false },
    {
      urls: ["<all_urls>"]
    }, 
    [
      "blocking", 
    ]);
  **/
  chrome.tabs.create({url:'/page/page.html'});
}
