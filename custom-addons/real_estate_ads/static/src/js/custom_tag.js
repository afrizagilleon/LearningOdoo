/** @odoo-module **/

import {registry} from "@web/core/registry";
import { Component } from "@odoo/owl";

class CustomActions extends Component{}
CustomActions.template = "CustomActions"

registry.category("actions").add('custom_client_action', CustomActions)

