#stolen from http://chrismontrois.net/2016/01/30/handlebars-switch/
Handlebars.registerHelper "switch", (value, options) ->
  @_switch_value_ = value
  html = options.fn @
  delete @_switch_value_
  return html

Handlebars.registerHelper "case", (value, options) ->
  if value == @_switch_value_
    return options.fn @

# inspired by https://stackoverflow.com/questions/17934477/macros-in-handlebars#17939032
Handlebars.registerHelper "macro", (name, defaults) ->
  Handlebars.registerHelper name, (options) ->
    e = $.extend(@, defaults.hash, options.hash)
    return new Handlebars.SafeString(defaults.fn e)

Handlebars.registerHelper "ifAlbum", (options) ->
  if @kind == 'ALBUM'
    return options.fn(this)
  return options.inverse(this)
