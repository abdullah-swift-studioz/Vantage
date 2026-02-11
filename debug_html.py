from html.parser import HTMLParser

class TagValidator(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.errors = []
        self.line_map = {} # Tag -> Start Line

    def handle_starttag(self, tag, attrs):
        if tag in ['br', 'img', 'meta', 'link', 'input', 'hr', 'source', 'path', 'circle', 'svg']: 
            return # Void elements or svgs that we might skip deep validation for
        
        # We really care about 'a' and 'div'
        if tag in ['a', 'div']:
            self.stack.append((tag, self.getpos()[0]))

    def handle_endtag(self, tag):
        if tag in ['br', 'img', 'meta', 'link', 'input', 'hr', 'source', 'path', 'circle', 'svg']:
            return

        if tag in ['a', 'div']:
            if not self.stack:
                self.errors.append(f"Unexpected closing tag </{tag}> at line {self.getpos()[0]}")
                return

            last_tag, start_line = self.stack[-1]
            if last_tag == tag:
                self.stack.pop()
            else:
                # Mismatch
                # Try to find if this closes an earlier tag (implying missing intermediate closes)
                # or if it's just extra.
                found = False
                for i in range(len(self.stack) - 1, -1, -1):
                    if self.stack[i][0] == tag:
                        found = True
                        # We found a match further down. Everything on top is unclosed.
                        for j in range(len(self.stack) - 1, i, -1):
                             self.errors.append(f"Unclosed <{self.stack[j][0]}> opened at line {self.stack[j][1]}")
                        self.stack = self.stack[:i] # Pop everything including correct one
                        break
                
                if not found:
                     self.errors.append(f"Unexpected closing tag </{tag}> at line {self.getpos()[0]}. Expected </{last_tag}>")

    def validate(self, filename):
        with open(filename, 'r') as f:
            self.feed(f.read())
        
        for tag, line in self.stack:
            self.errors.append(f"Unclosed <{tag}> opened at line {line}")

        return self.errors

validator = TagValidator()
errors = validator.validate('/Users/abdullah/Downloads/vantage/index.html')
for error in errors:
    print(error)
