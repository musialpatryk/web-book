from django.core.validators import FileExtensionValidator

def validate_image(file):
    validator = FileExtensionValidator(['jpg', 'png', 'jpeg'])
    try:
        validator(file)
    except:
        return False
    return True
