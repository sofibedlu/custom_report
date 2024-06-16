odoo.define('custom_sales_report.close_wizard', function (require) {
    "use strict";

    var ActionManager = require('web.ActionManager');

    ActionManager.include({
        _executeReportAction: function (action, options) {
            var result = this._super.apply(this, arguments);
            if (action.close_wizard) {
                this.dialog_close();
            }
            return result;
        },
    });
});