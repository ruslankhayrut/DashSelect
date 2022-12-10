# AUTO GENERATED FILE - DO NOT EDIT

#' @export
select <- function(id=NULL, class_name=NULL, disabled=NULL, multiple=NULL, options=NULL, size=NULL, style=NULL, value=NULL) {
    
    props <- list(id=id, class_name=class_name, disabled=disabled, multiple=multiple, options=options, size=size, style=style, value=value)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'Select',
        namespace = 'dash_select',
        propNames = c('id', 'class_name', 'disabled', 'multiple', 'options', 'size', 'style', 'value'),
        package = 'dashSelect'
        )

    structure(component, class = c('dash_component', 'list'))
}
