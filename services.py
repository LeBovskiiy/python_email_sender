def get_email_lists():
    with open('emails.txt', 'r') as file:
        content = file.read()
        
    return content.strip().split('\n')

def _get_template():
    with open('index.html', 'r') as template:
        content = template.read()
        
    return content

def sub_text_in_template(*args, **kwargs):
    _template = _get_template()
    new_template = _template
    for key, value in kwargs.items():
        placeholder = "{" + key + "}"
        new_template = new_template.replace(placeholder, str(value))
        
    return new_template
