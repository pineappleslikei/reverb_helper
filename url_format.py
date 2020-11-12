import re

pattern = r'https://drive.google.com/file/d/[A-za-z0-9-]+/view[?]usp=sharing$'


# make sure that the input is a google drive url pointing to a resource


def url_validate(url):
    match = re.match(pattern, url)
    if match:
        return True
    else:
        return None


# take the resource id from url


def photo_id_strip(url):
    photo_url = url.split('/')
    return photo_url[5]


# format new url that points to a download link for resource


def url_format(photo_id):
    new_url = f'https://drive.google.com/uc?id={photo_id}&export=download'
    return new_url
