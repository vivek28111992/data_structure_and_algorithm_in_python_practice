# Matching Tags in a Markup Language
# Function for testing if an HTML document has matching tags.

from array_based_stack_implemenatation import ArrayStack

def is_matched_html(raw):
    """Return True if all HTML tags are properly match; False otherwise."""
    S = ArrayStack()
    j = raw.find('<')                   # find first '<' character (if any)
    while j != -1:
        k = raw.find('>', j+1)          # find next '>' character
        if k == -1:
            return False                # invalid tag
        tag = raw[j+1:k]                # strip away < >
        if not tag.startswith('/'):     # this is opening tag
            S.push(tag)
        else:
            if S.is_empty():
                return False            # nothing to match with

            if tag[1:] != S.pop():
                return False            # mismatched delimiter
            
        j = raw.find('<', k+1)          # find next '<' character (if any)
    return S.is_empty()                 # were all opening tags matched?

raw = '<body><center><h1> The Little Boat </h1></center><p> The storm tossed the little boat like a cheap sneaker in an old washing machine. The three drunken fishermen were used to such treatment, of course, but not the tree salesman, who even as a stowaway now felt that he had overpaid for the voyage.</p><ol><li> Will the salesman die? </li><li> What color is the boat? </li><li> And what about Naomi? </li></ol></body>'
res = is_matched_html(raw)
print(res)
