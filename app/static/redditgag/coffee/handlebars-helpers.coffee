#stolen from http://chrismontrois.net/2016/01/30/handlebars-switch/
Handlebars.registerHelper "switch", (value, options) ->
  this._switch_value_ = value
  html = options.fn this
  delete this._switch_value_
  return html

Handlebars.registerHelper "case", (value, options) ->
  if value == this._switch_value_
    return options.fn this
