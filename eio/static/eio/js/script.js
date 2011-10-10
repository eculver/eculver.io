/*
 *  File: script.js
 *  Created On: 10/9/11
 *  Created By: Evan Culver for eculver.io
 *  Details: Core JS.
 */

/*
 * Define EIO module. Don't taint the Global namespace any more than we need to.
 */
EIO = (function () {

    function EIO () {
    }

    EIO.prototype.init = function () {
        console.log('EIO module initialized');
    }

    return new EIO();
})();

/*
 *  Global onload events
 */
$(document).ready(function() {
    EIO.init();
});


