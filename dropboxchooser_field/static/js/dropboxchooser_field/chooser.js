
(function() {

    function dropbox_chooser(){

        var chooser_field = document.querySelector('input[type=dropbox-chooser]');

        Dropbox.appKey = chooser_field.getAttribute("data-app-key");

        options = {
            linkType: "direct",

            success: function(files) {
                chooser_field.value = files[0].link
            }
        };
        
        // add extensions only if specified
        if(chooser_field.hasAttribute("data-extensions")) {
            options['extensions'] =  chooser_field.getAttribute("data-extensions")
                .split(" ");
        }

        var button = Dropbox.createChooseButton(options);
        chooser_field.parentNode.insertBefore(button, chooser_field);
    }

    $ = this.jQuery || this.Zepto || this.ender || this.$;

    if($) {
        $(dropbox_chooser);
    } else {
        window.onload = dropbox_chooser;
    }

})();
