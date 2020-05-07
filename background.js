'use strict';

const appName = 'com.tom.nmyv'; 
const pauseVideoCMD = 'document.getElementsByTagName("video")[0].pause()';

function parseURL(url) {
    var parser = document.createElement('a'),
        searchObject = {},
        queries, split, i;
    // Let the browser do the work
    parser.href = url;
    // Convert query string to object
    queries = parser.search.replace(/^\?/, '').split('&');
    for( i = 0; i < queries.length; i++ ) {
        split = queries[i].split('=');
        searchObject[split[0]] = split[1];
    }
    return {
        protocol: parser.protocol,
        host: parser.host,
        hostname: parser.hostname,
        port: parser.port,
        pathname: parser.pathname,
        search: parser.search,
        searchObject: searchObject,
        hash: parser.hash
    };
}

// Accepts a url, attempts to pull out the video ID and passes it onto the host
// The host is responsible for check this is a good message before using it
function nmyvOpen(url) {
	let parsed = parseURL(url);
	if(parsed.searchObject.v){
		let vid = parsed.searchObject.v;
		console.log(vid);
		chrome.runtime.sendNativeMessage(appName, {text: vid})
	}
}

// Injects a command into the current tab to pause the first HTML5 video it finds
function pauseVideo(){
	chrome.tabs.executeScript({code: pauseVideoCMD});
}

// Listener for clicking on extension icon
chrome.browserAction.onClicked.addListener(function(tab) {
	chrome.tabs.query({active: true, lastFocusedWindow: true}, tabs => {
		pauseVideo();
		nmyvOpen(tabs[0].url);
	});
});

// Adding context menu item to open link with nmyv
chrome.contextMenus.create({
	id: 'nmyv_open',
	title: "Open with nmyv",
	targetUrlPatterns: ["*://*.youtube.com/*"],
	contexts: ['link']
});

// On click event listener for the context menu item
chrome.contextMenus.onClicked.addListener( function(info) {
	if( info.menuItemId == 'nmyv_open' ) {
		nmyvOpen(info.linkUrl);
	}
});

