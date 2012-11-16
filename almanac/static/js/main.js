(function ($) {

$(document).ready(function () {
    // venue filter
    var $venueSearch = $("#venue-search");
    if ($venueSearch) {
        $venueSearch.on("keyup", function () {
            var filterValue = $venueSearch.val().toLowerCase();

            $(".venue-name").each(function(index) {
                var $this = $(this);
                $this
                    .closest("li")
                    .toggle(filterValue.length === 0 || $this.text().toLowerCase().indexOf(filterValue) > -1);
            });
        });
    }
});

})(jQuery);
