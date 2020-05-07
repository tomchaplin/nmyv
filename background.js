'use strict';

let appName = 'com.tom.nmyv'; 

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

const pauseVideoCMD = 'document.getElementsByTagName("video")[0].pause()';

chrome.browserAction.onClicked.addListener(function(tab) {
	chrome.tabs.query({active: true, lastFocusedWindow: true}, tabs => {
		let url = tabs[0].url;

		let parsed = parseURL(url);
		if(parsed.searchObject.v){
			let vid = parsed.searchObject.v;
			console.log(vid);
			chrome.runtime.sendNativeMessage(appName, {text: vid})
			chrome.tabs.executeScript({code: pauseVideoCMD});

		}
	});
});
