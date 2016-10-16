#stolen from http://chrismontrois.net/2016/01/30/handlebars-switch/
Handlebars.registerHelper "switch", (value, options) ->
  @_switch_value_ = value
  html = options.fn @
  delete @_switch_value_
  return html

Handlebars.registerHelper "case", (value, options) ->
  if value == @_switch_value_
    return options.fn @
